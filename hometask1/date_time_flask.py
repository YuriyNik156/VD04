# Задание 1
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main_page():
    time_now = datetime.now()
    current_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Текуще дата и время — {current_time}</h1>"

if __name__ == "__main__":
    app.run()
