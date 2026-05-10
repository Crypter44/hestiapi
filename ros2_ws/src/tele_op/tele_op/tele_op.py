#!/usr/bin/env python3

from enum import IntEnum
from threading import Lock

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8
from tele_op.gpio import GPIOMotorController


class TeleOpNode(Node):
	def __init__(self):
		super().__init__('tele_op_node')

		self.declare_parameter('command_topic', 'tele_op_command')

		self._state_sub = self.create_subscription(
			UInt8,
			self.get_parameter('command_topic').value,
			self._state_callback,
			10,
		)

		self.gpio_controller = GPIOMotorController()

		self.get_logger().info(
			f'TeleOp node ready. Subscribed to topic: {self.get_parameter("command_topic").value}'
		)

	def _state_callback(self, msg: UInt8) -> None:
		self.gpio_controller.execute_command(msg.data)


def main(args=None):
	rclpy.init(args=args)
	node = TeleOpNode()

	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	finally:
		node.destroy_node()
		rclpy.shutdown()


if __name__ == '__main__':
	main()
