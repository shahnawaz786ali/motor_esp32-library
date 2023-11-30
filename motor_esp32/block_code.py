from machine import Pin, PWM
import time

class MotorController:
    def __init__(self):
        # Define motor pins
        self.motor_1_pin1 = Pin(12, Pin.OUT)
        self.motor_1_pin2 = Pin(13, Pin.OUT)
        self.motor_1_enable_pin = PWM(Pin(14))

        self.motor_2_pin1 = Pin(2, Pin.OUT)
        self.motor_2_pin2 = Pin(4, Pin.OUT)
        self.motor_2_enable_pin = PWM(Pin(15))

    # Function to set motor speed and direction based on power percentage
    def set_motor_speed(self, motor_enable_pin, motor_pin1, motor_pin2, power_percent):
        if power_percent < -100:
            power_percent = -100
        elif power_percent > 100:
            power_percent = 100

        speed = int((power_percent / 100) * 1023)

        if speed > 0:
            motor_pin1.on()
            motor_pin2.off()
        elif speed < 0:
            motor_pin1.off()
            motor_pin2.on()
        else:
            motor_pin1.off()
            motor_pin2.off()

        motor_enable_pin.duty(abs(speed))

    # Function to move motors forward
    def move_forward(self, power_percent, duration):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, power_percent)
        time.sleep(duration)
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, 0)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, 0)

    # Function to move motors backward
    def move_backward(self, power_percent, duration):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, -power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, -power_percent)
        time.sleep(duration)
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, 0)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, 0)

    # Function to turn motors left
    def move_left(self, power_percent, duration):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, -power_percent)
        time.sleep(duration)
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, 0)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, 0)

    # Function to turn motors right
    def move_right(self, power_percent, duration):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, -power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, power_percent)
        time.sleep(duration)
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, 0)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, 0)

    # Function to stop motors
    def stop_movement(self):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, 0)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, 0)
        
    def forward(self, power_percent):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, power_percent)

    def backward(self, power_percent):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, -power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, -power_percent)

    def left(self, power_percent):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, -power_percent)

    def right(self, power_percent):
        self.set_motor_speed(self.motor_1_enable_pin, self.motor_1_pin1, self.motor_1_pin2, -power_percent)
        self.set_motor_speed(self.motor_2_enable_pin, self.motor_2_pin1, self.motor_2_pin2, power_percent)

    def motor_movement(self, movement_type, power_percent):
        if movement_type == "forward":
            self.forward(power_percent)
        elif movement_type == "backward":
            self.backward(power_percent)
        elif movement_type == "left":
            self.left(power_percent)
        elif movement_type == "right":
            self.right(power_percent)