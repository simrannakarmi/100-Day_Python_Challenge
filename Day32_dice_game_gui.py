import pygame
import random
import time

p = [
    pygame.transform.scale(pygame.image.load("dice-face-one.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("dice-face-two.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("dice-face-three.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("dice-face-four.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("dice-face-five.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("dice-face-six.png"), (50, 50))   
]

name1 = input("Enter the name of Player 1: ")
name2 = input("Enter the name of Player 2: ")

val1 = random.randint(1, 6)
val2 = random.randint(1, 6)

if val1 > val2:
    result = name1 + " Wins"
elif val1 < val2:
    result = name2 + " Wins"
else:
    result= "It is a DRAW"
    
pygame.init()
white = (255, 255, 255)
green = (0, 200, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont("Times New Roman", 22)

text1 = font.render(name1, True, green, blue)
text2 = font.render(name2, True, green, blue)
result = font.render(result, True, green, blue)

textRect1 = text1.get_rect(center = (150, 100))
textRect2 = text2.get_rect(center = (450, 100))
textRect3 = result.get_rect(center = (300, 50))

# Create window
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dice Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    win.blit(result, textRect3)
    win.blit(p[val1 - 1], (200, 250))
    win.blit(p[val2 - 1], (350, 250))
    
    pygame.display.update()
    
pygame.quit()