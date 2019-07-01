from flask import Flask, render_template

app = Flask (__name__)
#to not need to re-launch the server
app.debug = True

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run()
