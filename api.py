from flask import Flask, request
from flask_cors import CORS

app = Flask (__name__)
cors = CORS(app)

@app.route ("/")
def hello ():
        return "Hello!"

if __name__ == "__main__":
        app.run(debug=True)