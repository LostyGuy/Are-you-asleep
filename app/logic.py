from libraries import *

class time_logic():

    @staticmethod
    def time_check(root) -> object:
        while True:
            current_time: t.struct_time = t.localtime()
            if current_time.tm_hour in range(0,5) or current_time.tm_hour == 23:
                task1 = Process(target=time_logic.is_the_time_right, args=(current_time,))
                log.info("Thread started")
                task1.start() 
                if not time_logic.mssbox(task1):
                    hour_number: int = 2
                    log.info(f"Clock check suspended for {hour_number} hour")
                    t.sleep(hour_number*3600) # <-- value of intervals between checks
                    log.info("Clock check resumed")
            t.sleep(1)
            
    @staticmethod
    def is_the_time_right(current_time) -> None:
        log.info(f"Countdown beginned on: {current_time.tm_year}, {current_time.tm_mday}, {current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}")

        # Give user ten minutes to take action
        if current_time.tm_min >= 50:
            while True:
                if current_time.tm_min + 10 in range(0,10) or current_time.tm_min + 10 == 60:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)
        else:
            while True:
                if current_time.tm_min + 10 == t.localtime().tm_min:
                    log.info("Shut down is in progress")
                    time_logic.shutdown()
                    break
                t.sleep(1)

    @staticmethod
    def mssbox(task1) -> bool:
        log.info("msbox is called")
        if messagebox.askyesno("Wakey Wakey", "Are you asleep?"):
            time_logic.shutdown()
            return True          
        else:
            log.info("msbox is closed")
            task1.terminate()
            log.info("Thread is terminated")
            return False

    @staticmethod
    def shutdown() -> None:
            log.info("Shutting down the system...")
            os.system("shutdown /s /t 120")