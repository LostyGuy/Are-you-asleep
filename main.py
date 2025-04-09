from libraries import *
from logic import logic, what_is_the_time

log.basicConfig(level=log.INFO, filename="app_log")

class window():

    def main_window():
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("300x200")
        root.withdraw()

        logic.what_is_the_time()

        root.mainloop()

window.main_window()
