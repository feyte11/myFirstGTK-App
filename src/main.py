import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="Hello World") #from parent class we get the title ande name it

        self.button = Gtk.Button(label="Click Here") #a button object with label "Click Here"
        self.button.connect("clicked", self.on_button_clicked) #Connect the buttonn with the event "clicked" and func on_button_clicked
        self.add(self.button) #add the button to the window
    
    def on_button_clicked(self, widget) -> None: #func when button will be clicked 
        print("Hello World")

win = MyWindow() #instance of the class 

# win = Gtk.Window() # create some window
win.connect("destroy", Gtk.main_quit) #connect the x button to signal, so when x clicked the window will be closed
win.show_all() #show all(also any child) elements on the window
Gtk.main() #start the main loop