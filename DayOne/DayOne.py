#!/usr/bin/env python

def findDifferences():

    left = []
    right = []

    with open('DayOneData.txt', 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            left.append(numbers[0])
            right.append(numbers[1])

    left.sort()
    right.sort()

    sums = []
    sim_score = 0
    sum = 0

    for i in range(len(left)):
        sums.append(abs(right[i] - left[i]))
        sim_score += right.count(left[i]) * left[i]
        sum += sums[i]

    print(sum)
    print(sim_score)


if __name__ == "__main__":

    findDifferences()