from app.libraries import *

# To where the app will be copied
folder_path = r"C:\Are-you-asleep"

#Folder creation
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# path to app folder that will be copied
source_path = os.path.join(os.path.dirname(__file__), "app")
# os.path.join() makes a path from two arguments

# Copy the app folder to the target folder
shutil.copytree(source_path, folder_path, dirs_exist_ok=True)
# copytree() copies the folder with it's content to the target folder
# dirs_exist_ok=True allows the copy to overwrite existing directories

# Path to the startup folder
startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
# getenv() gets the value of an environment variable
# os.path.join() then path.join() make a path from given arguments

# Create the startup file path
startup_file_path = os.path.join(startup_path, 'Are-you-asleep.vbs')

# Path to run copied script
app_script_path = os.path.join(folder_path, 'main.py')

with open(startup_file_path, 'w') as f:    
    f.write('Set WshShell = CreateObject("WScript.Shell")\n')
    f.write(f'WshShell.Run "pyw ""{app_script_path}""", 0\n')  # Use pyw to suppress the console
    f.write('Set WshShell = Nothing.\n')