import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


win = Gtk.Window() # create some window
win.connect("destroy", Gtk.main_quit) #connect the x button to signal, so when x clicked the window will be closed
win.show_all() #show all(also any child) elements on the window
Gtk.main() #start the main loop