import pygame

name = input("Enter your name: ")
pygame.init()

clr = (0, 0, 0)
w = len(name) * 100 + 100
win = pygame.display.set_mode((w, 500))

pygame.display.set_caption('My Name')
t = {}

for ch in "abcdefghijklmnopqrstuvwxyz":
    image = pygame.image.load(f"alphabets/{ch}.png")
    t[ch] = pygame.transform.scale(image, (100, 100))

img = []

for ch in name.lower():
    img.append(t[ch])
    
while True:
    
    win.fill(clr)
    x = 50
    for i in img:
        win.blit(i, (x, 50))
        x += 100
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
