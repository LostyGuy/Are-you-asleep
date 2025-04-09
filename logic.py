from libraries import *
from main import window

class logic():

    def shutdown() -> None:
        log.info("Shutting down the system...")
        os.system("shutdown /s /t 1")

    def what_is_the_time(root) -> object:
        while True:
            current_time = t.localtime()
            log.info(f"Current time: {current_time.tm_year}, {current_time.tm_mday} ,{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}")
            if current_time.tm_hour in range(1,6) or current_time.tm_hour in [23,24]:
                logic.is_the_time_right(current_time)
                window.main_window()
                t.sleep(3600)
            t.sleep(1)
            return current_time
    
    def is_the_time_right(current_time) -> None:
        note_down_time = current_time
        log.info(f"Note down time: {note_down_time.tm_year}, {note_down_time.tm_mday} ,{note_down_time.tm_hour}:{note_down_time.tm_min}:{note_down_time.tm_sec}")

        # Give user ten minutes to take action
        if note_down_time.th_min > 50:
            while True:
                if note_down_time.tm_min + 10 in [0,60]:
                    log.info("Shut down is in progress")
                    logic.shutdown()
                    break
                t.sleep(1)

        else:
            while True:
                if note_down_time.tm_min + 10 == t.localtime().tm_min:
                    log.info("Shut down is in progress")
                    logic.shutdown()
                    break
                t.sleep(1)