import pgzrun

WIDTH = 1000
HEIGHT = 500

p = Actor('hippo', (100,100))
e = Actor("panda", (500,200))

p.speed = 3
e.speed = 2
gameover = False

def player_movement():
    if keyboard.W:
        p.y -= p.speed
    if keyboard.S:
        p.y += p.speed
    if keyboard.A:
        p.x -= p.speed
    if keyboard.D:
        p.x += p.speed
    # boundary handling
    if p.x < 0: # agar player left side se bahar ja raha h
        p.x = WIDTH # to right side pe dikhne lage
    if p.x > WIDTH: # vice versa
        p.x = 0 
    if p.y < 0:
        p.y = HEIGHT
    if p.y > HEIGHT:
        p.y = 0
    
def enemy_movement():
    if p.y > e.y:
        e.y += e.speed
    if p.y <= e.y:
        e.y -= e.speed
    if p.x > e.x:
        e.x += e.speed
    if p.x <= e.x:
        e.x -= e.speed

def check_collision():
    global gameover
    if e.colliderect(p):
        p.image = 'giraffe'
        gameover = True

def draw():
    if not gameover:
        screen.clear()
        e.draw()
        p.draw()
    else:
        screen.fill("crimson")
        screen.draw.text("Game Over", center = (WIDTH//2, HEIGHT//2),color= "white", fontsize=100 )

def update():
    player_movement()
    enemy_movement()
    check_collision()

pgzrun.go()

