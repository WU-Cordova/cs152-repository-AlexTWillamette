from datastructures.array2d import Array2D
from typing import Iterator, Sequence
testarray = Array2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]], data_type=int)

testarray = Array2D.empty(rows=3, cols=3, data_type=int)

def main():

    print("Hello, World!")

    print(testarray)
    for row in range(3):
        for col in range(3):
            print(testarray[row][col])


if __name__ == '__main__':
    main()
