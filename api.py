from flask import Flask, request
from flask_cors import CORS
from Controller import SQLStatements

app = Flask (__name__)
cors = CORS(app)

s = SQLStatements()

@app.route ("/")
def hello ():
        return "Hello!"

# gets all regular (unarchived) bookmarks
@app.get ("/bookmarks/")
def getBookmarks ():
        return s.getBookmarks("u")

# gets (unarchived) bookmarks with a certain tag
@app.get ("/bookmarks")
def getBookmarksWithTag ():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id)

@app.get ("/bookmarks/<id>")
def getBookmarkbyId (id):
        return s.getBookmark(id)

@app.get ("/bookmarks/archived/")
def getArchivedBookmarks ():
        return s.getBookmarks("a")

@app.get ("/bookmarks/archived")
def getArchivedBookmarksWithTag ():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id,"a")

# gets all bookmarks, archived and unarchived
@app.get ("/bookmarks/all/")
def getAllBookmarks ():
        return s.getBookmarks("all")

@app.get ("/bookmarks/all")
def getAllBookmarksWithTag():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id,"all")

@app.get ("/tags")
def getTags ():
        return s.getTags()

@app.get ("/tags/<id>")
def getTag(id):
        return s.getTag(id)

@app.post ("/add/bookmark")
# not sure how this will work yet

@app.post ("/add/tag")
def addTag():
        # tag_name = request.form['tag_name']
        tag_name = request.get_json()['tag_name']
        s.addTag(tag_name)
        return "Successfully added tag."

if __name__ == "__main__":
        app.run(debug=True)