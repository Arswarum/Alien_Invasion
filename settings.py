class Settings():
    """
    Сlass to store all game settings Alien Invasion
    """
    def __init__(self):
        """
        Initiates game settings
        """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_speed_factor = 1.5 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed =3