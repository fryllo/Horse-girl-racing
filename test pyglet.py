import pyglet

window = pyglet.window.Window(720,480,"epstein window",resizable=True)

player_img = pyglet.image.load("OIP.webp")
player = pyglet.sprite.Sprite(player_img, x=100, y=100)

@window.event
def on_draw():
    window.clear()
    player.draw()


pyglet.app.run()