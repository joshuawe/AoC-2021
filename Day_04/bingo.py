import numpy as np


class Board():
    def __init__(self, lines:"list[str]") -> None:
        
        assert(len(lines) == 5)
        data = list()
        for line in lines:
            l = line.strip().split(" ")
            l = [int(element) for element in l if element.isnumeric()]
            data.append(l)

        self.board = np.array(data)
        self.marked = np.zeros(self.board.shape)
        self.bingo = False

        assert(self.board.shape == (5,5))

    def set_mark(self, number:int):
        """Will set a mark (==1) on self.marked wherever the entries of self.board are equal to the number."""
        hits = (self.board == number)
        if hits.any():
            #print("HIT!")
            self.marked += hits
        self.bingo_check(number)
        return
        

    def bingo_check(self, number):
        """Will check if any row's or column's sum equals to five"""
        
        if (np.sum(self.marked, axis=0) == 5).any() or (np.sum(self.marked, axis=1) == 5).any():
            print("BINGO! BINGO! BINGO!")
            score = number * np.sum(self.board * (self.marked == 0))
            print("The score of this board is ", score, "!")
            print("BINGO BINGO BINGO")
            self.bingo = True
        
        return

    def __repr__(self) -> str:
        return "Board:\n" + str(self.board) + "\n" + "Marked:\n" + str(self.marked) + "\n"








def read_numbers(path:str) -> "list[int]":
    """Reads in all the random numbers from a given path."""
    data = open(path, "r")
    numbers = list()
    for line in data:
        numbers.extend(line.split(","))

    return list(map(int, numbers))


def read_boards(path) -> "list[Board]":
    """Reads in all the boards from a given path."""
    data = open(path, "r")

    boards = list()
    temp = list()
    for line in data:
        if line != "\n":
            temp.append(line)
        elif len(temp) == 5:
            boards.append(Board(temp))
            temp = list()
        else:
            raise RuntimeError("Something went wrong. Sorry.")

    return boards



if __name__ == "__main__":

    print("Start...")
    
    path_numbers = "Day_04/test_number.txt"
    path_boards  = "Day_04/test_boards.txt"

    path_numbers = "Day_04/input_numbers.txt"
    path_boards  = "Day_04/input_boards.txt"

    numbers = read_numbers(path_numbers)
    boards  = read_boards(path_boards)

    print(f"Will draw {len(numbers)} numbers for {len(boards)} boards.")

    for number in numbers:
        print("==== NUMBER: ", number, " ====")
        for board in boards:
            board.set_mark(number)
            #print(board)
        
        # For task 1 comment out the following lines of code
        boards = [board for board in boards if board.bingo == False]

