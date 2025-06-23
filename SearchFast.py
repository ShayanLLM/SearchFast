import subprocess
import threading

def run_gui():
    subprocess.Popen(["python", "file_search_gui.py"])

def run_other():
    subprocess.Popen(["python", "local_search.py"])

threading.Thread(target=run_gui).start()
threading.Thread(target=run_other).start()
