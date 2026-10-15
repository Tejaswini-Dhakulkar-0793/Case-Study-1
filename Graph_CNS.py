
from collections import deque

# College campus graph
campus = {
    "Main Gate": ["Library", "Canteen"],
    "Library": ["Main Gate", "Classroom", "Hostel"],
    "Classroom": ["Library", "Laboratory"],
    "Laboratory": ["Classroom", "Canteen"],
    "Canteen": ["Main Gate", "Laboratory"],
    "Hostel": ["Library"]
}

def find_route(source, destination):
    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        current = queue.popleft()

        if current == destination:
            break

        for neighbor in campus[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Check whether destination was reached
    if destination not in visited:
        print("No route found!")
        return

    # Reconstruct route
    route = []
    current = destination

    while current is not None:
        route.append(current)
        current = parent[current]

    route.reverse()

    print("\nShortest route:")
    print(" -> ".join(route))
    print("Number of pathways:", len(route) - 1)


# Display available locations
print("COLLEGE CAMPUS NAVIGATION SYSTEM")
print("Available locations:", ", ".join(campus.keys()))

source = input("\nEnter starting location: ").strip().title()
destination = input("Enter destination: ").strip().title()

if source not in campus or destination not in campus:
    print("Invalid location! Please enter a location from the list.")
else:
    find_route(source, destination)
