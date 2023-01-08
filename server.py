from flask import Flask 
from home.home import home


app = Flask(__name__)
app.register_blueprint(home)

@app.route("/")
def home():
    return {"Message": "Hello World!"}


if __name__ == "__main__":
    app.run(debug=True)