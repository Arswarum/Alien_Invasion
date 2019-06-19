import sys, pygame

def check_keydown_events(event, ship):
    """
    Responds to keystrokes
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """
    Reacts to key release
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """
    Handles keystrokes and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

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