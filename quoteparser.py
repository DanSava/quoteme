import json as json
if __name__ == '__main__':
    json_export = []
    with open("quotes.txt") as file:
        my_list = file.readlines()
        my_list = [x.strip() for x in my_list]
        for line in my_list:
            # Strip quote
            quote_bi = line.find("\'") + 1
            quote_ei = line.rfind("\'")
            quote = line[quote_bi:quote_ei].strip(" ")

            # Strip author
            bi = line.rfind("\'") + 1
            ei = line.rfind("\"")
            author = line[bi:ei].strip(" ").strip("-")

            if author == "":
                author = "The Internet"
            item = {"Quote": quote, "Author": author}
            json_export.append(item)

    with open('data.json', 'w') as outfile:
        json.dump(json_export, outfile)

