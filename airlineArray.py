import heapq

def add_edge(routes, from_node, to_node, weight):
    if from_node not in routes:
        routes[from_node] = []
    routes[from_node].append({to_node: weight})

def find_quickest_route(routes, start, end):
    # Min-heap priority queue for Dijkstra's algorithm
    priority_queue = [(0, start, [])]  # (current time, current airport, path)
    visited = set()

    while priority_queue:
        current_time, current_airport, path = heapq.heappop(priority_queue)

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
    "CZM": [ {"DFW": 273},  {"STT": 118},    {"AXA": 128},   {"CDG": 269}, {"LAS": 251},  {"BRU": 87}],
    "TUL": [ {"CDG": 209},  {"LAS": 288},    {"LGA": 257},   {"BRU": 291}, ],
    "CDG": [ {"SLC": 168},  {"AXA": 217},    {"DFW": 218},   {"TUL": 83 }, {"LAS": 279}  ],
    "BRU": [ {"LAS": 245},  {"CDG": 123},    {"SLC": 299},   {"NYC": 193}, {"LAX": 259},  {"AMS": 110}    ],
    "AMS": [ {"LGA": 193},  {"BRU": 33 },    {"STT": 292},   {"AUS": 137}, ],
    "LAS": [ {"AUS": 168},  {"AMS": 138},    {"MIA": 161},   {"NYC": 200}, {"CZM": 152}  ],
    "STT": [ {"AXA": 37},   {"TUL": 113},    {"AUS": 97 },   {"LGA": 101}, {"AMS": 163}  ],
    "AXA": [ {"NYC": 123},  {"AUS": 75 },    {"BRU": 252},   {"LGA": 226}, ],
    "AUS": [ {"LAS": 149},  {"MIA": 289},    {"AMS": 263},   {"CDG": 151}, ],
    "LAX": [ {"CDG": 218},  {"CZM": 47 },    {"SLC": 262},   {"DFW": 296}, {"AMS": 99}, {"TUL": 53}    ],
    "DFW": [ {"BRU": 61},   {"LAX": 130},    {"SLC": 72 },   {"AXA": 259}, {"CZM": 75}, {"MIA": 270}   ],
    "SLC": [ {"NYC": 155},  {"MIA": 49 },    {"CDG": 43 },   {"LAS": 267}, ],
    "NYC": [ {"STT": 39},   {"LGA": 179},    {"SLC": 68 },   {"DFW": 151}, ],
    "LGA": [ {"CZM": 222},  {"AMS": 31 },    {"SLC": 244},   {"AUS": 213}, {"MIA": 181}  ],
    "MIA": [ {"DFW": 150},  {"AUS": 213},    {"CDG": 220},   {"BRU": 106}, {"AXA": 260}  ]
}

# Add airline paths (routes) with weights (distances or times)
add_edge(routes, "SLC", "LAX", 5)

start = "SLC"
end = "LAX"
time, route = find_quickest_route(routes, start, end)
if route:
    print(f"Quickest route from {start} to {end} takes {time} hours: {' -> '.join(route)}")
else:
    print(f"No route found from {start} to {end}.")