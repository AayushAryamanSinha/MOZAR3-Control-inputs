import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    raise Exception("No controller detected")

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Connected to: {joystick.get_name()}")


def apply_deadzone(value, threshold=0.1):
    if abs(value) < threshold:
        return 0
    return value


def get_inputs():

    pygame.event.pump()  

    left_stick_x = joystick.get_axis(0)
    rt_trigger = joystick.get_axis(5)


    left_stick_x = apply_deadzone(left_stick_x)

    throttle_normalized = (rt_trigger + 1) / 2
    throttle = int(throttle_normalized * 255)

    steering = int(left_stick_x * 100)

    return throttle + 1, -steering
