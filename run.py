from flask import Flask

app = Flask (__name__)
#to not need to re-launch the server
app.debug = True

@app.route("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.run()
