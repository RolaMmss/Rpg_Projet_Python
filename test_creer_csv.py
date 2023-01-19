# # import csv  
# from main import players, score

# # empty_list_1= []
# # list_of_players = empty_list_1.append(player_name)
# # print(list_of_players)
# # # empty_list_2= []


# import csv  

# # header = ['name', 'area', 'country_code2', 'country_code3']
# # data = ['Afghanistan', 652090, 'AF', 'AFG']

# with open('board.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     player = [writer.writerow(players)]

#     # write the data
#     final_score = writer.writerow(score)



# def display_final(rpg_data, player_name):
#     # board = {}
#     # board.append(player_name,{rpg_data['player_score']})
#     with open('board.csv', 'w', encoding='UTF8') as f:
#         writer = csv.writer(f)

#         # write the header
#         player = writer.writerow(player_name)

#         # write the data
#         final_score = writer.writerow({rpg_data['player_score']})
#     return player, final_score
