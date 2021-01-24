from tkinter import *
from tkinter import ttk
import time
import pyautogui
import threading

from style import Style
from interpreter import Interpreter


class Application():
    def __init__(self, master):

        self.style = Style()

        self.cardframe_list = []
        self.cardframe_type_list = []

        self.master = master
        self.master.configure(bg=self.style.navbar_color)

        self.navbar_frame = Frame(self.master, bg=self.style.navbar_color)
        self.navbar_frame.pack(fill=X, pady=10)

        self.status_frame = Frame(
            self.master, bg=self.style.status_color)
        self.status_frame.pack(side=BOTTOM, fill=X)

        self.content_frame = Frame(
            self.master, bg=self.style.content_color)
        self.content_frame.pack(fill=BOTH, expand=True)

        self.status_label = Label(
            self.status_frame, bg=self.style.status_color, text='Press Play to Start')
        self.status_label.pack()

        self.mouse_button = Button(
            self.navbar_frame, image=self.style.mouse_icon, relief=FLAT, bg=self.style.navbar_color)
        self.mouse_button.bind("<ButtonRelease-1>", self.add_cardframe_mouse)
        self.mouse_button.pack(side=LEFT)

        self.keyboard_button = Button(self.navbar_frame, image=self.style.keyboard_icon,
                                      relief=FLAT, bg=self.style.navbar_color)
        self.keyboard_button.bind(
            "<ButtonRelease-1>", self.add_cardframe_keyboard)
        self.keyboard_button.pack(side=LEFT)

        self.time_button = Button(
            self.navbar_frame, image=self.style.time_icon, relief=FLAT, bg=self.style.navbar_color)
        self.time_button.bind("<ButtonRelease-1>", self.add_cardframe_time)
        self.time_button.pack(side=LEFT)

        self.play_button = Button(
            self.navbar_frame, image=self.style.play_icon, relief=FLAT, bg=self.style.navbar_color)
        self.play_button.bind("<ButtonRelease-1>", self.play)
        self.play_button.pack(side=RIGHT)

        self.stop_button = Button(
            self.navbar_frame, image=self.style.pause_icon, relief=FLAT, bg=self.style.navbar_color)
        self.stop_button.bind("<ButtonRelease-1>", self.teste)
        self.stop_button.pack(side=RIGHT)

        self.tasks = []

    def add_cardframe_mouse(self, event=None):

        card_frame = Frame(self.content_frame, height=60, width=240,
                           bg=self.style.card_color)
        card_frame.pack(pady=2, fill=X)

        arrow_label = Label(card_frame, text='>', height=2)
        arrow_label.pack(side=LEFT)

        type_of_clicl_combo = ttk.Combobox(
            card_frame, values=['Click', 'DoubleClick'], width=12)
        type_of_clicl_combo.set('Click')
        type_of_clicl_combo.pack(side=LEFT, padx=5, pady=10)

        pos_x_label = Label(card_frame, text='X :', bg=self.style.card_color)
        pos_x_label.pack(side=LEFT, padx=2)

        pos_x_entry = Entry(card_frame, relief=FLAT, width=5)
        pos_x_entry.pack(side=LEFT)
        pos_x_entry.insert(0, '0')

        pos_y_label = Label(card_frame, text='Y :', bg=self.style.card_color)
        pos_y_label.pack(side=LEFT, padx=2)

        pos_y_entry = Entry(card_frame, relief=FLAT, width=5)
        pos_y_entry.pack(side=LEFT)
        pos_y_entry.insert(0, '0')

        get_pos_button = Button(card_frame, image=self.style.select_icon,
                                cursor='circle', relief=FLAT, bg=self.style.card_color)
        get_pos_button.bind("<ButtonRelease-1>", self.pos_mouse_track)
        get_pos_button.pack(side=LEFT, padx=2)

        delete_button = Button(
            card_frame, image=self.style.delete_icon, relief=FLAT, bg=self.style.card_color)
        delete_button.bind("<ButtonRelease-1>", self.delete_cardframe)
        delete_button.pack(side=RIGHT)

        self.cardframe_list.append(card_frame)
        self.cardframe_type_list.append('click')

    def pos_mouse_track(self, event=None):

        widget = event.widget
        widget_parent = widget.winfo_parent()

        for x in self.cardframe_list:
            if str(x) == widget_parent:

                widget_childs = x.slaves()

                pos_x_entry = widget_childs[3]
                pos_y_entry = widget_childs[5]

                mouse_x, mouse_y = pyautogui.position()

                pos_x_entry.delete(0, END)
                pos_x_entry.insert(0, mouse_x)

                pos_y_entry.delete(0, END)
                pos_y_entry.insert(0, mouse_y)

    def add_cardframe_time(self, event=None):

        card_frame = Frame(self.content_frame, height=60, width=240,
                           bg=self.style.card_color)
        card_frame.pack(pady=2, fill=X)

        arrow_label = Label(card_frame, text='>', height=2)
        arrow_label.pack(side=LEFT)

        time_entry = Entry(card_frame, relief=FLAT, width=5)
        time_entry.pack(side=LEFT, padx=5)
        time_entry.insert(0, '10')

        type_of_times_combo = ttk.Combobox(
            card_frame, values=['Seconds', 'Minutes', 'Hours'], width=12)
        type_of_times_combo.set('Seconds')
        type_of_times_combo.pack(side=LEFT, padx=2, pady=10)

        delete_button = Button(
            card_frame, image=self.style.delete_icon, relief=FLAT, bg=self.style.card_color)
        delete_button.bind("<ButtonRelease-1>", self.delete_cardframe)
        delete_button.pack(side=RIGHT)

        self.cardframe_list.append(card_frame)
        self.cardframe_type_list.append('sleep')

    def add_cardframe_keyboard(self, event=None):

        card_frame = Frame(self.content_frame, height=60, width=240,
                           bg=self.style.card_color)
        card_frame.pack(pady=2, fill=X)

        arrow_label = Label(card_frame, text='>', height=2)
        arrow_label.pack(side=LEFT)

        text_label = Label(card_frame, text='Text:', bg=self.style.card_color)
        text_label.pack(side=LEFT, padx=5)

        time_entry = Entry(card_frame, relief=FLAT, width=30)
        time_entry.pack(side=LEFT, padx=2)
        time_entry.insert(0, 'Hello, Word!!')

        delete_button = Button(
            card_frame, image=self.style.delete_icon, relief=FLAT, bg=self.style.card_color)
        delete_button.bind("<ButtonRelease-1>", self.delete_cardframe)
        delete_button.pack(side=RIGHT)

        self.cardframe_list.append(card_frame)
        self.cardframe_type_list.append('keyboard')

    def delete_cardframe(self, event=None):
        widget_call = event.widget
        cardframe_reference = widget_call.winfo_parent()

        for x in self.cardframe_list:
            if str(x) == cardframe_reference:

                self.cardframe_list.remove(x)

                x.destroy()

    def play(self, event):

        self.status_label.configure(text="Processing....")

        self.tasks = {}

        y = 0
        for x in self.cardframe_list:
            widget_childs = x.slaves()

            if self.cardframe_type_list[y] == 'click':

                y += 1

                pos_x = int(widget_childs[3].get())
                pos_y = int(widget_childs[5].get())

                z = {y: {'type': 'click', 'position_x': pos_x,
                         'position_y': pos_y, 'duration': 1}}

                self.tasks.update(z)

            elif self.cardframe_type_list[y] == 'sleep':
                y += 1

                type_time = widget_childs[2].get()

                duration = 10

                if type_time == 'seconds':
                    duration = int(widget_childs[1].get())

                elif type_time == 'minutes':
                    duration = int(widget_childs[1].get()) * 60

                elif type_time == 'hours':
                    duration = int(widget_childs[1].get()) * 3600

                z = {y: {'type': 'sleep', 'duration': duration}}

                self.tasks.update(z)

            elif self.cardframe_type_list[y] == 'keyboard':
                y += 1

                text_entry = widget_childs[2].get()

                z = {y: {'type': 'keyboard', 'text': text_entry, 'duration': 0.25}}
                self.tasks.update(z)

        threading.Thread(target=self.interpreter, daemon=True).start()

    def interpreter(self):
        self.status_label.configure(text="Started!")

        interpreter = Interpreter(self.tasks)

        self.status_label.configure(text="Finished")

    def teste(self, event):
        print(self.cardframe_type_list)


if __name__ == "__main__":
    root = Tk()

    app = Application(root)
    root.title('Task Automation')
    root.iconbitmap(f'icons/time.png')
    root.geometry('280x500')
    root.mainloop()
