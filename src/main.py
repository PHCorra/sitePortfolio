from flask import Flask, render_template

app = Flask(__name__)

# acess page
# route -> endpoint, path

# function -> o que você quer exibir naquela página


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Running the code
if __name__ == "__main__":
    app.run(debug=True)  # All changes in the code are reloaded
