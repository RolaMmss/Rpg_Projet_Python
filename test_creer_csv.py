# import csv  
# from main import rpg_data, player_name

# empty_list_1= []
# list_of_players = empty_list_1.append(player_name)
# print(list_of_players)
# # empty_list_2= []


import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
