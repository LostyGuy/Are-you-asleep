from libraries import *

class time_logic():

    
    def what_is_the_time(root) -> object:
        while True:
            current_time = t.localtime()
            if current_time.tm_hour in range(0,5) or current_time.tm_hour == 23:
                task1 = Process(target=time_logic.is_the_time_right, args=(current_time,))
                log.info("Thread started")
                task1.start()
                if not time_logic.mssbox(task1):
                    log.info("Clock check suspended for 1 hour")
                    t.sleep(3600)
                    log.info("Clock check resumed")
            t.sleep(1)
            
    def is_the_time_right(current_time) -> None:
        note_down_time = current_time
        log.info(f"Countdown beginned on: {note_down_time.tm_year}, {note_down_time.tm_mday}, {note_down_time.tm_hour}:{note_down_time.tm_min}:{note_down_time.tm_sec}")

        # Give user ten minutes to take action
        if note_down_time.tm_min >= 50:
            while True:
                if note_down_time.tm_min + 10 in range(0,10) or note_down_time.tm_min + 10 == 60:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)
        else:
            while True:
                if note_down_time.tm_min + 10 == t.localtime().tm_min:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)

    def mssbox(task1) -> None:
        log.info("msbox is called")
        if messagebox.askokcancel("Wakey Wakey", "Are you asleep?"):
            time_logic.shutdown()            
        else:
            log.info("msbox is closed")
            task1.terminate()
            log.info("Thread is terminated")

    def shutdown() -> None:
            log.info("Shutting down the system...")
            os.system("shutdown /s /t 1")