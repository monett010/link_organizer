from flask import Flask, request
from flask_cors import CORS
from Controller import SQLStatements
from Scraper import Scraper
import time
from datetime import date

app = Flask (__name__)
cors = CORS(app)

s = SQLStatements()


@app.route ("/")
def hello ():
        return "Hello!"

# =======
# GET
# =======

# gets all regular (unarchived) bookmarks
@app.get ("/bookmarks/")
def getBookmarks ():
        return s.getBookmarks("u")

# gets (unarchived) bookmarks with a certain tag
@app.get ("/bookmarks")
def getBookmarksWithTag ():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id)

# Gets a bookmark by its id
@app.get ("/bookmarks/<id>")
def getBookmarkbyId (id):
        return s.getBookmark(id)

# Gets all archived bookmarks
@app.get ("/bookmarks/archived/")
def getArchivedBookmarks ():
        return s.getBookmarks("a")

# Gets all archived bookmarks that have been tagged with a certain tag
@app.get ("/bookmarks/archived")
def getArchivedBookmarksWithTag ():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id,"a")

# gets all bookmarks, archived and unarchived
@app.get ("/bookmarks/all/")
def getAllBookmarks ():
        return s.getBookmarks("all")

# Gets all bookmarks, archived and unarchived, that have been tagged with a certain tag
@app.get ("/bookmarks/all")
def getAllBookmarksWithTag():
        tag_id = request.args.get("tag_id")
        return s.getBookmarksWithTag(tag_id,"all")

# Gets all tags
@app.get ("/tags")
def getTags ():
        return s.getTags()

# Gets a tag by its id
@app.get ("/tags/<id>")
def getTag(id):
        return s.getTag(id)


# @app.post ("/bookmark/info")
# def scrapeURLInfo ():
#         url = request.form['url']
#         scraper = Scraper(url)
#         title = scraper.getTitle()
#         today = date.today()
#         date_added = today.isoformat()
#         return {'bookmark_title': title, 'bookmark_url': url, 'date_added': date_added}

# ======
# ADD
# ======

# Adds a bookmark
@app.post ("/add/bookmark")
def addBookmark():
        bookmark_title = request.get_json()['bookmark_title']
        bookmark_url = request.get_json()['bookmark_url']
        date_added = request.get_json()['date_added']
        params = {'bookmark_title':bookmark_title, 'bookmark_url': bookmark_url, 'date_added': date_added}
        s.addBookmark(params)
        return "Successfully added bookmark."

# Adds a tag
@app.post ("/add/tag")
def addTag():
        # tag_name = request.form['tag_name']
        tag_name = request.get_json()['tag_name']
        s.addTag(tag_name)
        return "Successfully added tag."

if __name__ == "__main__":
        app.run(debug=True)