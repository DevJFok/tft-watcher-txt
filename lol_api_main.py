from riotwatcher import LolWatcher, ApiError

# golbal variables
api_key = 'RGAPI-f10ecff0-28c0-4855-95f3-2a724f9b7305'
my_lol_region = 'na1'
my_match_history_count = 10

# Assume valid Summoner Name
user_input_summonerName = input("Enter Summoner Name: ")
user_input_summonerName_filename = user_input_summonerName + '_lol_file.txt'
# Assume valid integer > 0
user_input_match_history_count = int(input("Enter Match History count: "))

#LoL global variables
lol_watcher = LolWatcher(api_key)
my_lol = lol_watcher.summoner.by_name(my_lol_region, user_input_summonerName)
my_lol_rank = lol_watcher.league.by_summoner(my_lol_region, my_lol['id'])
my_lol_matches = lol_watcher.match.matchlist_by_account(my_lol_region, my_lol['accountId'])

#LoL environment 
my_lol_dict = my_lol_rank[0]

my_lol_name = "Summoner Name: " + my_lol_dict["summonerName"]
my_lol_rank = "Rank: " + my_lol_dict["tier"] + " "  + my_lol_dict["rank"] + " " + str(my_lol_dict["leaguePoints"])
my_lol_win_percentage = "Win Percentage: " + str(round((my_lol_dict["wins"]/(my_lol_dict["wins"]+my_lol_dict["losses"])*100), 2)) + "% Wins: " + str(my_lol_dict["wins"]) + " Losses: " + str(my_lol_dict["losses"])



with open(user_input_summonerName_filename, 'w') as lol_file:
    lol_file.write(my_lol_name + "\n")
    lol_file.write(my_lol_rank + "\n")
    lol_file.write(my_lol_win_percentage + "\n")

# last match LoL 
last_lol_match = my_lol_matches['matches'][0]
match_detail = lol_watcher.match.by_id(my_lol_region, last_lol_match['gameId'])