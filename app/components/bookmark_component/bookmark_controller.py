import json


class BookMarkProcessor:

    def get_json_data():
        FILE_BOOKMARK = "c:\\users\\personal\\desktop\\python-bookmark\\app\\" \
                "static\\Bookmarks.json"
        with open(FILE_BOOKMARK, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        return data["roots"]["bookmark_bar"]["children"]


    def process_list_of_childrens(filebook, list_of_childrens):
        LONG_LINE = "\n------------------------------------------------------------------------------------------------------------------------\n"
        lista = []
        for children in list_of_childrens:
            lista.append(str(children["name"]))
            if 'children' in children:
                for children_ in children["children"]:
                    if "children" in children_:
                        lista.append(str(children_["name"]))
                        lista.append(str(children_["children"]))
                    else:
                        lista.append(str(children_))
            else:
                print(children)
                lista.append(children)
            print(LONG_LINE)
            lista.append(LONG_LINE)




