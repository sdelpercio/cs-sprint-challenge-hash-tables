def get_indices_of_item_weights(weights, length, limit):
    # create cache
    cache = {}
    
    # loop through weights
    for index, weight in enumerate(weights):
        ## otherwise check for match
        if limit - weight in cache:
            if index < cache[limit - weight]:
                return (cache[limit - weight], index)
            else:
                return (index, cache[limit - weight])
            
        cache[weight] = index

    return None
