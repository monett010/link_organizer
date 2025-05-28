async function getBookmark(){
    const response = await fetch("http://127.0.0.1:5000/bookmarks/1");
    const json = await response.json();
    return json;
}
async function logBookmark(){
    const bookmark = await getBookmark();
    console.log(bookmark);
}
