import numpy as np
import operator

class DataPoint():

    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # assert( x1 <= x2)
        # assert( y1 <= y2)

    def get_coord(self) -> "list[int]":
        return self.x1, self.y1, self.x2, self.y2


def func1(path):
    data = open(path, "r")
    datapoints = list()

    # append all data to a list
    for m in data:
        a = m.strip().split(" -> ")
        x1, y1 = list(map(int, a[0].split(",")))
        x2, y2 = list(map(int, a[1].split(",")))
        #print(f"{x1,y1} -> {x2,y2}")
        datapoints.append(DataPoint(x1, y1, x2, y2))

    # get max value dimensions
    x_max = max([max(d.x1, d.x2) for d in datapoints])
    y_max = max([max(d.y1, d.y2) for d in datapoints])


    # -----------------------------------------------
    #            T A S K   1
    # -----------------------------------------------
    # print("\nTask 1: Only horizontal and vertical\n")
    # vent_map = np.zeros((x_max+1, y_max+1))

    # # add the vents to the map
    # print("\nAdding vents:")
    # for point in datapoints:
    #     vent_map = add_vents(vent_map, point)

    # # count the number of vents above 2x
    # count = np.sum(vent_map > 1)

    # print("Max number of vents >2: ", count)
    # if max(vent_map.shape) < 11:
    #     print(vent_map)


    # -----------------------------------------------
    #            T A S K   2
    # -----------------------------------------------
    
    print("\nTask 2: Vents which are diagonal\n")
    vent_map = np.zeros((x_max+1, y_max+1))

    for point in datapoints:
        vent_map = add_vents(vent_map, point, diagonal=True)

    count = np.sum(vent_map > 1)

    print("Max number of vents >2: ", count)
    if max(vent_map.shape) < 11:
        print(vent_map)

    return


def add_vents(vent_map: np.ndarray, point:DataPoint, diagonal=False) -> np.ndarray:

    x1,y1,x2,y2 = point.get_coord()

    if diagonal is False:
        #print(f"\n{x1,y1} -> {x2,y2}")

        # Check if this line of vents is diagonal
        if (x1 != x2) and (y1 != y2):
            print("No change.")
            
        else:
            # subscripts of array must be in ascending order
            if (x1 > x2): x1, x2 = x2, x1
            if (y1 > y2): y1, y2 = y2, y1
            
            vent_map[x1:x2+1, y1:y2+1] += 1
            #print(vent_map)

        return vent_map

    if diagonal is True:

        # Check if this line of vents is diagonal
        if (x1 != x2) and (y1 != y2):

            # create matrix with diagonal full of ones
            dx, dy = x2-x1, y2-y1
            x_dim = abs(dx) + 1
            y_dim = abs(dy) + 1

            assert(x_dim == y_dim)
            line_of_vents = np.eye(y_dim)
            if (dx * dy < 0): line_of_vents = np.rot90(line_of_vents)

            # subscripts of array must be in ascending order
            if (x1 > x2): x1, x2 = x2, x1
            if (y1 > y2): y1, y2 = y2, y1

            vent_map[x1:x2+1, y1:y2+1] += line_of_vents

            print("Diagonal.")
            print(f"\n{x1,y1} -> {x2,y2}")
            print( vent_map)

        else:
            # subscripts of array must be in ascending order
            if (x1 > x2): x1, x2 = x2, x1
            if (y1 > y2): y1, y2 = y2, y1
            
            vent_map[x1:x2+1, y1:y2+1] += 1
            #print(vent_map)

        return vent_map

        





    





if __name__ == "__main__":
    path = "Day_05/test_input.txt"
    path = "Day_05/input.txt"
    func1(path)