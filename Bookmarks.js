class Fetch {

    constructor () {
    // sets the base url for all the fetch operations in these classes
    this.url = "http://127.0.0.1:5000/";
    }
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
                endpoint_url = this.url + "bookmarks/all/"
                break;
            case "archived":
                endpoint_url = this.url + "bookmarks/archived/";
                break;
            default:
                endpoint_url = this.url + "bookmarks/";
            }
        const bookmarks = await this.fetchData(endpoint_url);
        return bookmarks;
    }

    async getBookmarksByTag (tag_id) {
        const endpoint_url = this.url + "bookmarks?tag_id=" + tag_id
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

    writeContextMenu (bookmark_id) {
        const node = document.getElementById(bookmark_id);
        const menu_html = `<nav class='menu' id='menu_${bookmark_id}'>
                    <ul><li><button class='context_menu_btn' aria-label='add_tags'>Add Tags</button></li>
                    <li><button class='context_menu_btn' aria-label='remove_tags'>Remove Tags</button></li>
                    <li><button class='context_menu_btn-archive' id='archive_${bookmark_id}' aria-label='archive_bookmark'>Archive Bookmark</button></li>
                    <li><button class='context_menu_btn' aria-label='delete_bookmark'>Delete Bookmark</button></li>
                    </ul></nav>`;
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

    async archiveBookmark (bookmark_id) {
        const response = await fetch (this.url + 'archive/bookmark/' + bookmark_id);
        const msg = await response.text();
        return msg;
    }

    addEventListenerstoArchiveBtns () {
        let btns = document.getElementsByClassName ("context_menu_btn-archive");

        for (let b=0; b < btns.length; b++) {
            let btn_id = btns[b].id;
            let bookmark_id = btn_id.split("_")[1];
            btns[b].addEventListener("click", (e)=> {
                this.archiveBookmark(bookmark_id);
                window.location.reload();
            })
        }
    }

}


class BookmarkTags extends Bookmarks {

    async getBookmarkTags(bookmark_id){
        const response = await fetch(this.url + "bookmarks/" + bookmark_id + "/tags/")
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
        const tags_ = await this.fetchData (this.url + "tags");
        const node = document.getElementById("tags_menu");


        for (let t in tags_) {
            let url_ = "index.html?tag=" + t;
            node.innerHTML += `<a href='${url_}'>${tags_[t]['tag_name']}</a>`;
        }
    }

}
