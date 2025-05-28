import sqlite3

class Connection ():

    def __init__(self):
        self.db = "Bookmarks.db"
    
    def sql_fetch (self, sql_statement, id=0):
        connection_ = sqlite3.connect(self.db)
        cursor = connection_.cursor()

        if (id != 0):
            rows_ = cursor.execute(sql_statement, id)
        else:
            rows_ = cursor.execute(sql_statement)

        rows = rows_.fetchall()
        cursor.close()
        connection_.close()
        return rows

    def sql_commit (self, sql_statement, params):
        connection_ = sqlite3.connect(self.db)
        cursor = connection_.cursor()
        cursor.execute(sql_statement, params)
        connection_.commit()
        cursor.close()
        connection_.close()



class SQLStatements (Connection) :

    # GET
    def getBookmark (self, bookmark_id:int) -> dict:
        sql_statement = "SELECT * FROM Bookmarks WHERE bookmark_id=?;"
        bookmark_ = Connection.sql_fetch(self, sql_statement, (bookmark_id,))
        bookmark = dict()

        for b in bookmark_:
            keys = ["bookmark_id","bookmark_title","bookmark_url","date_added","archived","date_archived"]
            values = [b[0], b[1], b[2], b[3], b[4], b[5]]
            bmk = dict(zip(keys, values))
            bookmark[b[0]] = bmk
        return bookmark

    def getBookmarks (self, opt:str) -> dict:
        match opt:
            case "all":
                sql_statement = "SELECT * FROM Bookmarks;"
            case "u":
                sql_statement = "SELECT * FROM Bookmarks WHERE archived='N';"
            case "a":
                sql_statement = "SELECT * FROM Bookmarks WHERE archived='Y';"

        bookmarks_ = Connection.sql_fetch(self, sql_statement)
        bookmarks = dict()

        for b in bookmarks_:
            keys = ["bookmark_id","bookmark_title","bookmark_url","date_added","archived","date_archived"]
            values = [b[0], b[1], b[2], b[3], b[4], b[5]]
            bookmark = dict(zip(keys, values))
            bookmarks[b[0]] = bookmark
        return bookmarks
    
    def getBookmarksWithTag (self, tag_id:int, opt=0):
        match opt:
            case 0:
                sql_statement = "SELECT Bookmarks.bookmark_id AS bookmark_id, Bookmarks.bookmark_url AS url, Bookmarks.bookmark_title AS title FROM Bookmark_tags INNER JOIN Bookmarks ON Bookmarks.bookmark_id = Bookmark_tags.bookmark_id AND Bookmark_tags.tag_id = ? AND Bookmarks.archived='N';"
            case "a":
                sql_statement = "SELECT Bookmarks.bookmark_id AS bookmark_id, Bookmarks.bookmark_url AS url, Bookmarks.bookmark_title AS title FROM Bookmark_tags INNER JOIN Bookmarks ON Bookmarks.bookmark_id = Bookmark_tags.bookmark_id AND Bookmark_tags.tag_id = ? AND Bookmarks.archived='Y';"
            case "all":
                sql_statement = "SELECT Bookmarks.bookmark_id AS bookmark_id, Bookmarks.bookmark_url AS url, Bookmarks.bookmark_title AS title FROM Bookmark_tags INNER JOIN Bookmarks ON Bookmarks.bookmark_id = Bookmark_tags.bookmark_id AND Bookmark_tags.tag_id = ?;"

        bookmarks_ = Connection.sql_fetch(self, sql_statement, (tag_id,))
        bookmarks = dict()
    
        for b in bookmarks_:
            keys = ["bookmark_id", "bookmark_url", "bookmark_title"]
            values = [b[0], b[1], b[2]]
            bookmark = dict(zip(keys, values))
            bookmarks[b[0]] = bookmark
        return bookmarks



    def getTag (self, tag_id:int) -> dict:
        sql_statement = "SELECT * FROM Tags WHERE tag_id=?;"
        tag = Connection.sql_fetch(self, sql_statement, (tag_id,))
        return tag

    def getTags (self) -> dict:
        sql_statement = "SELECT * FROM Tags;"
        tags_ = Connection.sql_fetch(self, sql_statement)

        tags = dict()

        for t in tags_:
            keys = ["tag_id", "tag_name"]
            values = [t[0], t[1]]
            tag = dict(zip(keys, values))
            tags[t[0]] = tag

        return tags
    
    # INSERT

    def addBookmark (self, params_:dict) -> None:
        sql_statement = "INSERT INTO Bookmarks (bookmark_title,bookmark_url,date_added) VALUES (?,?,?);"
        params = (params_['bookmark_title'], params_['bookmark_url'], params_['date_added'],)
        Connection.sql_commit(self, sql_statement, params)

    def addTag (self, tag_name:str) -> None:
        sql_statement = "INSERT INTO Tags (tag_name) VALUES (?);"
        Connection.sql_commit(self, sql_statement, (tag_name,))

    def addTagToBookmark (self, params_:dict) -> None:
        sql_statement = "INSERT INTO Bookmark_tags (bookmark_id, tag_id) VALUES (?,?);"
        params = (params_['bookmark_id'], params_['tag_id'],)
        Connection.sql_commit(self, sql_statement, params)

    # DELETE
    def removeBookmark (self, bookmark_id:int) -> None:
        sql_statement = "DELETE FROM Bookmarks WHERE bookmark_id = ?;"
        Connection.sql_commit(self, sql_statement, (bookmark_id,))

    def removeTag (self, tag_id:int) -> None:
        sql_statement = "DELETE FROM Tags WHERE tag_id = ?;"
        Connection.sql_commit(self, sql_statement, (tag_id,))
    

    def removeTagFromBookmark (self, params_) -> None:
        sql_statement = "DELETE FROM Bookmark_tags WHERE tag_id = ? AND bookmark_id = ?;"
        params = (params_['tag_id'],params_['bookmark_id'],)
        Connection.sql_commit(self,sql_statement, params)