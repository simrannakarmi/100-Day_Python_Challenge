import pygame
import random

pygame.init()

dice_size = (80, 80)
p = [
    pygame.transform.scale(pygame.image.load("dice-face-one.png"), dice_size),
    pygame.transform.scale(pygame.image.load("dice-face-two.png"), dice_size),
    pygame.transform.scale(pygame.image.load("dice-face-three.png"), dice_size),
    pygame.transform.scale(pygame.image.load("dice-face-four.png"), dice_size),
    pygame.transform.scale(pygame.image.load("dice-face-five.png"), dice_size),
    pygame.transform.scale(pygame.image.load("dice-face-six.png"), dice_size)   
]

name1 = input("Enter the name of Player 1: ")
name2 = input("Enter the name of Player 2: ")

val1 = random.randint(1, 6)
val2 = random.randint(1, 6)

if val1 > val2:
    result = f"{name1} Wins!"
elif val1 < val2:
    result = f"{name2} Wins!"
else:
    result= "It is a DRAW!"

# Colors
bg_color = (20, 20, 30)
text_color = (230, 230,230)
highlight_color = (72, 201, 176)
result_color = (255, 165, 0)

# Font
font = pygame.font.SysFont("Times New Roman", 30)
result_font = pygame.font.SysFont("Arial", 40, bold=True)

# Render text with colors
text1 = font.render(name1, True, highlight_color)
text2 = font.render(name2, True, highlight_color)
result = result_font.render(result, True, result_color)

# Create window
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dice Game")

textRect1 = text1.get_rect(center = (200, 100))
textRect2 = text2.get_rect(center = (400, 100))
textRect3 = result.get_rect(center = (300, 500))

dice1_pos = (175, 200)
dice2_pos = (375, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(bg_color)
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    win.blit(p[val1 - 1], dice1_pos)
    win.blit(p[val2 - 1], dice2_pos)
    win.blit(result, textRect3)
    
    pygame.display.update()
    
pygame.quit()