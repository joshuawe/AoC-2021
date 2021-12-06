import numpy as np
from collections import Counter, OrderedDict




def read_in_fish_status(path:str) -> "list[int]":
    data = open(path, "r")
    stat = list()
    for line in data:
        stat.extend(line.split(","))
    
    stat = map(int, stat)
    stat = dict(Counter(stat))
    stat = OrderedDict(sorted(stat.items()))

    fish_population = OrderedDict()
    for key in range(0,9):
        try:
            fish_population[key] = stat[key]
        except:
            fish_population[key] = 0

    print("Current fish popoluation:\n", fish_population)

    return fish_population


def next_day(fish_population:OrderedDict) -> OrderedDict:
    pop_nxt_day = {key: 0 for key in fish_population}
    for i in range(len(fish_population.keys())):
        # If it is the day of repruduction, add a fish 
        if i == 0:
            pop_nxt_day[6] += fish_population[i]
            pop_nxt_day[8] += fish_population[i]
        else:
            pop_nxt_day[i-1] += fish_population[i]

    return pop_nxt_day


def get_total_fish_num(fish_population:OrderedDict) -> int:
    num_fish = 0
    for key in fish_population:
        num_fish += fish_population[key]
    
    return num_fish





if __name__ == "__main__":

    path = "Day_06/input_test.txt"
    path = "Day_06/input.txt"
    days = 256

    fish_population = read_in_fish_status(path)

    for i in range(1,days+1):
        fish_population = next_day(fish_population)
        num_fish = get_total_fish_num(fish_population)
        print(f"Day {i:02.0f}:\t{num_fish} fish")