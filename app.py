import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
VIDEO_FOLDER = 'videos'

os.makedirs(VIDEO_FOLDER, exist_ok=True)

# أشهر 5 امتدادات هندعمهم في الموقع
ALLOWED_EXTENSIONS = ('.mp4', '.mkv', '.webm', '.avi', '.mov')

@app.route('/')
def index():
    # بنجيب أسماء الملفات اللي بتنتهي بأي امتداد من القايمة اللي فوق (ومحولين الحروف لـ small عشان لو الامتداد مكتوب كابيتال)
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(ALLOWED_EXTENSIONS)]
    return render_template('index.html', videos=videos)

@app.route('/video/<filename>')
def video(filename):
    # إرسال الفيديو مع دعم التقديم والتأخير
    return send_from_directory(VIDEO_FOLDER, filename, conditional=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
