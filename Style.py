from tkinter import Tk, Menu, Frame, RIGHT, Canvas, messagebox
from PFD import Pad

class style():

    def __init__(self, Pad):# i still need a muscle file to link these two
        self.Pad = pad
    
    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command( label = "New File", accelerator = "Ctrl+N", command= self.on_new_clicked)
        self.file_menu.add_command(label = "Open File", accelerator = "Ctrl+O", command= self.on_open_clicked)
        self.file_menu.add_command(label = "Save", accelerator = "Ctrl+S", command = self.on_save_clicked)
        self.file_menu.add_command(label = "Save As", accelerator = "Ctrl+Shift+S", command = self.on_save_as_clicked)
        self.file_menu.add_command(label = "Recent File", command= self.on_recent_file_clicked)
        self.menu_bar.add_cascade(label= "File", menu=self.file_menu)
        self.muscle.config(menu= None)#something is here
    
    def create_edit_menu(self):
        self.edit_menu = Menu(self.menu_bar, tearoff= 0)
        self.edit_menu.add_command(label = "Undo", accelerator = "Ctrl+Z", command=self.on_undo_clicked)
        self.edit_menu.add_command(label = "Redo", accelerator = "Ctrl+Y", command= self.on_redo_clicked)
        self.edit_menu.add_command(label = "Copy", accelerator = "Ctrl+C", command= self.on_copy_clicked)
        self.edit_menu.add_command(label = "Paste", accelerator = "Ctrl+P", command= self.on_paste_clicked)
        self.menu_bar.add_cascade(label = "Edit", command= self.edit_menu)
        self.muscle.config(menu= None)#something is here too

    def create_view_menu(self):
        # the most strainous thing i would experience
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label= "Run", accelerator = "F5", command= self.on_run_clicked)
        self.view_menu.add_command(label = "Create Dump File", command= self.on_dump_clicked)
        self.view_menu.add_command(label= "Preference", command= self.on_theme_clicked)#i used theme instead of preference 
        self.menu_bar.add_cascade(Label = "View", command= self.view_menu)

    def create_help_menu(self):
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label= "About", command= self.on_about_clicked)
        self.help_menu.add_command(label= "License", command = self.on_info_clicked)
        self.help_menu.add_command(accelerator = "Ctrl+F", command = self.on_find_clicked)
        self.menu_bar.add_cascade(label= "Help", command= self.help_menu)
        self.muscle.config(menu=None)#something here too

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# ill be needing a lot of textboxes and i mean a awfull lot
    def on_new_clicked(self):
        Pad(name)# dont know if this should do the trick, besides pad has no attribute name

    def on_open_clicked(self):
        #honestly i'll like to say i know how this would look like but its too early too lie
        pass

    def on_save_clicked(self):
        pass
    
    def on_save_as_clicked(self):
        pass
    
    def on_recent_file_clicked(self):
        pass
#this one is not understandable
#*#*#*#*#*#*##**##*#**#*#*#*#*#*#*#*#*#***#*#*#*#*##*#*#
#the edit menu properties
    def on_undo_clicked(self):
        pass
    
    def on_redo_clicked(self):
        pass

    def on_copy_clicked(self):
        pass
    
    def on_paste_clicked(self):
        pass
    
#*#*#*#*#*#*##**##*#**#*#*#*#*#*#*#*#*#***#*#*#*#*##*#*#
    def on_run_clicked(self):
        pass

    def on_dump_clicked(self):
        pass

    def on_theme_clicked(self):
        pass
#*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*

def on_about_clicked():
    messagebox.showinfo(
        "About", "{}{}".format(Pad, "Pad Foundation Design Engine\n (C) copyright 2018"))
    #this should do it, dont have any thing by the name PROGRAM_NAME

def on_info_clicked():
    with open("license.txt", rt) as me:
        data = me.read()#show print this with Tk
        #should put a text box for ok that closes the file
#*#*##*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
        

def main(muscle):
    root= Tk()
    root.title = "Pyramid Pad Foundation Design Engine"
    style(root, muscle)
    root.mainloop()

def startup():
    pass

"""
remember to root(destroy) on exit
add accelerator to the ones that apply
"""
