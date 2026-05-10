from gpiozero import Motor
from time import sleep
from enum import IntEnum

from gpiozero import Device
from gpiozero.pins.lgpio import LGPIOFactory


class Commands(IntEnum):
    STOP = 0
    MOVE_FORWARD = 1
    MOVE_BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class GPIOMotorController:
    def __init__(self):
        Device.pin_factory = LGPIOFactory()
        self.motor1 = Motor(forward=6, backward=5)
        self.motor2 = Motor(forward=20, backward=21)

        self.motor1_speed = 0
        self.motor2_speed = 0

    def _set_motor_speed(self, motor, speed):
        if speed > 0:
            motor.forward(speed)
        elif speed < 0:
            motor.backward(-speed)
        else:
            motor.stop()

    def execute_command(self, command):
        if command == Commands.MOVE_FORWARD:
            print("Forward")
            self.motor1_speed += 0.1
            self.motor2_speed -= 0.1
        elif command == Commands.MOVE_BACKWARD:
            print("Backward")
            self.motor1_speed -= 0.1
            self.motor2_speed += 0.1
        elif command == Commands.LEFT:
            print("Left")
            self.motor1_speed -= 0.1
            self.motor2_speed -= 0.1
        elif command == Commands.RIGHT:
            print("Right")
            self.motor1_speed += 0.1
            self.motor2_speed += 0.1
        else:
            print("Stop")
            self.motor1_speed = 0
            self.motor2_speed = 0

        # clip speeds to [-1, 1]
        self.motor1_speed = max(-1, min(1, self.motor1_speed))
        self.motor2_speed = max(-1, min(1, self.motor2_speed))
        
        self._set_motor_speed(self.motor1, self.motor1_speed)
        self._set_motor_speed(self.motor2, self.motor2_speed)
    
