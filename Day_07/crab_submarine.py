import numpy as np

def read_in_crab_pos(path:str) -> "list[int]":
    data = open(path, "r")
    positions = list()
    for line in data:
        positions.extend(line.split(","))
    
    positions = list(map(int, positions))

    return positions


def calculate_fuel(positions, n:int, burning_rate="constant"):
    X = np.array(positions)
    if burning_rate == "constant":
        X -= n
        X = np.abs(X)
        fuel = np.sum(X)
    elif burning_rate == "linear":
        X = np.float32(positions)
        X -=n
        X = np.abs(X)
        X *= (X-1) * 0.5  # Formula for: Given a number n, what is the sum of all integers less than n?
        fuel = np.sum(X)
    
    return fuel






if __name__ == "__main__":
    path = "Day_07/input_test.txt"
    path = "Day_07/input.txt"

    positions = read_in_crab_pos(path)

    print(f"There are {len(positions)} crab submarines.")
    print(f"Mean position:\t\t{np.mean(positions)}")
    print(f"Median position:\t{np.median(positions)}")

    
    # Task 1
    print("--- Task 1: Constant fuel burning ---")
    fuel_prev = 0
    fuel_history = list()
    for i in range(min(positions), max(positions)):
        fuel = calculate_fuel(positions, i)
        if fuel > fuel_prev:    grad = "+"
        else:                   grad = "-"

        #print(f"Algining at pos {i} requires {fuel:2.0f}. grad: {grad}")
        fuel_prev = fuel
        fuel_history.append(fuel)

    argmin = np.argmin(fuel_history)
    print(f"\n-> Minimum fuel of {fuel_history[argmin]} at position {argmin}!\n")



    # Task 2
    print("--- Task 2: Linearly increasing fuel burning ---")

    fuel_history = list()
    for i in range(min(positions), max(positions)):
        fuel = calculate_fuel(positions, i, burning_rate="linear")
        fuel_history.append(fuel)
        #print(f"Algining at pos {i} requires {fuel:2.0f}")

    argmin = np.argmin(fuel_history)
    print(f"\n-> Minimum fuel of {fuel_history[argmin]} at position {argmin}!\n")
    



