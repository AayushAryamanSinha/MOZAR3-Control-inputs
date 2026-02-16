import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Connected to:", joystick.get_name())
print("Axes:", joystick.get_numaxes())
print("Buttons:", joystick.get_numbuttons())
print("Hats:", joystick.get_numhats())

while True:
    pygame.event.pump()


    for i in range(joystick.get_numaxes()):
        val = joystick.get_axis(i)
        print(f"Axis {i}: {val:.3f}")


    for i in range(joystick.get_numbuttons()):
        if joystick.get_button(i):
            print(f"Button {i} pressed")


    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        if hat != (0, 0):
            print(f"Hat {i}: {hat}")

    print("------")
    pygame.time.wait(200)
