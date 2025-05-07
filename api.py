from flask import Flask, request
from flask_cors import CORS
from Controller import SQLStatements

app = Flask (__name__)
cors = CORS(app)

s = SQLStatements()

@app.route ("/")
def hello ():
        return "Hello!"

@app.get ("/get/bookmarks")
def getBookmarks ():
        return s.getBookmarks("all")


@app.get ("/get/bookmarks/<id>")
def getBookmarkbyId (id):
        return s.getBookmark(id)

@app.get ("/get/tags")
def getTags ():
        return s.getTags()

@app.get ("/get/tags/<id>")
def getTag(id):
        return s.getTag(id)        

if __name__ == "__main__":
        app.run(debug=True)