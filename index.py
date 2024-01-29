import shutil
import os
import subprocess
def deleteDriver():
    directory = 'dist'  # Replace with the directory path you want to delete
    if os.path.exists(directory):
        
        shutil.rmtree(directory)
        print(f"The directory '{directory}' has been deleted.")
    else:
        print(f"The directory '{directory}' does not exist.")
    directory = 'build'  # Replace with the directory path you want to delete
    if os.path.exists(directory):
        
        shutil.rmtree(directory)
        print(f"The directory '{directory}' has been deleted.")
    else:
        print(f"The directory '{directory}' does not exist.")
subprocess.call("TASKKILL /f /IM CHROMEDRIVER.EXE")
    
# deleteDriver()