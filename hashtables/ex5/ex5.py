# Your code here



def finder(files, queries):
    # start cache of queries
    # start matches list
    query_cache = {}
    matches =  []
    
    # loop through queries, add all to cache
    for query in queries:
        if query not in query_cache:
            query_cache[query] = 1
            
    # loop through paths, if the end matches a query, add to match list
    for f in files:
        stripped = f.split("/")[-1]
        if stripped in query_cache:
            matches.append(f)

    return matches

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
