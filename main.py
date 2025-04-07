import os
import sys
import time as t
import tkinter as tk
from tkinter import messagebox
import threading


def shutdown(stop_event, main):
    print("Thread 2 started")

    # Use main thread to show the messagebox
    def ask_user():
        if messagebox.askokcancel("Shutting Down", "The computer will shutdown soon. Are you asleep?"):
            os.system("shutdown /s /t 1")
        else:
            stop_event.set()  # Signal the thread to stop

    main.after(0, ask_user)  # Schedule the messagebox in the main thread

def is_the_time_right(saved_time, stop_event):
    print("Thread 1 started")
    while not stop_event.is_set():  # Check if the stop event is set
        check_time = t.localtime().tm_hour * 60 + t.localtime().tm_min
        if saved_time + 10 < check_time:
            shutdown(stop_event, main)
            break
        t.sleep(1)  # Avoid busy-waiting

def asleep():



    while True:
        current_time = t.localtime()
        print(current_time)
        if current_time.tm_hour >= 21 or current_time.tm_hour < 6:
            saved_time = t.localtime().tm_hour * 60 + t.localtime().tm_min
            stop_event = threading.Event()  # Create a stop event
            task1 = threading.Thread(target=is_the_time_right, args=(saved_time, stop_event))
            task1.start()
            task2 = threading.Thread(target=shutdown, args=(stop_event,main))
            task2.start()
            task1.join()
            task2.join()
            t.sleep(1800)
        else:
            t.sleep(1)

main = tk.Tk()
main.withdraw()

asleep()

main.mainloop()

