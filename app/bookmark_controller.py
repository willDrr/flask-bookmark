import json

from .models import Directories


class BookMarkProcessor:

    def __init__(self, file_bookmark: str):
        """
        Takes the file bookmark url as parameter(string), usually localted in
        'C:\\Users\\(USERNAME)\\AppData\\Local\\Google\\Chrome\\User Data
        \\Default'
        """
        self.file_bookmark = file_bookmark

    def get_json_data(self):
        """
        Loads the json file to traverse it later on
        """
        with open(self.file_bookmark, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        return data["roots"]["bookmark_bar"]["children"]

    def process_list_of_childrens(self) -> Directories:
        """
        Process the granchildrens of json object. Since bookmakrs are saved
        under the top level object children their granchildrens are nested
        in form of dictionary when have more granchildrens or list when are
        only children
        """
        list_of_childrens = self.get_json_data()
        lista: Directories = []
        for children in list_of_childrens:
            # top leve if: check if bookmark is dir or plain url
            if 'children' in children:
                for children_ in children["children"]:
                    name = children["name"]
                    content = ""
                    url = ""
                    dirs = True
                    links = True
                    if "children" in children_:
                        content = str(children_["children"])
                    else:
                        content = str(children_)

                    lista.append(Directories(name, url, content, dirs, links))
            else:
                name = children["name"]
                content = str(children)
                url = ""
                dirs = False
                links = True
                lista.append(Directories(name, url, content, dirs, links))

        return lista
