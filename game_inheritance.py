
from random import randint as ri
from turtle import speed
import pgzrun

WIDTH = 700
HEIGHT = 500

#all the class logic

class player(Actor):
    #override the default contructor
    def __init__(self,image,speed=5):
     pos = ri(0,WIDTH), ri(0,HEIGHT) #generate a random x.y coordinate
     super().__init__(image, pos)  #call the parent class constructor and pass image and pos
     self.speed = speed

    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.angle = self.speed
            self.angle =+10
        elif keyboard.D:
            self.x += self.speed
            self.angle = -10

    def check_boundary(self):
        pass
p=player('panda')
def draw():
    screen.fill('black')
    screen.fill('black')
    p.draw()
    def update():
        p.move()
        p.check_boundary()

pgzrun.go()


