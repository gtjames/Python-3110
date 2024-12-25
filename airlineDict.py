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
            if neighbor not in visited:                                
                heapq.heappush(priorityQueue, (routeTime + timeToDest, neighbor, path))

    return float('inf'), []  # If no route exists

# Add airline paths (routes) with weights (distances or times)
# addEdge(routes, "SLC", "LAX", 5)
routes = {
    'ATL': {'EWR': 22, 'MSP': 22, 'FLL': 26, 'DTW': 18, 'CLT': 25, 'DCA': 22, 'LAX': 10},
    'LAX': {'DCA': 21, 'BOS': 26, 'SEA': 14, 'CLT': 13, 'DEN': 22, 'SLC': 20, 'LAS': 20},
    'ORD': {'SFO': 19, 'PHX': 19, 'FLL': 27, 'BWI': 29, 'MSP': 11, 'BOS': 26},
    'DFW': {'JFK': 17, 'CLT': 28, 'MSP': 13},
    'DEN': {'BOS': 23, 'SFO': 20, 'JFK': 24, 'DCA': 16, 'ORD': 29},
    'JFK': {'SFO': 14, 'DEN': 16, 'BOS': 12, 'PHX': 29},
    'SFO': {'SEA': 17, 'MIA': 22},
    'SEA': {'BWI': 11, 'ORD': 13, 'LAX': 13, 'CLT': 18, 'DTW': 30},
    'LAS': {'SFO': 28, 'PHX': 18, 'MIA': 19},
    'MIA': {'DFW': 10, 'DTW': 30},
    'SLC': {'MSP': 12, 'SEA': 26, 'IAH': 22, 'DFW': 15},
    'PHX': {'ABQ': 25, 'SEA': 15},
    'IAH': {'SLC': 29, 'MSP': 28},
    'CLT': {'BOS': 16, 'SLC': 15},
    'EWR': {'JFK': 14, 'BWI': 11, 'SFO': 13},
    'MSP': {'DFW': 12, 'DCA': 10, 'IAH': 30, 'SLC': 20, 'ATL': 25},
    'BOS': {'EWR': 25, 'PHX': 22, 'ORD': 28},
    'DTW': {'DFW': 28, 'ATL': 26, 'ORD': 12, 'DCA': 13, 'PHX': 30},
    'FLL': {'SEA': 17, 'EWR': 27, 'LAX': 19, 'MSP': 12, 'SFO': 24},
    'BWI': {'ATL': 28, 'SFO': 13, 'LAS': 14},
    'DCA': {'DEN': 11, 'SEA': 19, 'PHX': 23},
    'ABQ': {'ORD': 24, 'SLC': 27, 'LAS': 14, 'DEN': 14, 'JFK': 10, 'BWI': 24},
}
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
