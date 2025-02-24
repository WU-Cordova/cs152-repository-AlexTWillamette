from datastructures.array2d import Array2D
from typing import Iterator, Sequence
testarray = Array2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]], data_type=int)

def main():

    print("Hello, World!")

    test = "invalid_string"
    if isinstance(test, Sequence):
        print("yup")
    for row in test:
        print(row)
        print(type(row))
        #if isinstance(row, Sequence):
        #    print("uhuh")

    #_ = Array2D(123, data_type=int)  # Not a list of lists

    #_ = Array2D("invalid_string", data_type=int)  # Not a sequence of sequences

    #_ = Array2D({1: [1, 2, 3]}, data_type=int)  # Dictionary is not a valid sequence


if __name__ == '__main__':
    main()
