import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join('images', 'upgrade_menu.png'))
UPGRADE_IMAGE = pygame.image.load(os.path.join('images', 'upgrade.png'))
SELL_IMAGE = pygame.image.load(os.path.join('images', 'sell.png'))

class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(MENU_IMAGE, (150, 150))
        self.upgrade_image = pygame.transform.scale(UPGRADE_IMAGE, (60, 40))
        self.sell_image = pygame.transform.scale(SELL_IMAGE, (30, 30))

        self.menu_rect = self.menu_image.get_rect()
        self.up_rect = self.upgrade_image.get_rect()
        self.sell_rect = self.sell_image.get_rect()

        self.menu_rect.center = (x, y)
        self.up_rect.center = (x, y-50)  # location of the upgrade button
        self.sell_rect.center = (x, y+55) # location of the sell button

        self.__buttons = [Button(self.upgrade_image, 'upgrade', self.up_rect.center[0], self.up_rect.center[1]),\
                            Button(self.sell_image, 'sell', self.sell_rect.center[0], self.sell_rect.center[1])]  # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, self.menu_rect)
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade_image, self.up_rect)
        win.blit(self.sell_image, self.sell_rect)
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.name = name

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






