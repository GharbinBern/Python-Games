import random  
pressed_keys = set()

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80
        self.speed = 5

    def move_up(self):
        self.y = max(0, self.y - self.speed)

    def move_down(self):
        self.y = min(height - self.height, self.y + self.speed)

    def display(self):
        fill(255)
        rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.y <= 0 or self.y >= height:
            self.speed_y *= -1

    # Inside the Ball class
    def reset(self):
        self.x = width / 2
        self.y = height / 2
        self.speed_x *= random.choice([-1, 1])  # Use random.choice() correctly
        self.speed_y *= random.choice([-1, 1])  # Use random.choice() correctly
    
    def display(self):
        fill(255)
        ellipse(self.x, self.y, self.size, self.size)


def setup():
    size(800, 400)
    global paddle1, paddle2, ball, player1_score, player2_score
    paddle1 = Paddle(20, height / 2 - 40)
    paddle2 = Paddle(width - 30, height / 2 - 40)
    ball = Ball(width / 2, height / 2)
    player1_score = 0
    player2_score = 0
    global pressed_keys
    pressed_keys = set()


def draw():
    background(0)
    handle_input()
    move_objects()
    check_collisions()
    display_objects()
    display_scores()


def handle_input():
    global paddle1, paddle2, pressed_keys
    # Player 2 (arrow keys)
    if CODED in pressed_keys:
        if UP in pressed_keys:
            paddle2.move_up()
        if DOWN in pressed_keys:
            paddle2.move_down()
    # Player 1 (w/s)
    if ord('w') in pressed_keys:
        paddle1.move_up()
    if ord('s') in pressed_keys:
        paddle1.move_down()

def keyPressed():
    global pressed_keys
    if key == CODED:
        pressed_keys.add(CODED)
        pressed_keys.add(keyCode)
    else:
        pressed_keys.add(ord(key))

def keyReleased():
    global pressed_keys
    if key == CODED:
        pressed_keys.discard(keyCode)
        # Remove CODED if no arrow keys are pressed
        if not any(k in pressed_keys for k in [UP, DOWN, LEFT, RIGHT]):
            pressed_keys.discard(CODED)
    else:
        pressed_keys.discard(ord(key))


def move_objects():
    global ball
    ball.move()


def check_collisions():
    global paddle1, paddle2, ball, player1_score, player2_score
    # Ball and paddle collisions
    if ball.x <= paddle1.x + paddle1.width and paddle1.y <= ball.y <= paddle1.y + paddle1.height:
        ball.speed_x *= -1
    elif ball.x >= paddle2.x - ball.size and paddle2.y <= ball.y <= paddle2.y + paddle2.height:
        ball.speed_x *= -1

    # Ball and wall collisions
    ball.check_collision()

    # Ball and score zone collisions
    if ball.x < 0:
        player2_score += 1
        ball.reset()
    elif ball.x > width:
        player1_score += 1
        ball.reset()


def display_objects():
    global paddle1, paddle2, ball
    paddle1.display()
    paddle2.display()
    ball.display()


def display_scores():
    textSize(32)
    fill(255)
    textAlign(CENTER)
    text(player1_score, width / 4, 50)
    text(player2_score, width * 3 / 4, 50)
