class Bookmarks {

    constructor () {
        
    }
    async method fetchBookmarks (endpoint_url){
        const response = await fetch(endpoint_url);
        const json = await response.json();
        return json;
    }
}