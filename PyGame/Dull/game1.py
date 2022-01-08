# adjust the speed of enemy for every ten points
# create bullet for the enemy
# create the supply for player

# import the pygame
import pygame
# import random
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

screenX = 900
screenY = 800
# create the screen
screen = pygame.display.set_mode((screenX, screenY))

# Background image
background = pygame.image.load("img_1.png")

# title  and icon
pygame.display.set_caption("Cheese Power")
icon = pygame.image.load('halloween-black-cat.png')
pygame.display.set_icon(icon)

# Background sound
result = random.randint(0, 4)
if result % 2 == 0:
    mixer.music.load('(Paddy Sun) Sunflower - Sergey Yarovoy (1).wav')
    mixer.music.play(-1)
else:
    mixer.music.load('Yiruma - River Flows in You - Fingerstyle Guitar Cover.wav')
    mixer.music.play(-1)

# Image
image = pygame.image.load("rat.png")
imageX = 450
imageY = 600
changeX = 0
changeY = 0

# Bullet
bullet = pygame.image.load("cheese (3).png")
bulletX = 0
bulletY = imageY
change_bulletX = 0
change_bulletY = 1
bullet_state = "ready"

# Enemy
number_enemy = 5
enemy = []
enemyX = []
enemyY = []
changeEnemyX = []
changeEnemyY = []

for i in range(number_enemy):
    enemy.append(pygame.image.load("cat.png"))
    enemyX.append(random.randint(0, screenX - 63))
    enemyY.append(random.randint(0, 201))
    changeEnemyX.append(1)
    changeEnemyY.append(20)


# display image
def display(x, y):
    screen.blit(image, (x, y))


# Fire Bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))


#  display enemy
def display_enemy(x, y, i):
    screen.blit(enemy[i], (x, y))


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 40)

scoreX = 10
scoreY = 10


def display_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


# collision detecting
def isCollision(x, y, x1, y1):
    global collision
    collision = False
    distance = math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2))
    if distance < 50:
        collision = True
        collision_sound = mixer.Sound('Cat_Meow_2-Cat_Stevens-2034822903 (2).wav')
        print("Coloosion happens")
        mixer.Sound.play(collision_sound)


# Game Over Text
    game_over_font = pygame.font.Font("freesansbold.ttf", 70)


# game over
def display_game_over():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (screenX/2, screenY/2))


# game loop
isRunning = True
while isRunning:

    #     The Background Color RGB - Red, Green, Blue
    screen.fill((255, 255, 0))

    # Add the Background Image

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -0.7
                print("Left")
            if event.key == pygame.K_RIGHT:
                changeX = 0.7
                print("Right")
            if event.key == pygame.K_UP:
                changeY = -0.7
                print("Up")
            if event.key == pygame.K_DOWN:
                changeY = 0.7
                print("Down")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    print("Space")
                    bulletX = imageX
                    fire_bullet(imageX, imageY)
                    bulllet_sound = mixer.Sound('cartoon_04.wav')
                    mixer.Sound.play(bulllet_sound)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeX = 0
                changeY = 0

    # Image Movement
    imageX += changeX
    imageY += changeY
    if imageX <= 0:
        imageX = 0
    elif imageX > screenX - 104:
        imageX = screenX - 104
    if imageY <= 0:
        imageY = 0
    elif imageY > screenY - 64:
        imageY = screenY - 64
    display(imageX, imageY)

    # Enemy movement
    for i in range(number_enemy):

        if enemyY[i] > screenY:
            for j in range(number_enemy):
                enemyY[j] = 2000
            display_game_over()
            break

        enemyX[i] += changeEnemyX[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0

        elif enemyX[i] >= screenX - 64:
            enemyX[i] = screenX - 64

        if enemyX[i] == 0 or enemyX[i] == screenX - 64:
            changeEnemyX[i] *= -1
        if enemyX[i] == 0 or enemyX[i] == screenX - 64:
            enemyY[i] += changeEnemyY[i]

        isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = imageY
            bullet_state = "ready"
            enemyX[i] = random.randint(0, screenX - 63)
            enemyY[i] = random.randint(0, 201)
            score_value += 1

        display_enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= change_bulletY*2
    if bulletY <= 0:
        bulletY = imageY
        bullet_state = "ready"
    display_score(scoreX, scoreY)
    pygame.display.update()
