#clean start
import pyglet
import glooey

#passwordChecker

class PandaLabel(glooey.Label):
    custom_font_size = 25
    custom_alignment = "center"
    custom_color = "ffe215"
    custom_bold = True

class TheButton(glooey.Button):
    custom_font_size = 15
    custom_alignment = "center"
    custom_color = "ff0000"
    custom_bold = False
class Result(glooey.Label):
    custom_font_size = 15
    custom_alignment = "left"
    custom_color = "ff0000"
    custom_bold = True
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)
title = PandaLabel("Welcome to Password Checker")
enterPassword = glooey.Form()
button = glooey.Button("Check Password")
result = Result("")

def buttonClicked(widget):
    if enterPassword.text == "1234" or enterPassword.text == "123456" or enterPassword.text == "12345678" or enterPassword.text == "password" or enterPassword.text == "qwerty":
        Result.custom_color = "ff0000"
        result.set_text("Your password is too weak!")
    else:
        Result.custom_color = "00ff00"
        result.set_text("Your password is ok")
    


rows.add(title)
rows.add(enterPassword)
rows.add(button)
rows.add(result)
button.push_handlers(on_click=buttonClicked)

pyglet.app.run()