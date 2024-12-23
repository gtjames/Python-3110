import random

# List of 20 airport codes
airports = [
    "ATL", "LAX", "ORD", "DFW", "DEN"
#  "JFK", "SFO", "SEA", "LAS", "MIA", "SLC",
#  "PHX", "IAH", "CLT", "EWR", "MSP", "BOS", "DTW", "FLL", "BWI", "DCA", "ABQ"
]

# Generate routes
routes = {}
for airport in airports:
    # Randomly select 5-7 other airports as connections
    connections = random.sample([a for a in airports if a != airport], random.randint(3, 4))
    # Assign a random travel time (in minutes) to each connection
    routes[airport] = {conn: random.randint(100, 420) for conn in connections}

# Print routes
print("routes = {")
for airport, connections in routes.items():
    print(f"    '{airport}': {connections},")
print("}")
