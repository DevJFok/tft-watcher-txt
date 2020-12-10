import json

tft_base_item_dict = {}

# Find composition of items
def findCompositionItemsFunction(composition_item_dict, occurance_item_dict):

    for l in occurance_item_dict:
        if l > 9:
            for m in composition_item_dict:
                if l == m:
                    item1 = composition_item_dict[m][0]
                    item2 = composition_item_dict[m][1]
                    for n in tft_base_item_dict:
                        if n == item1:
                            tft_base_item_dict.update({n: tft_base_item_dict[n] + 1})
                        if n == item2:
                            tft_base_item_dict.update({n: tft_base_item_dict[n] + 1})

    return tft_base_item_dict