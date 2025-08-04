from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/start-gesture')
def start_gesture_control():
    try:
        subprocess.Popen(["python", "gesture_recognition.py"])
        return "Gesture Control Started!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
