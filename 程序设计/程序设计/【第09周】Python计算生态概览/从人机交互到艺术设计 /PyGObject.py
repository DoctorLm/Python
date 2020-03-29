#PyGObject: 使用GTK+开发GUI的功能库
#提供了整合GTK+、WebKitGTK+等库的功能 - GTK+:跨平台的一种用户图形界面GUI框架
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World") window.show()
window.connect("destroy", Gtk.main_quit) Gtk.main()
