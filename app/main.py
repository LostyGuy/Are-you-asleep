from libraries import *
from logic import time_logic

log.basicConfig(level=log.INFO, filename="app_log")

class window():

    def main_window() -> None:
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("300x200")
        root.attributes("-topmost", True)
        root.iconify()

        time_logic.what_is_the_time(root)

        root.mainloop()

if __name__ ==  '__main__':
    window.main_window()