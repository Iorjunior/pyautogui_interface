import pyautogui
import time

task = {
    1: {'type': 'click', 'position_x': 500, 'position_y': 400, 'duration': 1},
    2: {'type': 'sleep', 'duration': 10},
    3: {'type': 'keyboard', 'text': 'Hello, Word!!', 'duration': 10},

}


class Interpreter():
    def __init__(self, automation):

        for task_id, task in automation.items():

            print(task_id)

            if task['type'] == 'click':

                self.mouse_click(task['position_x'],
                                 task['position_y'], task['duration'])

            elif task['type'] == 'sleep':

                self.sleep_cycle(task['duration'])

            elif task['type'] == 'keyboard':
                self.keyboard_writer(task['text'], task['duration'])

    def mouse_click(self, position_x, position_y, duration):
        pyautogui.click(position_x, position_y, duration=duration)

    def sleep_cycle(self, duration):
        time.sleep(duration)

    def keyboard_writer(self, text, duration):
        pyautogui.write(str(text), interval=duration)
