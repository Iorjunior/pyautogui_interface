from tkinter import PhotoImage


class Style():
    def __init__(self):

        self.mouse_icon = PhotoImage(file=r"icons/mouse.png")
        self.keyboard_icon = PhotoImage(file=r"icons/keyboard.png")
        self.time_icon = PhotoImage(file=r"icons/time.png")

        self.play_icon = PhotoImage(file=r"icons/play.png")
        self.pause_icon = PhotoImage(file=r'icons/pause.png')

        self.delete_icon = PhotoImage(file=r'icons/delete.png')

        self.select_icon = PhotoImage(file=r'icons/select.png')

        self.navbar_color = '#418EF2'
        self.content_color = '#261B40'
        self.status_color = '#418EF2'

        self.card_color = '#5ABFA3'
