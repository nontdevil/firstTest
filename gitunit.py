#clean start
import pyglet
import glooey
import random


#passwordChecker

class PandaLabel(glooey.Label):
    custom_font_size = 25
    custom_alignment = "center"
    custom_color = "ffe215"
    custom_bold = True

class TheButton(glooey.Button):
    class Label(glooey.Label):
        custom_padding = 10
    class Base(glooey.images.Background):
        custom_outline = "ffffff"
        custom_color = "00ffad"
    class Over(glooey.images.Background):
        custom_outline = "ffffff"
        custom_color = "0000ff"
    class Down(glooey.images.Background):
        custom_outline = "00ff00"
        custom_color = "00ff00"

class Result(glooey.Label):
    custom_font_size = 15
    custom_alignment = "left"
    custom_color = "ff0000"
    custom_bold = True


class SomeFrame(glooey.Frame):
    class Decoration(glooey.images.Background):
        custom_color = "00ffa5"
        custom_outline = "000000"
    class Box(glooey.Bin):
        custom_padding = 2

class Generate(TheButton):
    class Base(glooey.images.Background):
        custom_outline = "ffff00"
        custom_color = "ffff00"
    class Over(glooey.images.Background):
        custom_outline = "ff0000"
        custom_color = "ff0000"
    class Down(glooey.images.Background):
        custom_outline = "ffffff"
        custom_color = "a24f21"



def buttonClicked(widget):
    if enterPassword.text == "1234" or enterPassword.text == "123456" or enterPassword.text == "12345678" or enterPassword.text == "password" or enterPassword.text == "qwerty":
        Result.custom_color = "ff0000"
        result.set_text("Your password is too weak!")
    else:
        Result.custom_color = "00ff00"
        result.set_text("Your password is ok")
    print(enterPassword.text)

def generatePasswordClicked(widget):
    result.set_text(str(random.randint(123456789,999999999)))


frame = SomeFrame()


mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
title = PandaLabel("Welcome to Password Checker")
enterPassword = glooey.Form()
button = TheButton("Check Password")
result = Result("")

mainGui.add(frame)

generatePassword = Generate("Generate")

rows.add(title)
rows.add(enterPassword)
rows.add(button)
rows.add(result)
rows.add(generatePassword)
button.push_handlers(on_click=buttonClicked)
generatePassword.push_handlers(on_click=generatePasswordClicked)
frame.add(rows)

pyglet.app.run()