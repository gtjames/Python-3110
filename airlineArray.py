import heapq
from collections import namedtuple

def addEdge(routes, from_node, to_node, weight):
    if from_node not in routes:
        routes[from_node] = []
    routes[from_node].append({to_node: weight})

def addPath(routes, to_node, path, time):
    if to_node not in routes:
        routes[to_node] = []
    routes[to_node].append({time: time, path: path})

def findQuickestRoute(routes, start, end):
    # Min-heap priority queue for Dijkstra's algorithm
    priority_queue = [(0, start, [])]  # (current time, current airport, path)
    visited = set()
    paths = {}
    
    while priority_queue:
        current_time, current_airport, path = heapq.heappop(priority_queue)
        addPath(paths, current_airport, path, current_time)

        # If we reach the destination
        if current_airport == end:
            return current_time, path + [current_airport]

        # Skip if this node has already been visited
        if current_airport in visited:
            continue
        path = path + [current_airport]
        visited.add(current_airport)

        # Explore neighbors
        for rt in routes.get(current_airport, []):
            neighbor, weight = list(rt.items())[0]
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_time + weight, neighbor, path))
    return float('inf'), []  # If no route exists

# Add airline paths (routes) with weights (distances or times)
routes = {
    "TUL": [ {"CDG": 79},   {"LAS":  28},    {"LGA":  25},   {"BRU":  29}, ],
    "CDG": [ {"SLC": 68},   {"AXA":  21},    {"DFW":  21},   {"TUL":  83}, {"LAS": 79}  ],
    "BRU": [ {"LAS": 45},   {"CDG":  12},    {"SLC":  29},   {"NYC":  19}, {"LAX": 59},  {"AMS": 10}    ],
    "AMS": [ {"LGA": 93},   {"BRU":  33},    {"STT":  29},   {"AUS":  13}, ],
    "LAS": [ {"AUS": 68},   {"AMS":  13},    {"MIA":  16},   {"NYC":  20}, {"CZM": 52}  ],
    "STT": [ {"AXA": 37},   {"TUL":  11},    {"AUS":  97},   {"LGA":  10}, {"AMS": 63}  ],
    "AXA": [ {"NYC": 23},   {"AUS":  75},    {"BRU":  25},   {"LGA":  22}, ],
    "AUS": [ {"LAS": 49},   {"MIA":  28},    {"AMS":  26},   {"CDG":  15}, ],
    "LAX": [ {"CDG": 18},   {"CZM":  47},    {"SLC":  26},   {"DFW":  29}, {"AMS":  99}, {"TUL": 53}   ],
    "DFW": [ {"BRU": 61},   {"LAX":  13},    {"SLC":  72},   {"AXA":  25}, {"CZM":  75}, {"MIA": 70}   ],
    "SLC": [ {"NYC": 55},   {"MIA":  49},    {"CDG":  43},   {"LAS":  26}, ],
    "NYC": [ {"STT": 39},   {"LGA":  17},    {"SLC":  68},   {"DFW":  15}, ],
    "LGA": [ {"CZM": 22},   {"AMS":  31},    {"SLC":  24},   {"AUS":  21}, {"MIA": 81}  ],
    "MIA": [ {"DFW": 50},   {"AUS":  21},    {"CDG":  22},   {"BRU":  10}, {"AXA": 60}  ]
}

# Add airline paths (routes) with weights (distances or times)
addEdge(routes, "SLC", "DFW", 5)

start = "TUL"
end = "DFW"
time, route = findQuickestRoute(routes, start, end)
if route:
    print(f"Quickest route from {start} to {end} takes {time} hours: {' -> '.join(route)}")
else:
    print(f"No route found from {start} to {end}.")