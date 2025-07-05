from libraries import *
from logic import time_logic

log_location = os.path.join(os.path.dirname(__file__), "app_log")



log.basicConfig(level=log.INFO, filename=log_location, filemode='a',)

class window():

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("300x200")
        self.root.attributes("-topmost", True)
        self.root.iconify()

        self.start_time = t.localtime()
        

    def main_window(self) -> None:

        log.info(f"_______________________________________________________________________________________________________")
        log.info(f"Start time: {self.start_time.tm_year}, {self.start_time.tm_mday} ,{self.start_time.tm_hour}:{self.start_time.tm_min}:{self.start_time.tm_sec}")


        time_logic.time_check(self.root)
        
        self.root.mainloop()

if __name__ ==  '__main__':
    win = window()
    win.main_window()