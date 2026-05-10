import sys
import select
import termios
import tty

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8


def read_single_key(timeout: float = 0.1) -> str | None:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if not ready:
            return None
        key = sys.stdin.read(1)
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class WASDCommandSender(Node):
    def __init__(self):
        super().__init__('wasd_command_sender')
        self.publisher_ = self.create_publisher(UInt8, 'tele_op_command', 10)
        self.get_logger().info('WASD Command Sender node has been started.')

    def send_command(self, command: int):
        msg = UInt8()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sent command: {command}')


def main(args=None):
    rclpy.init(args=args)
    node = WASDCommandSender()

    print('Press W/A/S/D to send commands, Q to quit. No Enter required.')
    try:
        while rclpy.ok():
            key = read_single_key()
            if key is None:
                continue
            key = key.upper()
            if key == 'Q':
                print('Quitting...')
                node.send_command(0)  # STOP
                break
            elif key == 'X':
                node.send_command(0)  # STOP
            elif key == 'W':
                node.send_command(1)  # MOVE_FORWARD
            elif key == 'S':
                node.send_command(2)  # MOVE_BACKWARD
            elif key == 'A':
                node.send_command(3)  # LEFT
            elif key == 'D':
                node.send_command(4)  # RIGHT
            else:
                print(f'Ignored key: {repr(key)}')
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()