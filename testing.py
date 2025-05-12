from Controller import Connection, SQLStatements

s = SQLStatements()

# TESTING GET BOOKMARKS
# print (s.getBookmarks("u"))
# print(s.getBookmark(1))

# TESTING GET TAGS
# print (s.getTags())

#TESTING ADDING BOOKMARK

# bookmark_title = "How To Define A Function With Optional Arguments?"
# bookmark_url = "https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments"
# date_added = "2025-05-06"

# s.addBookmark ((bookmark_title, bookmark_url, date_added,))

# TESTING ADDING BOOKMARK V2
# params = {'bookmark_title':'How To Define A Function With Optional Arguments?', 'bookmark_url':'https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments', 'date_added':'2025-05-07'}

# s.addBookmark (params)

# TESTING ADDING TAG
# s.addTag ("documentation still rules")

# TESTING ADDING TAG TO BOOKMARK
# s.addTagToBookmark ("6","3")

# TESTING REMOVE BOOKMARK
# s.removeBookmark(7)

# TESTING REMOVE TAG FROM BOOKMARK
# s.removeTagFromBookmark(3, 1)

# TESTING REMOVE TAG
# s.removeTagFromBookmark(2, 4)
# s.removeTag(2)

# s.addTag("rip private equity")
# s.addTagToBookmark(4, 5)

# TESTING GET BOOKMARKS WITH TAG
print(s.getBookmarksWithTag(1, "u"))