class Fetch {
    async fetchData (endpoint_url){
        const response = await fetch(endpoint_url);
        const json = await response.json();
        return json;
    }
}

class Bookmarks extends Fetch {

    async getBookmarks (tag=0) {
        let endpoint_url = "";
        switch (tag) {
            case "all":
                endpoint_url = "http://127.0.0.1:5000/bookmarks/all/"
                break;
            case "archived":
                endpoint_url = "http://127.0.0.1:5000/bookmarks/archived/";
                break;
            default:
                endpoint_url = "http://127.0.0.1:5000/bookmarks/";
            }
        const bookmarks = await this.fetchData(endpoint_url);
        return bookmarks;
    }

    async getBookmarksByTag (tag_id) {
        const endpoint_url = "http://127.0.0.1:5000/bookmarks?tag_id=" + tag_id
        const bookmarks = await this.fetchData(endpoint_url);
        return bookmarks;
    }



    async writeBookmarks (bookmarks_) {
        let bookmarks = await bookmarks_
        const node = document.getElementById("bookmark_list");
        const tags = new BookmarkTags();

         for (let b in bookmarks) {
            const bookmark_tags = await tags.printTags(b);
            const bookmark_html = "<div class='bookmark' id='" + b + "'> <ul><li><a href='bookmark.html'>" + bookmarks[b]['bookmark_title'] + "</a></li><li><a href='" + bookmarks[b]['bookmark_url'] + "'>" + bookmarks[b]['bookmark_url'] + "</a></li><li>" + bookmark_tags + "</li></ul><div class='dots' id='dots_" + b + "' tabindex='-1'></div></div>";
            node.innerHTML += bookmark_html;
            this.writeContextMenu(b, bookmarks[b]['bookmark_url']);
        }
        
    }

    writeContextMenu (bookmark_id, bookmark_url) {
        const node = document.getElementById(bookmark_id);
        const menu_html = `<nav class='menu' id='menu_${bookmark_id}'>
                            <ul><li><a href=''>Add Tags</a></li>
                            <li><a href=''>Remove Tags</a></li>
                            <li><a href='http://127.0.0.1:5000/archive/bookmark/${bookmark_id}'>Archive Bookmark</a></li>
                            <li><a href=''>Delete Bookmark</a></li></ul></nav>`;
        node.innerHTML += menu_html;
    }

    writeBookmarksList () {
        ////////
        // Gets the tag parameter from the url and displays the appropriate set of bookmarks
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        let tag = urlParams.get('tag')
        
        // If the tag parameter is null, main, or archived, use Bookmarks.getBookmarks()
        if (tag === null || tag === "main") {
            let bookmarks_ = this.getBookmarks()
            this.writeBookmarks(bookmarks_);
        }
        else if (tag === "archived") {
            let bookmarks_ = this.getBookmarks("archived")
            this.writeBookmarks(bookmarks_);
        }
        // If the tag parameter is a tag id, use Bookmarks.getBookmarksByTag() 
        else {
            let bookmarks_ = this.getBookmarksByTag(decodeURIComponent(tag))
            this.writeBookmarks(bookmarks_);
        }
    }

    addEventListenerstoDots() {
        let dots = document.getElementsByClassName("dots");
        let menus = document.getElementsByClassName("menu");


        for (let d=0; d < dots.length; d++) {
            let menu_id = menus[d].id;
            let menu_ = document.getElementById(menu_id);
            dots[d].addEventListener("click", (e)=>{
                if (menu_.style.visibility === "visible") {
                    menu_.style.visibility = "hidden";
                } else {
                    menu_.style.visibility = "visible";
                }
            });
        }
    }

}


class BookmarkTags extends Bookmarks {

    async getBookmarkTags(bookmark_id){
        const response = await fetch("http://127.0.0.1:5000/bookmarks/" + bookmark_id + "/tags/")
        const json = await response.json();
        return json;
    }

    async printTags(bookmark_id) {
        const bookmark_tags = await this.getBookmarkTags (bookmark_id);
        let tags = "";
            for (let t in bookmark_tags){
                tags += bookmark_tags[t]['tag_name'] + " | ";
            }
        return tags.substring(0, tags.length - 3);
    }

}

class Tags extends Fetch {
    async printTagLinks () {
        const tags_ = await this.fetchData ("http://127.0.0.1:5000/tags");
        const node = document.getElementById("tags_menu");


        for (let t in tags_) {
            let url = "index.html?tag=" + t;
            node.innerHTML += "<a href='" + url + "'>" + tags_[t]['tag_name'] + "</a>";
        }
    }

}
