import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*": {"origins": "*"}})
# acess page
# route -> endpoint, path

# function -> o que você quer exibir naquela página


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    pass


# Running the code
if __name__ == "__main__":
    app.run(debug=True)  # All changes in the code are reloaded
