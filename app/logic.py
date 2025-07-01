from libraries import *

class time_logic():

    def __init__(self) -> None:
        self.current_time = t.localtime()
    
    def time_check(self, root) -> object:
        while True:
            if self.current_time.tm_hour in range(0,5) or self.current_time.tm_hour == 23:
                task1 = Process(target=time_logic.is_the_time_right, args=(self.current_time,))
                log.info("Thread started")
                task1.start() 
                if not time_logic.mssbox(task1):
                    hour_number: int = 2
                    log.info(f"Clock check suspended for {hour_number} hour")
                    t.sleep(hour_number*3600) # <-- value of intervals between checks
                    log.info("Clock check resumed")
            t.sleep(1)
            
    def is_the_time_right(self) -> None:
        log.info(f"Countdown beginned on: {self.current_time.tm_year}, {self.current_time.tm_mday}, {self.current_time.tm_hour}:{self.current_time.tm_min}:{self.current_time.tm_sec}")

        # Give user ten minutes to take action
        if self.current_time.tm_min >= 50:
            while True:
                if self.current_time.tm_min + 10 in range(0,10) or self.current_time.tm_min + 10 == 60:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)
        else:
            while True:
                if self.current_time.tm_min + 10 == t.localtime().tm_min:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)

    def mssbox(task1) -> None:
        log.info("msbox is called")
        if messagebox.askyesno("Wakey Wakey", "Are you asleep?"):
            time_logic.shutdown()            
        else:
            log.info("msbox is closed")
            task1.terminate()
            log.info("Thread is terminated") 

    def shutdown() -> None:
            log.info("Shutting down the system...")
            os.system("shutdown /s /t 120")