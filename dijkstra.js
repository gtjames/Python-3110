function dijkstra(graph, startNode) {
    const distances = {};
    const visited = {};
    const priorityQueue = new Map();

    // Initialize distances
    for (let node in graph) {
        distances[node] = Infinity;
    }
    distances[startNode] = 0;

    // Add the start node to the priority queue
    priorityQueue.set(startNode, 0);

    while (priorityQueue.size > 0) {
        // Get the node with the smallest distance
        const [currentNode] = [...priorityQueue.entries()].reduce(
            (acc, entry) => (entry[1] < acc[1] ? entry : acc)
        );  

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
                    priorityQueue.set(neighbor, newDist);
                }
            }
        }
    }

    return distances;
}

// Example usage:
const graph = {
    A: { B: 1,  D: 5,  E: 1 },
    B: { C: 4,  D: 5 },
    C: { F: 2,  D: 5 },
    D: { G: 2 },
    E: { D:  5, G: 1 },
    G: { F: 1 },
    F: { A: 6, D: 1.1 }
};

const startNode = "A";
const distances = dijkstra(graph, startNode);
console.log("Shortest distances from", startNode, ":", distances);