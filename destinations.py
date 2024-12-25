import sys
import random

# Main program to handle command-line arguments
if len(sys.argv) == 2:
    cnt = int(sys.argv[1])
else:
    cnt = int(input("Enter the nujmber of cities: "))

# List of 20 airport codes
airports = [
    "ATL", "LAX", "ORD", "DFW", "DEN", "JFK", "SFO", "SEA", "LAS", "MIA", "SLC",
    "PHX", "IAH", "CLT", "EWR", "MSP", "BOS", "DTW", "FLL", "BWI", "DCA", "ABQ"
]

# Generate routes
routes = {}
for airport in airports:
    # Randomly select 5-7 other airports as connections
    connections = random.sample([a for a in airports if a != airport], random.randint(cnt-3, cnt+2))
    # Assign a random travel time (in minutes) to each connection
    routes[airport] = {conn: random.randint(10, 30) for conn in connections}

# Print routes
    # 'ATL':   {'EWR': 22, 'MSP': 22, 'FLL': 26, 'DTW': 18, 'CLT': 25, 'DCA': 22, 'LAX': 10},
print("routes = {")
for airport, connections in routes.items():
    print(f"    '{airport}': {connections},")

#not yet ready
    # "CZM": [ {"DFW": 273},  {"STT": 118},    {"AXA": 128},   {"CDG": 269}, {"LAS": 251},  {"BRU": 87}],

print("}")
