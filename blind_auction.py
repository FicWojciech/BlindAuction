from art import auction_hammer
import os

print(auction_hammer)


def convert(a):
    players_list = iter(a)
    players_dict = dict(zip(players_list, players_list))
    winner_name = (max(players_dict, key=players_dict.get))
    print(f"The winner is {winner_name} with a bid of ${players_dict[winner_name]}!")


player_name = input("What is your name?\n").capitalize()
player_bid = int(input("What is your bid?\n$"))
players_list = []
players_list.append(player_name)
players_list.append(player_bid)


flag = True

while flag:
    other_players = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    os.system('cls')
    player_name = input("What is your name?\n").capitalize()
    player_bid = int(input("What is your bid?\n$"))
    other_players = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    players_list.append(player_name)
    players_list.append(player_bid)
    if other_players == 'no':
        convert(players_list)
        flag = False
