from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world(password = None):
    html = """
    <h1>Тестовый запуск локального сервера</h1>
    <p>А это просто текст</p>
    """
    return html

@app.route("/new/")
@app.route("/newpage/")
@app.route("/новаястраница/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()
