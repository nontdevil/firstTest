#clean start
import pyglet
import glooey

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
col = glooey.HBox()
mainGui.add(rows)
background = "#FF0000"
label = glooey.Label("Hello World")
label2 = glooey.Label("Hello Banana")
label3 = glooey.Label("Hello Cantaloupe")

form = glooey.Form("Enter password: ")

button = glooey.Button("Click Here!")


def buttonClicked(widget):
    print("Clicked!")

button.push_handlers(on_click=buttonClicked)

rows.add(button)
rows.add(form)
rows.add(label)
rows.add(label2)
rows.add(label3)

pyglet.app.run()
