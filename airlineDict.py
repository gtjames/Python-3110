import sys
import heapq

def addEdge(routes, from_node, to_node, weight):
    if from_node not in routes:
        routes[from_node] = []
    routes[from_node][to_node] = weight

def findQuickestRoute(routes, start, end):
    # Min-heap priority queue for Dijkstra's algorithm
    priorityQueue = [(0, start, [])]  # (current time, current airport, path)
    visited = set()

    while priorityQueue:
        # Get the current shortest route
        routeTime, currentAirport, path = heapq.heappop(priorityQueue)

        # Have we reached the destination?
        if currentAirport == end:
            return routeTime, path + [currentAirport]

        # Skip if this node has already been visited
        if currentAirport in visited:
            continue

        # Note this airport as now visited
        path = path + [currentAirport]
        visited.add(currentAirport)

        # Explore neighbors
        for neighbor, timeToDest in routes.get(currentAirport, {}).items():
            print(f"{neighbor} - {timeToDest}")
            if neighbor not in visited:                                
                heapq.heappush(priorityQueue, (routeTime + timeToDest, neighbor, path))
                print(f"    {priorityQueue}")

    return float('inf'), []  # If no route exists

# Add airline paths (routes) with weights (distances or times)

#   set this up for two routes for ATL to LAX
#   ATL -> DFW -> DEN -> LAX    8 9 29      46
#   ATL -> ORD -> PHX -> LAX    105 2 120   227
#   ATL -> PHX -> LAX           168 120     288
routes = {
    'ATL': {'DFW':   8, 'ORD': 105, 'PHX': 168},
    'DFW': {'DEN':   9, 'ATL': 419, 'ORD': 120},
    'DEN': {'LAX':  29, 'ORD': 243, 'ATL': 304},
    'LAX': {'DFW': 100, 'ATL': 328},

    'ORD': {'PHX':   2, 'DEN': 206, 'DFW': 255},
    'PHX': {'LAX': 120},
} 

# Add airline paths (routes) with weights (distances or times)
# addEdge(routes, "SLC", "LAX", 5)

# Main program to handle command-line arguments
if len(sys.argv) == 3:
    start = sys.argv[1].upper()
    end = sys.argv[2].upper()
else:
    start = input("Enter the start city: ").upper()
    end = input("Enter the end city: ").upper()

if start not in routes or end not in routes:
    print("Error: Start or end city is not in the list of available cities.")
    sys.exit(1)

time, route = findQuickestRoute(routes, start, end)
if route:
    print(f"Quickest route from {start} to {end} takes {time} hours: {' -> '.join(route)}")
else:
    print(f"No route found from {start} to {end}.")
