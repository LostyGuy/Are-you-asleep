from app.libraries import *

# Check if folder 'Are-you-asleep' exists

folder_path = r"C:\Are-you-asleep"

if not os.path.exists(folder_path):
    # If not, create the folder
    os.makedirs(folder_path)

# Correct the source path to the app directory
source_path = os.path.join(os.path.dirname(__file__), "app")
# os.path.join() makes a path from two arguments

# Copy the app directory to the target folder
shutil.copytree(source_path, folder_path, dirs_exist_ok=True)
# copytree() copies the folder with it's content to the target folder
# dirs_exist_ok=True allows the copy to overwrite existing directories

# Create a file on startup folder that runs main.py
startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
# getenv() gets the value of an environment variable
# os.path.join() then path.join() make a path from given arguments

startup_file_path = os.path.join(startup_path, 'Are-you-asleep.bat')
main_script_path = os.path.join(folder_path, 'main.py')

with open(startup_file_path, 'w') as f:
    f.write(f'@echo off\n')
    f.write(f'start "{main_script_path}"\n')
    f.write(f'exit\n')
