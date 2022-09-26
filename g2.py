import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 900


c = Actor('hippo',(50,50))
w = Actor('giraffe',(50,50))
panda = Actor('panda', (randint(100,900), randint(100,500)))
score = 0 # variable (global)
speed = 5 # variable (global)

def draw():
    c.draw()
    w.draw()
    screen.draw.text("A Chicken Story", (10,10), color='red')
    screen.draw.text(f"Score: {score}", (900,10), color='red')
    panda.draw()

def update():
    global score
    if keyboard.W:
        c.y -= speed
    elif keyboard.S:
        c.y += speed
    elif keyboard.A:
        c.x -= speed
    elif keyboard.D:
        c.x += speed

    if c.colliderect(panda):
        score +=1
        panda.pos = (randint(100,900), randint(100,500))
    
pgzrun.go()

