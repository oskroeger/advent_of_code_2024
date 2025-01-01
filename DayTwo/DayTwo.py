#!/usr/bin/env python

import numpy as np

def findSafe():
    """
    Tests if each line in a file is "safe", passes the following requirements (count):
    - Completely ascending or descending
    - No duplicate numbers
    - The difference between any two consecutive numbers <= 3

    Also tests if each line passes if any one number is removed from the line (updated count).

    """

    count = 0
    updated_count = 0

    with open('DayTwoData.txt', 'r') as file:
        for line in file:
            numbers = np.array([int(num) for num in line.split()])

            is_sorted = np.array_equal(np.sort(numbers), numbers)
            is_inversely_sorted = np.array_equal(np.sort(numbers)[::-1], numbers)

            for i in range(len(numbers)):
                if ((is_sorted) and (np.all(np.diff(numbers) <= 3)) and (np.all(np.diff(numbers) > 0))):
                    count += 1
                    updated_count += 1
                    break

                elif (is_inversely_sorted and (np.all(np.diff(numbers) >= -3)) and (np.all(np.diff(numbers) < 0))):
                    count += 1
                    updated_count += 1
                    break

                new_arr = np.delete(numbers, i)
                new_is_sorted = np.array_equal(np.sort(new_arr), new_arr)
                new_is_inversely_sorted = np.array_equal(np.sort(new_arr)[::-1], new_arr)

                if ((new_is_sorted) and (np.all(np.diff(new_arr) <= 3)) and (np.all(np.diff(new_arr) > 0))):
                    updated_count += 1
                    break
                elif ((new_is_inversely_sorted) and (np.all(np.diff(new_arr) >= -3)) and (np.all(np.diff(new_arr) < 0))):
                    updated_count += 1
                    break


    print(f'COUNT = {count}')
    print(f'UPDATED_COUNT = {updated_count}')

if __name__ == "__main__":
    findSafe()