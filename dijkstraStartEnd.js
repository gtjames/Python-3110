function dijkstra(graph, startNode, endNode) {
    const distances = {};
    const visited = {};
    const priorityQueue = new Map();
    const previous = {};

    // Initialize distances and previous
    for (let node in graph) {
        distances[node] = Infinity;
        previous[node] = null;
    }
    distances[startNode] = 0;

    // Add the start node to the priority queue
    priorityQueue.set(startNode, 0);

    while (priorityQueue.size > 0) {
        // Get the node with the smallest distance
        const [currentNode] = [...priorityQueue.entries()].reduce(
            (acc, entry) => (entry[1] < acc[1] ? entry : acc)
        );

        // If we reached the end node, stop
        if (currentNode === endNode) break;

        // Remove the node from the priority queue
        priorityQueue.delete(currentNode);

        // Mark the node as visited
        visited[currentNode] = true;

        // Update distances for neighboring nodes
        for (let neighbor in graph[currentNode]) {
            if (!visited[neighbor]) {
                const newDist = distances[currentNode] + graph[currentNode][neighbor];
                if (newDist < distances[neighbor]) {
                    distances[neighbor] = newDist;
                    previous[neighbor] = currentNode;
                    priorityQueue.set(neighbor, newDist);
                }
            }
        }
    }

    // Reconstruct the shortest path
    const path = [];
    let currentNode = endNode;
    while (currentNode) {
        path.unshift(currentNode);
        currentNode = previous[currentNode];
    }

    return {
        distance: distances[endNode],
        path: distances[endNode] !== Infinity ? path : null
    };
}

// Example usage:
const graph = {
    A: { B: 4, C: 2 },
    B: { A: 4, C: 1, D: 5 },
    C: { A: 2, B: 1, D: 8, E: 10 },
    D: { B: 5, C: 8, E: 2 },
    E: { C: 10, D: 2 }
};

const startNode = "A";
const endNode = "E";
const result = dijkstra(graph, startNode, endNode);

if (result.path) {
    console.log(`Shortest path from ${startNode} to ${endNode}:`, result.path);
    console.log(`Distance: ${result.distance}`);
} else {
    console.log(`No path found from ${startNode} to ${endNode}`);
}