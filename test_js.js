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

async function getBookmarksByTag(tag_id){
    const response = await fetch("http://127.0.0.1:5000/bookmarks?tag_id=" + tag_id);
    const json = await response.json();
    return json;
}

async function getArchivedBookmarks() {
    const response = await fetch("http://127.0.0.1:5000/bookmarks/archived/");
    const json = await response.json();
    return json;
}

async function getBookmarkTags(bookmark_id){
    const response = await fetch("http://127.0.0.1:5000/bookmarks/" + bookmark_id + "/tags/")
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

async function printTags(bookmark_id) {
    const bookmark_tags = await getBookmarkTags (bookmark_id);
    let tags = "";
    for (t in bookmark_tags){
        tags += bookmark_tags[t]['tag_name'] + " | ";
    }
    return tags.substring(0, tags.length - 3);
}

// writes unarchived bookmarks to home page
async function writeBookmarks() {
    const bookmarks = await getBookmarks();
    const node = document.getElementById("bookmark_list");
    // const bookmark_tags = await printTags();

    for (b in bookmarks) {
        const bookmark_tags = await printTags(b);
        const bookmark_html = "<div class='bookmark' id='" + b + "'> <ul><li><a href='bookmark.html'>" + bookmarks[b]['bookmark_title'] + "</a></li><li><a href='" + bookmarks[b]['bookmark_url'] + "'>" + bookmarks[b]['bookmark_url'] + "</a></li><li>" + bookmark_tags + "</li></ul></div>";
        node.innerHTML += bookmark_html;
    }
}

async function writeArchivedBookmarks() {
    const bookmarks = await getArchivedBookmarks();
    const node = document.getElementById("bookmark_list");

    for (b in bookmarks) {
        const bookmark_tags = await printTags(b);
        const bookmark_html = "<div class='bookmark' id='" + b + "'> <ul><li><a href='bookmark.html'>" + bookmarks[b]['bookmark_title'] + "</a></li><li><a href='" + bookmarks[b]['bookmark_url'] + "'>" + bookmarks[b]['bookmark_url'] + "</a></li><li>" + bookmark_tags + "</li></ul></div>";
        node.innerHTML += bookmark_html;
    }
}

async function writeBookmarksWithTag(tag_id) {
    const bookmarks = await getBookmarksByTag(tag_id);
    const node = document.getElementById("bookmark_list");

    for (b in bookmarks) {
        const bookmark_tags = await printTags(b);
        const bookmark_html = "<div class='bookmark' id='" + b + "'> <ul><li><a href='bookmark.html'>" + bookmarks[b]['bookmark_title'] + "</a></li><li><a href='" + bookmarks[b]['bookmark_url'] + "'>" + bookmarks[b]['bookmark_url'] + "</a></li><li>" + bookmark_tags + "</li></ul></div>";
        node.innerHTML += bookmark_html;
    }

}