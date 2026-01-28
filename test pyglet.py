import pyglet
from pyglet.window import key

window = pyglet.window.Window(720,480,"epstein window",resizable=True)

keys = key.KeyStateHandler()
window.push_handlers(keys)

player_img = pyglet.image.load("skelly_no_arc.png")
player = pyglet.sprite.Sprite(player_img, x=100, y=100)

velocity_y = 0
gravity = -15000

@window.event
def on_draw():
    window.clear()
    player.draw()

def update(dt):
    if keys[key.LEFT]:
        player.x -= 200 * dt
    if keys[key.RIGHT]:
        player.x += 200 * dt

    global velocity_y

    velocity_y += gravity * dt
    player.y += velocity_y * dt

    if player.y < 50:
        player.y = 50
    velocity_y = 0

    if keys[key.SPACE] and player.y == 50:
        velocity_y = 3000


pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
