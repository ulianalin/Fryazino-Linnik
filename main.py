import os
import sys

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("крест")

    size = width, height = 300, 200

    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    w = 32
    h = 17
    hw = 15
    all_sprites = pygame.sprite.Group()
    def load_image(name, colorkey=None):
        fullname = os.path.join(name)
        # если файл не существует, то выходим

        image = pygame.image.load(fullname)
        return image

    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("image11.bmp")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    for y in range(0, 14):
        for x in range(0, 12):
            x0 = x * w - (y % 2) * hw - 1
            y0 = y * h - 1
            pygame.draw.rect(screen, pygame.Color("white"), (x0, y0, w, h))
            pygame.draw.rect(screen, pygame.Color("red"), (x0 + 1, y0 + 1, w - 2, h - 2))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
