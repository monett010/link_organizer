async function getBookmark(){
    const response = await fetch("http://127.0.0.1:5000/bookmarks/1");
    const json = await response.json();
    return json;
}

// gets every unarchived bookmark
async function getBookmarks(){
    const response = await fetch("http://127.0.0.1:5000/bookmarks/");
    const json = await response.json();
    return json;
}

async function logBookmark(){
    const bookmark = await getBookmark();
    console.log(bookmark);
}

async function writeBookmark(){
    
    const bookmark_data = await getBookmark();

    const bookmark_html = "<div class='bookmark'> <ul><li><a href='bookmark.html'>" + bookmark_data['1']['bookmark_title'] + "</a></li><li><a href='" + bookmark_data['1']['bookmark_url'] + "'>" + bookmark_data['1']['bookmark_url'] + "</a></li> <li>tag | tag | tag</li></ul></div>";
    const bookmark_list_section = document.getElementById("bookmark_list");
    bookmark_list_section.innerHTML = bookmark_html;   
}

// writes unarchived bookmarks to home page
async function writeBookmarks() {
    const bookmarks = await getBookmarks();
    const node = document.getElementById("bookmark_list");

    for (b in bookmarks) {
        const bookmark_html = "<div class='bookmark'> <ul><li><a href='bookmark.html'>" + bookmarks[b]['bookmark_title'] + "</a></li><li><a href='" + bookmarks[b]['bookmark_url'] + "'>" + bookmarks[b]['bookmark_url'] + "</a></li> <li>tag | tag | tag</li></ul></div>";
        node.innerHTML += bookmark_html;
    }
}
