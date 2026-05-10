from gpiozero import Motor
from time import sleep

from gpiozero import Device
from gpiozero.pins.lgpio import LGPIOFactory

Device.pin_factory = LGPIOFactory()

what_motor = str(input("What motor do you want to use: 'A' or 'B'")).lower()
# L298N wiring (BCM)
if what_motor == 'a':
    motor = Motor(forward=6, backward=5)
else:
    motor = Motor(forward=20, backward=21)

print("Controls:")
print("f - forward")
print("b - backward")
print("s - stop")
print("e - exit")

speed = 0.5  # 0.0 to 1.0
direction = "s"

while True:
    x = input()

    if x == 'f':
        print("forward")
        motor.forward(speed)

    elif x == 'b':
        print("backward")
        motor.backward(speed)

    elif x == 's':
        print("stop")
        motor.stop()

    elif x == 'e':
        motor.stop()
        break

    elif x == 'l':
	    print("low")
	    speed = 0.25

    elif x == 'm':
	    print("medium")
	    speed = 0.5

    elif x == 'h':
	    print("high")
	    speed = 0.75
    else:
        print("invalid input")
