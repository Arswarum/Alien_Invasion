import sys, pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    Responds to keystrokes
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """
    Reacts to key release
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """
    Handles keystrokes and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien, bullets):
    """
    updates the image on the screen and displays the new screenaz
    """
    screen.fill(ai_settings.bg_color)  # background color assignment
    # All bullets are displayed behind images of the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # display the ship
    alien.blitme() #display the alien

    pygame.display.flip()  # display the last-drawn screen

def update_bullets(bullets):
    """
    Updates bullet positions and destroys old bullets.
    """
    bullets.update() # Bullet positions update
    # Removing bullets beyond the edge of the screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
           bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Fires a bullet if the maximum has not yet been reached
    """
    # Creating a new bullet and including it in the group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)