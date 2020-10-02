#  Hint:  You may not need all of these.  Remove the unused functions.

"""
`source` string = starting airport 
`destination` string = next airport along our trip
first flight = destination, `source` of`NONE`
final flight = source, destination of None

starting location is the key (source)
the destination is the value
 
"""
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    set up store for tickets source as key, dest as values
    first and last are none
    """
    store = {}
    for item in tickets:
        store[item.source] = item.destination
    
    current = store["NONE"]
    route = [current]

    while current != "NONE":
        current = store[current]
        route.append(current)


    return route

