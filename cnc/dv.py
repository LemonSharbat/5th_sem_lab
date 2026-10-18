INF = 999


def distance_vector(cost):
    n = len(cost)

    # Initially, final table is same as direct-link table
    distance = [row[:] for row in cost]

    # Store the next router to take
    via = [[j if cost[i][j] != INF else -1
            for j in range(n)] for i in range(n)]

    # Repeatedly update the routing tables
    for _ in range(n - 1):
        changed = False

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    if distance[i][k] != INF and cost[k][j] != INF:
                        new_cost = distance[i][k] + cost[k][j]

                        if new_cost < distance[i][j]:
                            distance[i][j] = new_cost
                            via[i][j] = via[i][k]
                            changed = True

        if not changed:
            break

    return distance, via


def display_table(distance, via):
    n = len(distance)

    for i in range(n):
        print(f"\nRouting Table for {chr(65 + i)}")
        print("Destination\tCost\tVia")

        for j in range(n):
            if via[i][j] == -1:
                next_hop = "-"
            else:
                next_hop = chr(65 + via[i][j])

            print(f"{chr(65 + j)}\t\t{distance[i][j]}\t{next_hop}")


def find_path(src, dst, via):
    path = [src]

    while src != dst:
        src = via[src][dst]
        path.append(src)

    return " --> ".join(chr(65 + node) for node in path)


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of routers: "))

print("\nEnter the initial routing table.")
print("Enter 999 if there is no direct connection.\n")

cost = []

for i in range(n):
    print(f"Router {chr(65 + i)}:")
    row = list(map(int, input().split()))
    cost.append(row)

distance, via = distance_vector(cost)

display_table(distance, via)

# Find shortest path
while True:
    src = int(input("\nEnter source router (0 to n-1): "))
    dst = int(input("Enter destination router (0 to n-1): "))

    print("Path:", find_path(src, dst, via))
    print("Cost:", distance[src][dst])

    choice = input("\nContinue? (Y/N): ").upper()

    if choice != "Y":
        break