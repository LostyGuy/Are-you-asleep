from app.libraries import os

class Setup:

    def __init__(self):
        self.path_of_copied_app = r"C:\Are-you-asleep"
        self.source_path_of_app =   os.path.join(os.path.dirname(__file__), "app") # os.path.dirname(__file__) get the path to where this file is located
        self.startup_system_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        self.ps1_file =  os.path.join(self.path_of_copied_app, 'Are-you-asleep.ps1') # Creates blank ps1 file
        self.vbs_file = os.path.join(self.startup_system_folder, 'Are-you-asleep.vbs') # Creates blank vbs file to launch ps1 file
        self.file_to_run_by_ps1 = os.path.join(self.path_of_copied_app, 'main.pyw') # The heart of app
    
    def does_folder_exist(self) -> None:
        if not os.path.exists(self.path_of_copied_app):
            os.makedirs(self.path_of_copied_app)

    def create_file_content_vbs(self) -> None:
        """Creates a VBS file"""
        with open(self.vbs_file, 'w') as f:    
            f.write('Set objShell = CreateObject("Wscript.Shell")\n')
            f.write(f'objShell.Run "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File ""{self.ps1_file}""", 0\n')
    
    def create_file_content_ps1(self) -> None:
        """Creates a ps1 file"""
        with open(self.ps1_file, 'w') as f:    
            f.write(f'$pythonw = "pythonw.exe"\n')
            f.write('$scriptPath = "C:\Are-you-asleep\main.pyw"\n')
            f.write('Start-Process -FilePath $pythonw -ArgumentList "$scriptPath"\n')

def main() -> None:

    setup = Setup()
    setup.does_folder_exist()
    setup.create_file_content_vbs()
    setup.create_file_content_ps1()

if __name__ == "__main__":
    main()