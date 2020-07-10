def intersection(arrays):
    # start a tally dictionary
    tallies = {}
    
    # loop through each sub array tallying all the numbers
    for array in arrays:
        for num in array:
            if num not in tallies:
                tallies[num] = 1
            else:
                tallies[num] += 1
    
    # use list comprehension to sort tallies only if they equal the length of arrays
    return [k for k, v in tallies.items() if v == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
