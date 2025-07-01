from libraries import *
from logic import time_logic

log_location = os.path.join(os.path.dirname(__file__), "app_log")



log.basicConfig(level=log.INFO, filename=log_location, filemode='a',)

class window():

    def __init__(self) -> None:
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("300x200")
        root.attributes("-topmost", True)
        root.iconify()

        self.start_time = t.localtime()
        

    def main_window(self, root) -> None:

        log.info(f"_______________________________________________________________________________________________________")
        log.info(f"Start time: {self.start_time.tm_year}, {self.start_time.tm_mday} ,{self.start_time.tm_hour}:{self.start_time.tm_min}:{self.start_time.tm_sec}")


        time_logic.time_check(root)
        
        root.mainloop()

if __name__ ==  '__main__':
    window.main_window()