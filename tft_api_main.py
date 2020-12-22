from riotwatcher import TftWatcher, ApiError
from collections import OrderedDict
import pandas as pd
import json
from findCompositionItems import *
from findTopThree import *
from findIdToName_item import *
from orderingDictDescending import *
from orderingDictAscending import *
from orderingListAscending import *
from findBottomThree import *

# from apiFunction import (findCompositionItems, findTopThree, findIdToName_item, orderingDict)

# golbal variables
api_key = 'enter-your-api-key'
my_tft_server = ''
my_tft_region = ''
my_match_history_count = 10

# Assume valid Summoner Name
user_input_summonerName = input("Enter Summoner Name: ")
# Assume valid server
user_input_server = input("Please enter your server: ")
user_input_server = user_input_server.lower()
if user_input_server == 'na1':
    my_tft_server = user_input_server
    my_tft_region = 'americas'
elif user_input_server == 'euw1' or user_input_server == 'eun1':
    my_tft_server = user_input_server
    my_tft_region = 'europe'
elif user_input_server == 'kr' or user_input_server == 'jp1':
    my_tft_server = user_input_server
    my_tft_region = 'asia'
# Assume valid integer > 0
user_input_match_history_count = int(input("Enter Match History count: "))
my_match_history_count = user_input_match_history_count
# Output file
user_input_summonerName_server_filename = user_input_summonerName + '_' + user_input_server + '_tft_file.txt'

#TFT global variables
tft_watcher = TftWatcher(api_key)
my_tft = tft_watcher.summoner.by_name(my_tft_server, user_input_summonerName)
my_tft_rank = tft_watcher.league.by_summoner(my_tft_server, my_tft['id'])
my_tft_matches = tft_watcher.match.by_puuid(my_tft_region, my_tft["puuid"], my_match_history_count)

tft_trait_dict = {
    'Boss': 0,
    'Cultist': 0,
    'Divine': 0,
    'Duelist': 0,
    'Dusk': 0,
    'Emperor': 0,
    'Fortune': 0,
    'Hunter': 0,
    'Keeper': 0,
    'Moonlight': 0,
    'Sharpshooter': 0,
    'Warlord': 0,
    'Set4_Adept': 0,
    'Set4_Assassin': 0,
    'Set4_Brawler': 0,
    'Set4_Dazzler': 0,
    'Set4_Elderwood': 0,
    'Set4_Enlightened': 0,
    'Set4_Exile': 0,
    'Set4_Mage': 0,
    'Set4_Mystic': 0,
    'Set4_Ninja': 0,
    'Set4_Shade': 0,
    'Set4_Spirit': 0,
    'Set4_Tormented': 0,
    'Set4_Vanguard': 0

    }
tft_solo_trait_dict = {
    'Boss': 0,
    'Emperor': 0,
    'Set4_Tormented': 0

    }
tft_character_dict = {
    'TFT4_Aatrox': 0,
    'TFT4_Ahri': 0,
    'TFT4_Akali': 0,
    'TFT4_Annie': 0,
    'TFT4_Aphelios': 0,
    'TFT4_Ashe': 0,
    'TFT4_Azir': 0,
    'TFT4_Cassiopeia': 0,
    'TFT4_Diana': 0,
    'TFT4_Elise': 0,
    'TFT4_Evelynn': 0,
    'TFT4_Ezreal': 0,
    'TFT4_Fiora': 0,
    'TFT4_Garen': 0,
    'TFT4_Hecarim': 0,
    'TFT4_Irelia': 0,
    'TFT4_Janna': 0,
    'TFT4_JarvanIV': 0,
    'TFT4_Jax': 0,
    'TFT4_Jhin': 0,
    'TFT4_Jinx': 0,
    'TFT4_Kalista': 0,
    'TFT4_Katarina': 0,
    'TFT4_Kayn': 0,
    'TFT4_Kennen': 0,
    'TFT4_Kindred': 0,
    'TFT4_LeeSin': 0,
    'TFT4_Lillia': 0,
    'TFT4_Lissandra': 0,
    'TFT4_Lulu': 0,
    'TFT4_Lux': 0,
    'TFT4_Maokai': 0,
    'TFT4_Morgana': 0,
    'TFT4_Nami': 0,
    'TFT4_Nidalee': 0,
    'TFT4_Nunu': 0,
    'TFT4_Pyke': 0,
    'TFT4_Riven': 0,
    'TFT4_Sejuani': 0,
    'TFT4_Sett': 0,
    'TFT4_Shen': 0,
    'TFT4_Sylas': 0,
    'TFT4_TahmKench': 0,
    'TFT4_Talon': 0,
    'TFT4_Teemo': 0,
    'TFT4_Thresh': 0,
    'TFT4_TwistedFate': 0,
    'TFT4_Vayne': 0,
    'TFT4_Veigar': 0,
    'TFT4_Vi': 0,
    'TFT4_Warwick': 0,
    'TFT4_Wukong': 0,
    'TFT4_XinZhao': 0,
    'TFT4_Yasuo': 0,
    'TFT4_Yone': 0,
    'TFT4_Yuumi': 0,
    'TFT4_Zed': 0,
    'TFT4_Zilean': 0
    }
tft_base_item_dict = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0
    }
tft_composition_item_dict = {
    11 : [1, 1],
    12 : [1, 2],
    13 : [1, 3],
    14 : [1, 4],
    15 : [1, 5],
    16 : [1, 6],
    17 : [1, 7],
    18 : [1, 8],
    19 : [1, 9],
    22 : [2, 2],
    23 : [2, 3],
    24 : [2, 4],
    25 : [2, 5],
    26 : [2, 6],
    27 : [2, 7],
    28 : [2, 8],
    29 : [2, 9],
    33 : [3, 3],
    34 : [3, 4],
    35 : [3, 5],
    36 : [3, 6],
    37 : [3, 7],
    38 : [3, 8],
    39 : [3, 9],
    44 : [4, 4],
    45 : [4, 5],
    46 : [4, 6],
    47 : [4, 7],
    48 : [4, 8],
    49 : [4, 9],
    55 : [5, 5],
    56 : [5, 6],
    57 : [5, 7],
    58 : [5, 8],
    59 : [5, 9],
    66 : [6, 6],
    67 : [6, 7],
    68 : [6, 8],
    69 : [6, 9],
    77 : [7, 7],
    78 : [7, 8],
    79 : [7, 9],
    88 : [8, 8],
    89 : [8, 9],
    99 : [9, 9]
    }
tft_spatula_composition_item_dict = {
    18 : 0,
    28 : 0,
    38 : 0,
    48 : 0,
    58 : 0,
    68 : 0,
    78 : 0,
    88 : 0,
    89 : 0
}
used_spatula_items = False
tft_base_item_name_dict = {}
tft_full_item_name_dict = {}
tft_spatula_full_item_name_dict = {}
item_list_dict = {}
top_trait_name = [' ', ' ', ' ']
top_trait_occurance = [0, 0, 0]
top_trait_name_number_unit = [' ', ' ', ' ']
top_trait_occurance_number_unit = [0, 0, 0]
bottom_trait_name = [' ', ' ', ' ']
bottom_trait_occurance = [10, 10, 10]
bottom_trait_number_unit_name = [' ', ' ', ' ']
bottom_trait_number_unit_occurance = [10, 10, 10]
top_full_item_name = [' ', ' ', ' ']
top_full_item_occurance = [0, 0, 0]
bottom_full_item_name = [' ', ' ', ' ']
bottom_full_item_occurance = [0, 0, 0]
top_composition_item_name = [' ', ' ', ' ']
top_composition_item_occurance = [0, 0, 0]
bottom_composition_item_name = [' ', ' ', ' ']
bottom_composition_item_occurance = [0, 0, 0]
top_spatula_item_name = [' ', ' ', ' ']
top_spatula_item_occurance = [0, 0, 0]
bottom_spatula_item_name = [' ', ' ', ' ']
bottom_spatula_item_occurance = [0, 0, 0]

my_tft_total_trait_occurance_dict_ordered = {}
my_tft_total_trait_unit_number_dict_ordered = {}
tft_base_item_name_dict_ordered = {}
tft_full_item_name_dict_ordered = {}
tft_spatula_full_item_name_dict_ordered = {}
tft_total_trait_occurance_per_match_dict_ordered = {}
tft_full_item_name_per_match_dict_ordered = {}
tft_composition_item_name_per_match_dict_ordered = {}
tft_spatula_item_name_per_match_dict_ordered = {}

#TFT environment
if my_tft_rank == []:  
    my_tft_name = my_tft["name"]
    my_tft_rank = "Unranked"

else:
    my_tft_rank_dict = my_tft_rank[0]
    my_tft_name = my_tft["name"]
    my_tft_rank = my_tft_rank_dict["tier"]+ " "  + my_tft_rank_dict["rank"] + " " + str(my_tft_rank_dict["leaguePoints"])  + "LP"    

# last match TFT
tft_match_dict = my_tft_matches[0]
my_tft_match_puuid = 0
my_tft_match_index = 0
my_tft_average_placement = 0
my_tft_average_last_round = 0
my_tft_average_time_eliminated = 0
my_tft_average_level = 0
my_tft_current_trait_occurance_dict = {}
my_tft_total_trait_unit_number_dict = {}
my_tft_total_trait_occurance_dict = {}
my_tft_total_item_occurance_dict = {}

# Report
with open(user_input_summonerName_server_filename, 'w') as tft_file:
    tft_file.write("Summoner Name: " + my_tft_name + "\n")
    tft_file.write("Rank: " + my_tft_rank + "\n\n\n\n")

with open('set4/items.json', 'r') as tft_item_file:
    item_list_dict = tft_item_file.read()

item_list_dict = json.loads(item_list_dict)

for y in range(0,my_match_history_count):
    tft_match_dict = my_tft_matches[y]
    tft_match_detail = tft_watcher.match.by_id(my_tft_region, tft_match_dict)
    tft_match_detail_paritipant = tft_match_detail['info']['participants']  
    for x in range(0,8):

        # Finds the player 
        if tft_match_detail_paritipant[x]["puuid"] == my_tft["puuid"]:
            my_tft_match_puuid = tft_match_detail_paritipant[x]["puuid"]
            my_tft_match_index = x  

            # Result Detail variables
            my_tft_average_placement += tft_match_detail_paritipant[my_tft_match_index]["placement"]
            my_tft_average_last_round += tft_match_detail_paritipant[my_tft_match_index]["last_round"]
            my_tft_average_time_eliminated += tft_match_detail_paritipant[my_tft_match_index]["time_eliminated"]
            my_tft_average_level += tft_match_detail_paritipant[my_tft_match_index]["level"]

            # Trait Occurance Detail
            my_tft_current_trait_occurance_dict = tft_match_detail_paritipant[my_tft_match_index]['traits']
            for x in range(0, len(my_tft_current_trait_occurance_dict)):
                s = my_tft_current_trait_occurance_dict[x]['name']
                if s not in my_tft_total_trait_occurance_dict:
                    my_tft_total_trait_occurance_dict.update({s: 1})
                else:
                    my_tft_total_trait_occurance_dict.update({s: (my_tft_total_trait_occurance_dict[s] + 1)})

                if s not in my_tft_total_trait_unit_number_dict:
                    my_tft_total_trait_unit_number_dict.update({s : my_tft_current_trait_occurance_dict[x]['num_units']})
                else:
                    my_tft_total_trait_unit_number_dict.update({s: (my_tft_total_trait_unit_number_dict[s]+ my_tft_current_trait_occurance_dict[x]['num_units'])})

                if s in tft_trait_dict:
                    tft_trait_dict.update({s: tft_trait_dict[s] + 1})

            # Item occurance dict
            my_tft_current_unit_occurance_dict = tft_match_detail_paritipant[my_tft_match_index]['units']
            for j in range(0, len(my_tft_current_unit_occurance_dict)):
                t = my_tft_current_unit_occurance_dict[j]['items']
                for k in range(0,len(t)):
                    if t[k] != None:
                        if t[k] not in my_tft_total_item_occurance_dict:
                            my_tft_total_item_occurance_dict.update({t[k]: 1})
                        else:
                            my_tft_total_item_occurance_dict.update({t[k]: (my_tft_total_item_occurance_dict[t[k]] + 1)})

                        if t[k] in tft_spatula_composition_item_dict:
                            tft_spatula_composition_item_dict.update({t[k]: tft_spatula_composition_item_dict[t[k]] + 1})
                            used_spatula_items = True
            
            # Find composition of items
            for l in my_tft_total_item_occurance_dict:
                if l > 9:
                    for m in tft_composition_item_dict:
                        if l == m:
                            item1 = tft_composition_item_dict[m][0]
                            item2 = tft_composition_item_dict[m][1]
                            for n in tft_base_item_dict:
                                if n == item1:
                                    tft_base_item_dict.update({n: tft_base_item_dict[n] + 1})
                                if n == item2:
                                    tft_base_item_dict.update({n: tft_base_item_dict[n] + 1})

            # Info on last match
            if y == 0:
                
                # Convert id to name of composition items
                for o in tft_base_item_dict:
                    indexValue = findIdToNameFunction('id', o)
                    tft_base_item_name_dict.update({indexValue: tft_base_item_dict[o]})

                # Convert id to name of full items
                for p in my_tft_total_item_occurance_dict:
                    indexValue = findIdToNameFunction('id', p)
                    tft_full_item_name_dict.update({indexValue: my_tft_total_item_occurance_dict[p]})

                # Convert id to name of spatuala full items 
                for q in tft_spatula_composition_item_dict:
                    indexValue = findIdToNameFunction('id', q)
                    tft_spatula_full_item_name_dict.update({indexValue: tft_spatula_composition_item_dict[q]})
                    
                #Ordering total trait unit number dict    
                my_tft_total_trait_unit_number_dict_ordered = orderingDictDescendingFunction(my_tft_total_trait_unit_number_dict)

                #Ordering total trait occurance dict 
                my_tft_total_trait_occurance_dict_ordered = orderingDictDescendingFunction(my_tft_total_trait_occurance_dict)

                #Ordering name of composition items dict    
                tft_base_item_name_dict_ordered = orderingDictDescendingFunction(tft_base_item_name_dict)
            
                #Ordering name of full items dict    
                tft_full_item_name_dict_ordered = orderingDictDescendingFunction(tft_full_item_name_dict)
                
                # Find top 3 total traits by occurance and number of units 
                top_trait_occurance, top_trait_name = findTopThreeFunction(my_tft_total_trait_occurance_dict_ordered, top_trait_occurance, top_trait_name)
                top_trait_occurance_number_unit, top_trait_name_number_unit = findTopThreeFunction(my_tft_total_trait_unit_number_dict_ordered, top_trait_occurance_number_unit, top_trait_name_number_unit)

                with open(user_input_summonerName_server_filename, 'a') as tft_file:

                    tft_file.write("Last Match:\n")
                    tft_file.write("\tPlacement: " + str(my_tft_average_placement) + "\n")
                    tft_file.write("\tLast round: " + str(round(my_tft_average_last_round,2)) + "\n")
                    tft_file.write("\tAverage time eliminated: " + str(round((round(my_tft_average_time_eliminated, 2))/ 60, 2)) + " minutes" + " (" + str(round(my_tft_average_time_eliminated, 2)) + " seconds)" + "\n") 
                    tft_file.write("\tLevel at elimination: " + str(my_tft_average_level) + "\n\n")
                    
                    tft_file.write("\tTop 3 traits used (by unit count): " + top_trait_name_number_unit[0] + " : " + str(top_trait_occurance_number_unit[0]) + ", " + top_trait_name_number_unit[1] + " : " + str(top_trait_occurance_number_unit[1]) + ", " + top_trait_name_number_unit[2] + " : " + str(top_trait_occurance_number_unit[2]) + "\n")
                    tft_file.write("\tList of total traits used (by unit count): " + json.dumps(my_tft_total_trait_unit_number_dict_ordered) + "\n\n")

                    tft_file.write("\tTop 3 traits used (by occurance): " + top_trait_name[0] + " : " + str(top_trait_occurance[0]) + ", " + top_trait_name[1] + " : " + str(top_trait_occurance[1]) + ", " + top_trait_name[2] + " : " + str(top_trait_occurance[2]) + "\n")
                    tft_file.write("\tList of total traits used (by occurance): " + json.dumps(my_tft_total_trait_occurance_dict_ordered) + "\n\n")
                    
                    tft_file.write("\tList of total full items used : " + json.dumps(tft_full_item_name_dict_ordered) + "\n")
                    tft_file.write("\tList of total composition items used : " + json.dumps(tft_base_item_name_dict_ordered) + "\n")
                    if (used_spatula_items == True):
                        tft_file.write("\tList of total spatula full items used : " + json.dumps(tft_spatula_full_item_name_dict) + "\n")
                    tft_file.write("\n")


my_tft_average_placement = my_tft_average_placement / my_match_history_count
my_tft_average_last_round = my_tft_average_last_round / my_match_history_count
my_tft_average_time_eliminated = my_tft_average_time_eliminated / my_match_history_count
my_tft_average_level = my_tft_average_level / my_match_history_count
 
# Convert id to name of composition items
for o in tft_base_item_dict:
    indexValue = findIdToNameFunction('id', o)
    tft_base_item_name_dict.update({indexValue: tft_base_item_dict[o]})

# Convert id to name of full items
for p in my_tft_total_item_occurance_dict:
    indexValue = findIdToNameFunction('id', p)
    tft_full_item_name_dict.update({indexValue: my_tft_total_item_occurance_dict[p]})

# Convert id to name of spatuala full items 
for q in tft_spatula_composition_item_dict:
    indexValue = findIdToNameFunction('id', q)
    tft_spatula_full_item_name_dict.update({indexValue: tft_spatula_composition_item_dict[q]})

# Ordering dicts
#   Ordering trait occurance dict
my_tft_total_trait_occurance_dict_ordered = orderingDictDescendingFunction(my_tft_total_trait_occurance_dict)
#   Ordering trait occurance by unit count dict
my_tft_total_trait_unit_number_dict_ordered = orderingDictDescendingFunction(my_tft_total_trait_unit_number_dict)
#   Ordering trait occurance by all traits
tft_trait_dict = orderingDictDescendingFunction(tft_trait_dict)
#   Ordering name of composition items dict    
tft_base_item_name_dict_ordered = orderingDictDescendingFunction(tft_base_item_name_dict)
#   Ordering name of full items dict    
tft_full_item_name_dict_ordered = orderingDictDescendingFunction(tft_full_item_name_dict)
#   Ordering name of spatula full items dict
tft_spatula_full_item_name_dict_ordered = orderingDictDescendingFunction(tft_spatula_full_item_name_dict)

# Top/Bottom traits/full items/composition items
#   Find top 3 total traits by occurance and number of units 
top_trait_occurance, top_trait_name = findTopThreeFunction(my_tft_total_trait_occurance_dict_ordered, top_trait_occurance, top_trait_name)
top_trait_occurance_number_unit, top_trait_name_number_unit = findTopThreeFunction(my_tft_total_trait_unit_number_dict_ordered, top_trait_occurance_number_unit, top_trait_name_number_unit)
#   Find bottom traits used by occurance
bottom_trait_name, bottom_trait_occurance = orderingListAscendingFunction(tft_trait_dict)
bottom_trait_number_unit_name, bottom_trait_number_unit_occurance = orderingListAscendingFunction(my_tft_total_trait_unit_number_dict_ordered)
#   Find top 3 full items used
top_full_item_occurance, top_full_item_name  = findTopThreeFunction(tft_full_item_name_dict_ordered, top_full_item_occurance, top_full_item_name)
#   Find bottom full items used
bottom_full_item_name, bottom_full_item_occurance = orderingListAscendingFunction(tft_full_item_name_dict_ordered)
#   Find top 3 composition items used 
top_composition_item_occurance, top_composition_item_name = findTopThreeFunction(tft_base_item_name_dict_ordered, top_composition_item_occurance, top_composition_item_name)
#   Find bottom composition items used 
bottom_composition_item_name, bottom_composition_item_occurance = orderingListAscendingFunction(tft_base_item_name_dict_ordered)
#   Find top 3 spatula items used 
top_spatula_item_occurance, top_spatula_item_name = findTopThreeFunction(tft_spatula_full_item_name_dict_ordered, top_spatula_item_occurance, top_spatula_item_name)
#   Find bottom spatula items used 
bottom_spatula_item_name, bottom_spatula_item_occurance = orderingListAscendingFunction(tft_spatula_full_item_name_dict_ordered)

# Find trait occurance per match 
for z in my_tft_total_trait_occurance_dict_ordered:
    tft_total_trait_occurance_per_match_dict_ordered.update({z: round((my_tft_total_trait_occurance_dict_ordered[z]/my_match_history_count), 2)})

# Find full item occurance per match 
for y in tft_full_item_name_dict_ordered:
    tft_full_item_name_per_match_dict_ordered.update({y: round((tft_full_item_name_dict_ordered[y]/my_match_history_count),2)})

# Find composition item occurance per match 
for w in tft_base_item_name_dict_ordered:
    tft_composition_item_name_per_match_dict_ordered.update({w: round((tft_base_item_name_dict_ordered[w]/my_match_history_count),2)})

# Find spatula item occurance per match
for u in tft_spatula_full_item_name_dict_ordered:
    tft_spatula_item_name_per_match_dict_ordered.update({u: round((tft_spatula_full_item_name_dict_ordered[u]/my_match_history_count),2)})

with open(user_input_summonerName_server_filename, 'a') as tft_file:
    tft_file.write("Last " + str(my_match_history_count) +" Matches: \n")
    tft_file.write("\tPlacement: " + str(round(my_tft_average_placement,2)) + "\n")
    tft_file.write("\tLast round: " + str(round(my_tft_average_last_round,2)) + "\n")
    tft_file.write("\tAverage time eliminated: " + str(round((round(my_tft_average_time_eliminated, 2))/ 60, 2)) + " minutes" + " (" + str(round(my_tft_average_time_eliminated, 2)) + " seconds)" + "\n") 
    tft_file.write("\tLevel at elimination: " + str(round(my_tft_average_level, 2)) + "\n\n")
    
    tft_file.write("\tList of traits used per game (by occurance): " + json.dumps(tft_total_trait_occurance_per_match_dict_ordered) + "\n")    
    tft_file.write("\tList of full items used per game: " + json.dumps(tft_full_item_name_per_match_dict_ordered) + "\n")    
    tft_file.write("\tList of composition items used per game: " + json.dumps(tft_composition_item_name_per_match_dict_ordered) + "\n")    
    if (used_spatula_items == True):
        tft_file.write("\tList of spatula items used per game: " + json.dumps(tft_spatula_item_name_per_match_dict_ordered) + "\n\n")    

    tft_file.write("\tTop 3 priority traits used (by unit count): " + top_trait_name_number_unit[0] + " : " + str(top_trait_occurance_number_unit[0]) + ", " + top_trait_name_number_unit[1] + " : " + str(top_trait_occurance_number_unit[1]) + ", " + top_trait_name_number_unit[2] + " : " + str(top_trait_occurance_number_unit[2]) + "\n")
    tft_file.write("\tLow priority traits used (by unit count): ")
    for y in range(0, len(bottom_trait_number_unit_name)):
        tft_file.write(str(bottom_trait_number_unit_name[y]) + " : " + str(bottom_trait_number_unit_occurance[y]) + ", ")
    tft_file.write("\n")
    tft_file.write("\tList of total traits used (by unit count): " + json.dumps(my_tft_total_trait_unit_number_dict_ordered) + "\n\n")
    
    tft_file.write("\tTop 3 priority traits used (by occurance): ") 
    for x in range(0, len(top_trait_name)):
        tft_file.write(str(top_trait_name[x]) + " : " + str(top_trait_occurance[x]) + ", ")
    tft_file.write("\n")
    tft_file.write("\tLow priority traits (by occurance): ")
    tft_file.write(str(bottom_trait_name[0]) + " : " + str(bottom_trait_occurance[0]) + ", ")
    for x in range(1, len(bottom_trait_name)):
        tft_file.write(", " + str(bottom_trait_name[x]) + " : " + str(bottom_trait_occurance[x]))
    tft_file.write("\n")
    tft_file.write("\tList of total traits used (by occurance): " + json.dumps(my_tft_total_trait_occurance_dict_ordered) + "\n\n")                
    
    tft_file.write("\tList of total full items used : " + json.dumps(tft_full_item_name_dict_ordered) + "\n")
    tft_file.write("\tList of total composition items used : " + json.dumps(tft_base_item_name_dict_ordered) + "\n")
    if (used_spatula_items == True):
        tft_file.write("\tList of total spatula full items used : " + json.dumps(tft_spatula_full_item_name_dict_ordered) + "\n")

# Summary of player 
f = open(user_input_summonerName_server_filename, "r")
contents = f.readlines()
f.close()

# Summary output 
contents.insert(3, my_tft_name + ' Summary (per game stat): \n')
contents.insert(4, '\tHigh priority: \n')
#   Summary for high priority traits
high_priority_traits =  '\t\tTraits: ' + str(top_trait_name[0]) + ' (' + str(tft_total_trait_occurance_per_match_dict_ordered[top_trait_name[0]]) + ')' 
for highPrioTrait in range(1,3):
    high_priority_traits += ", " + str(top_trait_name[highPrioTrait]) + ' (' + str(tft_total_trait_occurance_per_match_dict_ordered[top_trait_name[highPrioTrait]]) + ')'
contents.insert(5, high_priority_traits + '\n')
#   Summary for high priority full items
high_priority_full_items = '\t\tFull items: ' + str(top_full_item_name[0]) + ' (' + str(tft_full_item_name_per_match_dict_ordered[top_full_item_name[0]]) + ')' 
for highPrioFullItem in range(1,3):
    high_priority_full_items += ", " + str(top_full_item_name[highPrioFullItem]) + ' (' + str(tft_full_item_name_per_match_dict_ordered[top_full_item_name[highPrioFullItem]]) + ')'
contents.insert(6, high_priority_full_items + '\n')
#   Summary for high priority composition items
high_priority_composition_items = '\t\tComposition items: ' + str(top_composition_item_name[0]) + ' (' + str(tft_composition_item_name_per_match_dict_ordered[top_composition_item_name[0]]) + ')' 
for highPrioCompItem in range(1,3):
    high_priority_composition_items += ", " + str(top_composition_item_name[highPrioCompItem]) + ' (' + str(tft_composition_item_name_per_match_dict_ordered[top_composition_item_name[highPrioCompItem]]) + ')'
contents.insert(7, high_priority_composition_items + '\n')
#   Summary for high priority spatula items
if (used_spatula_items == True):
    high_priority_spatula_items = '\t\tSpatula items: ' + str(top_spatula_item_name[0]) + ' (' + str(tft_spatula_item_name_per_match_dict_ordered[top_spatula_item_name[0]]) + ')' 
    for highPrioSpatItem in range(1,3):
        high_priority_spatula_items += ", " + str(top_spatula_item_name[highPrioSpatItem]) + ' (' + str(tft_spatula_item_name_per_match_dict_ordered[top_spatula_item_name[highPrioSpatItem]]) + ')'
    contents.insert(8, high_priority_spatula_items + '\n\n')


contents.insert(9, '\tLow priority: \n')
#   Summary for low priority traits
low_priority_traits = '\t\tTraits: '
if bottom_trait_name[0] in tft_total_trait_occurance_per_match_dict_ordered:
    low_priority_traits += str(bottom_trait_name[0]) + ' (' + str(tft_total_trait_occurance_per_match_dict_ordered[bottom_trait_name[0]]) + ')'
else:
    low_priority_traits += str(bottom_trait_name[0]) + ' (0)'
for lowPrioTrait in range(1, len(bottom_trait_name)):
    if bottom_trait_name[lowPrioTrait] in tft_total_trait_occurance_per_match_dict_ordered:
        low_priority_traits += ", " + str(bottom_trait_name[lowPrioTrait]) + ' (' + str(tft_total_trait_occurance_per_match_dict_ordered[bottom_trait_name[lowPrioTrait]]) + ')'
    else:
        low_priority_traits += ", " + str(bottom_trait_name[lowPrioTrait]) + ' (0)'
contents.insert(10, low_priority_traits + "\n")
#   Summary for low priority full items
low_priority_full_items = '\t\tFull items: '
if bottom_full_item_name[0] in tft_full_item_name_per_match_dict_ordered:
    low_priority_full_items += str(bottom_full_item_name[0]) + ' (' + str(tft_full_item_name_per_match_dict_ordered[bottom_full_item_name[0]]) + ')'
else:
    low_priority_full_items += str(bottom_full_item_name[0]) + ' (0)'
for lowPrioFullItem in range(0, len(bottom_full_item_name)):
    if bottom_full_item_name[lowPrioFullItem] in tft_full_item_name_per_match_dict_ordered:
        low_priority_full_items += ", " + str(bottom_full_item_name[lowPrioFullItem]) + ' (' + str(tft_full_item_name_per_match_dict_ordered[bottom_full_item_name[lowPrioFullItem]]) + ')'
    else:
        low_priority_full_items += ", " + str(bottom_full_item_name[lowPrioFullItem]) + ' (0)'
contents.insert(11, low_priority_full_items + "\n")
#   Summary for low priority composition items
low_priority_composition_items = '\t\tComposition items: '
if bottom_composition_item_name[0] in tft_composition_item_name_per_match_dict_ordered:
    low_priority_composition_items += str(bottom_composition_item_name[0]) + ' (' + str(tft_composition_item_name_per_match_dict_ordered[bottom_composition_item_name[0]]) + ')'
else:
    low_priority_composition_items += str(bottom_composition_item_name[0]) + ' (0)'
for lowPrioCompItem in range(0, len(bottom_composition_item_name)):
    if bottom_composition_item_name[lowPrioCompItem] in tft_composition_item_name_per_match_dict_ordered:
        low_priority_composition_items += ", " + str(bottom_composition_item_name[lowPrioCompItem]) + ' (' + str(tft_composition_item_name_per_match_dict_ordered[bottom_composition_item_name[lowPrioCompItem]]) + ')'
    else:
        low_priority_composition_items += ", " + str(bottom_composition_item_name[lowPrioCompItem]) + ' (0)'
contents.insert(12, low_priority_composition_items + "\n")
#   Summary for low priority spatula items
if (used_spatula_items == True):
    low_priority_spatula_items = '\t\tSpatula items: '
    if bottom_spatula_item_name[0] in tft_spatula_item_name_per_match_dict_ordered:
        low_priority_spatula_items += str(bottom_spatula_item_name[0]) + ' (' + str(tft_spatula_item_name_per_match_dict_ordered[bottom_spatula_item_name[0]]) + ')'
    else:
        low_priority_spatula_items += str(bottom_spatula_item_name[0]) + ' (0)'
    for lowPrioSpatItem in range(0, len(bottom_spatula_item_name)):
        if bottom_spatula_item_name[lowPrioSpatItem] in tft_spatula_item_name_per_match_dict_ordered:
            low_priority_spatula_items += ", " + str(bottom_spatula_item_name[lowPrioSpatItem]) + ' (' + str(tft_spatula_item_name_per_match_dict_ordered[bottom_spatula_item_name[lowPrioSpatItem]]) + ')'
        else:
            low_priority_spatula_items += ", " + str(bottom_spatula_item_name[lowPrioSpatItem]) + ' (0)'
    contents.insert(13, low_priority_spatula_items)



f = open(user_input_summonerName_server_filename, "w")
contents = "".join(contents)
f.write(contents)
f.close()
