import sqlite3

class Connection ():

    def __init__(self):
        self.db = "Bookmarks.db"

    def sql_get (self, sql_statement):
        connection_ = sqlite3.connect(self.db)
        cursor = connection_.cursor()
        rows_ = cursor.execute(sql_statement)
        rows = rows_.fetchall()
        cursor.close()
        connection_.close()
        return rows

    def sql_insert (self, sql_statement, params):
        connection_ = sqlite3.connect(self.db)
        cursor = connection_.cursor()
        cursor.execute(sql_statement, params)
        connection_.commit()
        cursor.close()
        connection_.close()

    def sql_delete (self, sql_statement, params):
        connection_ = sqlite3.connect(self.db)
        cursor = connection_.cursor()
        cursor.execute(sql_statement, params)
        connection_.commit()
        cursor.close()
        connection_.close()



class SQLStatements (Connection) :

    # GET
    def getBookmarks (self, opt:str) -> dict:
        match opt:
            case "all":
                sql_statement = "SELECT * FROM Bookmarks;"
            case "u":
                sql_statement = "SELECT * FROM Bookmarks WHERE archived='N';"
            case "a":
                sql_statement = "SELECT * FROM Bookmarks WHERE archived='Y';"

        bookmarks = Connection.sql_get(self, sql_statement)
        return bookmarks

    def getTags (self) -> dict:
        sql_statement = "SELECT * FROM Tags;"
        tags = Connection.sql_get(self, sql_statement)
        return tags
    
    # INSERT

    def addBookmark (self, params_:dict) -> None:
        sql_statement = "INSERT INTO Bookmarks (bookmark_title,bookmark_url,date_added) VALUES (?,?,?);"
        params = (params_['bookmark_title'], params_['bookmark_url'], params_['date_added'],)
        Connection.sql_insert(self, sql_statement, params)

    def addTag (self, tag_name:str) -> None:
        sql_statement = "INSERT INTO Tags (tag_name) VALUES (?);"
        Connection.sql_insert(self, sql_statement, (tag_name,))

    def addTagToBookmark (self, params_:dict) -> None:
        sql_statement = "INSERT INTO Bookmark_tags (bookmark_id, tag_id) VALUES (?,?);"
        params = (params_['bookmark_id'], params_['tag_id'],)
        Connection.sql_insert(self, sql_statement, params)

    # DELETE
    def removeBookmark (self, bookmark_id:int) -> None:
        sql_statement = "DELETE FROM Bookmarks WHERE bookmark_id = ?;"
        Connection.sql_delete(self, sql_statement, (bookmark_id,))

    def removeTag (self, tag_id:int) -> None:
        sql_statement = "DELETE FROM Tags WHERE tag_id = ?;"
        Connection.sql_delete(self, sql_statement, (tag_id,))
    

    def removeTagFromBookmark (self, params_) -> None:
        sql_statement = "DELETE FROM Bookmark_tags WHERE tag_id = ? AND bookmark_id = ?;"
        params = (params_['tag_id'],params_['bookmark_id'],)
        Connection.sql_delete(self,sql_statement, params)