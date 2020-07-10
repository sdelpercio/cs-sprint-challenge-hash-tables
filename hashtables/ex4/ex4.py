def has_negatives(a):
    num_cache = {}
    
    for num in a:
        # check positive numbers
        if num > 0:
            if int('-' + str(num)) in num_cache:
                num_cache[num] = 1
            else:
                num_cache[num] = 0
               
        # check negative numbers
        elif num < 0:
            if abs(num) in num_cache:
                num_cache[abs(num)] = 1
            else:
                num_cache[num] = 0
                
    return [k for k, v in num_cache.items() if v == 1]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
