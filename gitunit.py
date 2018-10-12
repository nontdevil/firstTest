#clean start
import pyglet
import glooey

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)

label = glooey.Label("Hello World")
mainGui.add(label)

pyglet.app.run()