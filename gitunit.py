#clean start
import pyglet
import glooey

#passwordChecker
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)
title = glooey.Label("Welcome to Password Checker")
enterPassword = glooey.Form()
button = glooey.Button("Check Password")
result = glooey.Label("")

def buttonClicked(widget):
    if enterPassword.text == "1234" or enterPassword.text == "123456" or enterPassword.text == "12345678" or enterPassword.text == "password" or enterPassword.text == "qwerty":
        result.set_text("Your password is too weak!")
    else:
        result.set_text("Your password is ok")
    


rows.add(title)
rows.add(enterPassword)
rows.add(button)
rows.add(result)
button.push_handlers(on_click=buttonClicked)

pyglet.app.run()
#test\
#asdasd
#asddfgh