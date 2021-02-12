import pygame

pygame.init()

display_width = 300
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Caroline Wanjiku')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('img1.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.75)
y = (display_height * 0.89)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
