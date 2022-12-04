import json

from .models import Directories
from .models import Bookmark 


class BookMarkProcessor:

    def __init__(self, file_bookmark: str):
        """
        Takes the file bookmark url as parameter(string), usually localted in
        'C:\\Users\\(USERNAME)\\AppData\\Local\\Google\\Chrome\\User Data
        \\Default'
        """
        self.file_bookmark = file_bookmark
        self.allowed_objects = {"type": "url", "type": "folder"}

    def get_json_data(self):
        """
        Loads the json file to traverse it later on
        """
        with open(self.file_bookmark, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        return data["roots"]["bookmark_bar"]["children"]

    # TODO:: make a generic class for this
    def get_names(self, json_array):
        bookmarks: Bookmark = []
        for obj in json_array:
            if isinstance(obj, dict):
                bookmark = Bookmark(obj.get('name'), obj.get('url'))
                bookmarks.append(bookmark)
                # names.append(obj.get('name'))
                children = obj.get('children', None)
                if children:
                    bookmarks.extend(self.get_names(children))
            elif isinstance(obj, list):
                bookmarks.extend(self.get_names(obj))
        return bookmarks

    def process_list_of_childrens(self) -> Directories:
        """
        Process the granchildrens of json object. Since bookmakrs are saved
        under the top level object children their granchildrens are nested
        in form of dictionary when have more granchildrens or list when are
        only children
        """
        list_of_childrens = self.get_json_data()
        directories: Directories = []
        for children in list_of_childrens:
            if children["type"] == "url":
                directories.append(Directories(children["name"], children["url"], "", children["type"], True, True))
            else:
                directories.append(Directories(children["name"], "", "", children["type"], True, True))

        return directories
