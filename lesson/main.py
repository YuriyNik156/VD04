from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chessmans(password = None):
    return render_template("hometask_cards.html")

@app.route("/sportsmans/")
def sportsmans(password = None):
    return render_template("practice.html")

@app.route("/new/")
@app.route("/newpage/")
@app.route("/новаястраница/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()
