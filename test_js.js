async function getBookmark(){
    const response = await fetch("http://127.0.0.1:5000/bookmarks/1");
    const json = await response.json();
    return json;
}
async function logBookmark(){
    const bookmark = await getBookmark();
    console.log(bookmark);
}

async function writeBookmark(){
    const bookmark_data = await getBookmark();

    const html = "<div class='bookmark'> <ul><li><a href='bookmark.html'>Title</a></li><li><a href='bookmark.html'>URL</a></li> <li>tag | tag | tag</li></ul></div>"
}
