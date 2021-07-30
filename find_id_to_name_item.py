import json

item_list_dict = {}

with open('set4/items.json', 'r') as tft_item_file:
    item_list_dict = tft_item_file.read()

item_list_dict = json.loads(item_list_dict)

def findIdToNameFunction(keyVal, Val):

    for x in range(0,len(item_list_dict)):
        if item_list_dict[x][keyVal] == Val:
            return item_list_dict[x]['name']