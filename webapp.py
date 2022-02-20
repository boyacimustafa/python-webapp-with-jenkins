from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")