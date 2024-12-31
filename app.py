from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<essay_id>")
def essay(essay_id):
    # check if essay_id exists
    return render_template("template.html")

if __name__ == '__main__':
    app.run(debug=True)