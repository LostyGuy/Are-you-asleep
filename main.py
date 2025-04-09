from libraries import *
from logic import time_logic

log.basicConfig(level=log.INFO, filename="app_log")

class window():

    def main_window() -> None:
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("300x200")
        #root.withdraw()

        time_logic.what_is_the_time(root)
        current_time, msbox= time_logic.what_is_the_time(root)
        if msbox:
            messagebox.askokcancel("Quit", "Do you want to leave?")

        root.mainloop()

window.main_window()
