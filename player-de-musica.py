import pygame
pygame.init()

window = pygame.display.set_mode((380, 380))
pygame.display.set_caption("Guilherme")


background = pygame.image.load('foto2.jpg').convert()
background = pygame.transform.scale(background, (380, 380))

window.blit(background, (0, 0))
pygame.display .flip()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

font = pygame.font.Font(None, 36)

sound = pygame.mixer.Sound("Vestron Vulture - Judas Effect.mp3")

pygame.mixer.music.load('Vestron Vulture - Judas Effect.mp3')

pause_button = pygame.Rect(50, 300, 100, 40) 

play_button = pygame.Rect(180, 300, 100, 40)


pygame.mixer.music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause_button.collidepoint(event.pos):
                pygame.mixer.music.pause()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause_button.collidepoint(event.pos):
                pygame.mixer.music.play()


    pygame.draw.rect(window, white, pause_button)
    text = font.render("Pause", True, black)
    window.blit(text, (pause_button.x +15, pause_button.y + 10))

    pygame.draw.rect(window, white, play_button)
    text = font.render("Play", True, black)
    window.blit(text, (play_button.x +15, pause_button.y + 10))
    pygame.display.update()