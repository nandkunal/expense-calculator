import simplegui
message="Hello Gui"
def click():
    global message
    message="Clicked"

frame=simplegui.create_frame("Home",300,200)
