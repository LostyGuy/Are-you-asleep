from libraries import *
from logic import time_logic

log_location = os.path.join(os.path.dirname(__file__), "app_log")



log.basicConfig(level=log.INFO, filename=log_location, filemode='a',)

class window():

    def main_window() -> None:
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("300x200")
        root.attributes("-topmost", True)
        root.iconify()

        start_time = t.localtime()
        log.info(f"_______________________________________________________________________________________________________")
        log.info(f"Start time: {start_time.tm_year}, {start_time.tm_mday} ,{start_time.tm_hour}:{start_time.tm_min}:{start_time.tm_sec}")


        time_logic.what_is_the_time(root)
        
        root.mainloop()

if __name__ ==  '__main__':
    window.main_window()