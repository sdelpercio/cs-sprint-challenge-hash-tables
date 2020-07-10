#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # start cache of tickets (key = source, value = destination)
    # start route list of size length
    ticket_cache = {}
    route = [None] * length
    
    # build cache
    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination
    
    next_dest = "NONE"
    for i in range(length):
        if i == 0:
            route[i] = ticket_cache[next_dest]
            next_dest = ticket_cache[route[i]]
            continue
            
        route[i] = next_dest
        next_dest = ticket_cache[route[i]]
        
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))