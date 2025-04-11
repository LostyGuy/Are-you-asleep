from app.libraries import *

# Check if folder 'Are-you-asleep' exists
folder_path = r"C:\Are-you-asleep"

if not os.path.exists(folder_path):
    # If not, create the folder
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created.")

# Copy app content to 'Are-you-asleep'


# Create a file on startup folder that runs main.py

with open(startup_file, "w") as f:
    f.write(f'python "{os.path.join(folder_path, "main.py")}"\n')

print(f"Startup file created at '{startup_file}'.")