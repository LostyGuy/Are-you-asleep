from app.libraries import os, shutil

class Setup:

    def __init__(self):
        self.path_of_copied_app = r"C:\Are-you-asleep"
        self.source_path_of_app =   os.path.join(os.path.dirname(__file__), "app") # os.path.dirname(__file__) get the path to where this file is located
        self.WTS_command = fr'schtasks /create /sc onstart /tn "Are-you-asleep" /tr "pythonw.exe {os.path.join(self.path_of_copied_app, "main.pyw")}"'
    
    def does_folder_exist(self) -> None:
        if not os.path.exists(self.path_of_copied_app):
            shutil.copytree(self.source_path_of_app, self.path_of_copied_app, dirs_exist_ok= True)

    def schedule_task(self) -> None:
        """Creates a Task in Windows Task Schedule that will run main python file supressing the window too"""
        os.system(f"{self.WTS_command}")

def main() -> None:

    setup = Setup()
    setup.does_folder_exist()
    setup.schedule_task()

if __name__ == "__main__":
    main()