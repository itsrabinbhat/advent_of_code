'''
Advent Of Code Day 02
-> Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

'''
import re
idx_sum = 0

# Reading game data from data.txt file
with open('data.txt', 'r') as file:
    data = file.readlines()
    # Remove new line characters from each lines
    data = [item.strip() for item in data]

def is_game_valid(game):
    idx = 0
    game, game_info = game.split(':')
    game_info = re.split('[;,]', game_info)
    game_info = [item.strip() for item in game_info]

    # iterating through each game info item to find no. of cubes
    red_cubes = []
    green_cubes = []
    blue_cubes = []
    for item in game_info:
        if 'red' in item:
            red_cubes.append(int(item.split(' ')[0].strip()))
        elif 'green' in item:
            green_cubes.append(int(item.split(' ')[0].strip()))
        else:
            blue_cubes.append(int(item.split(' ')[0].strip()))
    
    # Checking if cubes in game are within threshold 
    if max(red_cubes) <= 12 and max(green_cubes) <= 13 and max(blue_cubes) <= 14:
        idx = int(game.split(' ')[-1].strip())

    return idx

for game in data:
    game_idx = is_game_valid(game)
    idx_sum += game_idx

print(idx_sum)