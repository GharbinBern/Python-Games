# Import the required modules
from random import randint

# Define the width and height of the window
WIDTH = 800
HEIGHT = 600

# Define the class for the player's spaceship
class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT - 50
        self.speed = 8
        self.bullets = []

    def move(self):
        if keyPressed and keyCode == LEFT:
            self.x = max(0, self.x - self.speed)
        elif keyPressed and keyCode == RIGHT:
            self.x = min(WIDTH, self.x + self.speed)

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y))

    def display(self):
        fill(255)
        rect(self.x - 10, self.y - 10, 20, 20)

# Define the class for the bullets
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 10

    def display(self):
        fill(0, 255, 0)
        ellipse(self.x, self.y, 5, 5)

# Define the class for the enemies
class Enemy:
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = 0
        self.size = 30
        self.speed = 3

    def move(self):
        self.y += self.speed

    def display(self):
        fill(255, 0, 0)
        rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

# Initialize the player's spaceship
player = Player()

# Initialize empty lists for bullets and enemies
bullets = []
enemies = []

def setup():
    size(WIDTH, HEIGHT)

def draw():
    background(0)
    handle_input()
    move_objects()
    check_collisions()
    display_objects()
    spawn_enemies_periodically()

def handle_input():
    player.move()
    if keyPressed and key == ' ':
        player.shoot()

def move_objects():
    player_bullets = player.bullets
    for bullet in player_bullets:
        bullet.move()

    for enemy in enemies:
        enemy.move()

def check_collisions():
    for bullet in player.bullets[:]:
        for enemy in enemies[:]:
            if dist(bullet.x, bullet.y, enemy.x, enemy.y) < 20:
                player.bullets.remove(bullet)
                enemies.remove(enemy)

    for enemy in enemies:
        if dist(player.x, player.y, enemy.x, enemy.y) < 20:
            game_over()

def display_objects():
    player.display()
    for bullet in player.bullets:
        bullet.display()
    for enemy in enemies:
        enemy.display()

def game_over():
    fill(255)
    textSize(40)
    textAlign(CENTER)
    text("Game Over", WIDTH / 2, HEIGHT / 2)
    noLoop()

# Function to spawn enemies periodically
def spawn_enemies():
    enemies.append(Enemy())

# Call the spawn_enemies function repeatedly to keep spawning enemies
def spawn_enemies_periodically():
    if frameCount % 60 == 0:
        spawn_enemies()
