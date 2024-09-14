'''
Advent Of Code Day 02 Part 02
-> For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?

'''
import re
cube_set_sum = 0

# Reading game data from data.txt file
with open('data.txt', 'r') as file:
    data = file.readlines()
    # Remove new line characters from each lines
    data = [item.strip() for item in data]

def is_game_valid(game):
    game, game_info = game.split(':')
    game_info = re.split('[;,]', game_info)
    game_info = [item.strip() for item in game_info]

    # iterating through each game info item to find no. of cubes
    red_cubes = [1]
    green_cubes = [1]
    blue_cubes = [1]
    for item in game_info:
        if 'red' in item:
            red_cubes.append(int(item.split(' ')[0].strip()))
        elif 'green' in item:
            green_cubes.append(int(item.split(' ')[0].strip()))
        else:
            blue_cubes.append(int(item.split(' ')[0].strip()))
    
        # Calculating power of cube set
        cube_set = max(red_cubes) * max(green_cubes) * max(blue_cubes)

    return cube_set

for game in data:
    cube_set = is_game_valid(game)
    cube_set_sum += cube_set

print(cube_set_sum)