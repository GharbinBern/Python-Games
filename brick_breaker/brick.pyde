import random  # Add this line at the beginning of your code



class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = width / 2 - self.width / 2
        self.y = height - 10
        self.speed = 10

    def move(self, direction):
        if direction == "left":
            self.x = max(0, self.x - self.speed)
        elif direction == "right":
            self.x = min(width - self.width, self.x + self.speed)

    def display(self):
        fill(255, 255, 255)
        rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self):
        self.size = 20
        self.x = width / 2
        self.y = height / 2
        self.speed_x = 5
        self.speed_y = -5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.x <= 0 or self.x >= width - self.size:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

    def reset(self):
        self.x = width / 2
        self.y = height / 2
        self.speed_x *= random.choice([-1, 1])  # Corrected line
        self.speed_y *= random.choice([-1, 1])  # Corrected line


    def display(self):
        fill(255, 255, 255)
        ellipse(self.x, self.y, self.size, self.size)


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 30
        self.color = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        self.visible = True

    def display(self):
        if self.visible:
            fill(self.color)
            rect(self.x, self.y, self.width, self.height)

def setup():
    size(800, 600)
    global paddle, ball, bricks, lives, score
    paddle = Paddle()
    ball = Ball()
    bricks = []
    for i in range(0, width, 100):
        for j in range(50, 200, 50):
            bricks.append(Brick(i, j))
    lives = 3
    score = 0
    loop()  # Start the game loop


def draw():
    background(0)
    handle_input()
    move_objects()
    check_collisions()
    display_objects()
    display_score()
    check_game_over()


def check_game_over():
    global lives, bricks
    if lives <= 0:
        game_over("You lost! Press any key to restart.")
    elif all(not brick.visible for brick in bricks):
        game_over("You won! Press any key to restart.")


def game_over(message):
    textSize(32)
    fill(255)
    textAlign(CENTER)
    text(message, width / 2, height / 2)
    noLoop()


def handle_input():
    global paddle
    if keyPressed:
        if keyCode == LEFT:
            paddle.move("left")
        elif keyCode == RIGHT:
            paddle.move("right")


def move_objects():
    global ball
    ball.move()


def check_collisions():
    global paddle, ball, bricks, lives, score
    # Ball and paddle collisions
    if ball.y + ball.size / 2 >= paddle.y and ball.x >= paddle.x and ball.x <= paddle.x + paddle.width:
        ball.speed_y *= -1

    # Ball and brick collisions
    for brick in bricks:
        if brick.visible and ball.y - ball.size / 2 <= brick.y + brick.height and ball.y + ball.size / 2 >= brick.y and \
                ball.x >= brick.x and ball.x <= brick.x + brick.width:
            ball.speed_y *= -1
            brick.visible = False
            score += 1

    # Ball and wall collisions
    ball.check_collision()

    # Ball and floor collision (losing a life)
    if ball.y - ball.size / 2 >= height:
        lives -= 1
        ball.reset()


def display_objects():
    global paddle, ball, bricks
    paddle.display()
    ball.display()
    for brick in bricks:
        brick.display()


def display_score():
    textSize(24)
    fill(255)
    textAlign(LEFT)
    text("Lives: " + str(lives), 10, 30)
    textAlign(RIGHT)
    text("Score: " + str(score), width - 10, 30)


def keyPressed():
    global paddle, ball, bricks, lives, score
    if lives <= 0 or all(not brick.visible for brick in bricks):  # Check if the game is over
        setup()  # Reset game state
        loop()  # Restart the game loop
