import sys, pygame

def check_events():
    """
    handles keystrokes and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """
    updates the image on the screen and displays the new screen
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    screen.fill(ai_settings.bg_color)  # background color assignment
    ship.blitme()  # display the ship

    pygame.display.flip()  # display the last-drawn screen