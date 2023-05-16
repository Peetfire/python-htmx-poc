from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

# assets = Environment(app)
# css = Bundle("src/main.css", output="dist/main.css")

# assets.register("css", css)
# css.build()

# Sets base root to index.html
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()