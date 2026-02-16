import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    raise Exception("No controller detected")

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Connected to: {joystick.get_name()}")


def r3apply_deadzone(value, threshold=0.1):
    if abs(value) < threshold:
        return 0
    return value


def R3get_inputs():

    pygame.event.pump()  

    Steering = joystick.get_axis(0)
    Throttle_input = joystick.get_axis(2)


    Steering = r3apply_deadzone(Steering)

    throttle_normalized = (Throttle_input + 1) / 2
    throttle = int(throttle_normalized * 255)

    steering = int(Steering * 100)

    return throttle, steering
