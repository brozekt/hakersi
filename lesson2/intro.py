# here we define window width and height
WIDTH = 800
HEIGHT = 420

# here we "say" that we need pg zero library, so Python can "load" it
import pgzrun

# here we create our spaceship
spaceship = Actor('spaceship')
spaceship.angle = 90
spaceship.pos = 100, 56

# the following block draws all our elements on the screen
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    spaceship.draw()

# and finally we give a signal to python to start the game
pgzrun.go()