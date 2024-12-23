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
    A: { B: 6,  C: 2 },
    B: { A: 4,  C: 1, D: 1 },
    C: { A: 2,  F: 1, D: 8, E: 10 },
    D: { B: 5,  C: 8, E: 2 },
    E: { C: 10, D: 2 },
    F: { B: 1,  D: 2 }
};

const startNode = "A";
const distances = dijkstra(graph, startNode);
console.log("Shortest distances from", startNode, ":", distances);