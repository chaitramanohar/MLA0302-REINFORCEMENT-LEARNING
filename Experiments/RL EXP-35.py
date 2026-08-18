import numpy as np
import matplotlib.pyplot as plt
import random
import math

# ============================================================
# RRT BASED UAV SURVEILLANCE PATH PLANNING
# ============================================================

# Environment size
WIDTH = 100
HEIGHT = 100

# Start and goal positions
START = (10, 10)
GOAL = (90, 90)

# RRT parameters
STEP_SIZE = 4
MAX_ITERATIONS = 5000
GOAL_THRESHOLD = 5

# ------------------------------------------------------------
# Urban buildings / obstacles
# Format: (x, y, width, height)
# ------------------------------------------------------------

obstacles = [
    (20, 15, 15, 25),
    (45, 10, 20, 20),
    (75, 15, 15, 25),
    (10, 55, 20, 25),
    (40, 50, 15, 30),
    (70, 55, 20, 20)
]


# ------------------------------------------------------------
# Check whether a point is inside an obstacle
# ------------------------------------------------------------

def point_in_obstacle(point):

    x, y = point

    for ox, oy, w, h in obstacles:

        if ox <= x <= ox + w and oy <= y <= oy + h:
            return True

    return False


# ------------------------------------------------------------
# Check collision between two points
# ------------------------------------------------------------

def collision_free(p1, p2):

    distance = math.dist(p1, p2)

    steps = max(int(distance / 1), 1)

    for i in range(steps + 1):

        t = i / steps

        x = p1[0] + t * (p2[0] - p1[0])
        y = p1[1] + t * (p2[1] - p1[1])

        if point_in_obstacle((x, y)):
            return False

    return True


# ------------------------------------------------------------
# Generate random point
# ------------------------------------------------------------

def random_point():

    return (
        random.uniform(0, WIDTH),
        random.uniform(0, HEIGHT)
    )


# ------------------------------------------------------------
# Find nearest node in RRT
# ------------------------------------------------------------

def nearest_node(tree, point):

    distances = [
        math.dist(node, point)
        for node in tree
    ]

    return tree[np.argmin(distances)]


# ------------------------------------------------------------
# Steer from nearest node toward random point
# ------------------------------------------------------------

def steer(from_node, to_node):

    distance = math.dist(from_node, to_node)

    if distance <= STEP_SIZE:
        return to_node

    theta = math.atan2(
        to_node[1] - from_node[1],
        to_node[0] - from_node[0]
    )

    new_x = from_node[0] + STEP_SIZE * math.cos(theta)
    new_y = from_node[1] + STEP_SIZE * math.sin(theta)

    return (new_x, new_y)


# ------------------------------------------------------------
# RRT Algorithm
# ------------------------------------------------------------

def rrt():

    tree = [START]

    parent = {}

    for iteration in range(MAX_ITERATIONS):

        # Goal bias:
        # Occasionally sample the goal directly
        if random.random() < 0.10:
            sample = GOAL
        else:
            sample = random_point()

        # Find nearest node
        nearest = nearest_node(tree, sample)

        # Generate new node
        new_node = steer(nearest, sample)

        # Check boundaries
        if not (
            0 <= new_node[0] <= WIDTH and
            0 <= new_node[1] <= HEIGHT
        ):
            continue

        # Check obstacle collision
        if not collision_free(nearest, new_node):
            continue

        # Add new node
        tree.append(new_node)
        parent[new_node] = nearest

        # Check whether goal is reached
        if math.dist(new_node, GOAL) <= GOAL_THRESHOLD:

            if collision_free(new_node, GOAL):

                tree.append(GOAL)
                parent[GOAL] = new_node

                print("Goal reached!")
                print("Iterations:", iteration)

                return tree, parent

    print("Goal was not reached.")

    return tree, parent


# ------------------------------------------------------------
# Extract final path
# ------------------------------------------------------------

def extract_path(parent):

    if GOAL not in parent:
        return None

    path = [GOAL]

    current = GOAL

    while current != START:

        current = parent[current]

        path.append(current)

    path.reverse()

    return path


# ------------------------------------------------------------
# Calculate path length
# ------------------------------------------------------------

def path_length(path):

    total = 0

    for i in range(len(path) - 1):

        total += math.dist(
            path[i],
            path[i + 1]
        )

    return total


# ------------------------------------------------------------
# Generate surveillance points
# ------------------------------------------------------------

def surveillance_points(path, spacing=10):

    points = []

    accumulated = 0

    points.append(path[0])

    for i in range(len(path) - 1):

        p1 = np.array(path[i])
        p2 = np.array(path[i + 1])

        segment_length = np.linalg.norm(p2 - p1)

        direction = (p2 - p1) / segment_length

        distance = spacing

        while distance < segment_length:

            new_point = p1 + direction * distance

            points.append(tuple(new_point))

            distance += spacing

        accumulated += segment_length

    points.append(path[-1])

    return points


# ============================================================
# MAIN PROGRAM
# ============================================================

tree, parent = rrt()

path = extract_path(parent)

if path is None:

    print("No collision-free path found.")

else:

    # Calculate path length
    length = path_length(path)

    # Generate surveillance points
    coverage_points = surveillance_points(path)

    print("\n========== UAV SURVEILLANCE RESULTS ==========")

    print("Start Position :", START)
    print("Goal Position  :", GOAL)
    print("Path Nodes     :", len(path))
    print("Path Length    :", round(length, 2))
    print("Coverage Points:", len(coverage_points))

    # --------------------------------------------------------
    # Visualization
    # --------------------------------------------------------

    plt.figure(figsize=(10, 10))

    # Draw obstacles
    for ox, oy, w, h in obstacles:

        rectangle = plt.Rectangle(
            (ox, oy),
            w,
            h,
            fill=True,
            alpha=0.7
        )

        plt.gca().add_patch(rectangle)

    # Draw RRT tree
    for node in tree:

        if node in parent:

            p = parent[node]

            plt.plot(
                [p[0], node[0]],
                [p[1], node[1]],
                linewidth=0.5,
                alpha=0.3
            )

    # Convert path to arrays
    path_array = np.array(path)

    # Draw final UAV path
    plt.plot(
        path_array[:, 0],
        path_array[:, 1],
        linewidth=3,
        label="RRT UAV Path"
    )

    # Draw surveillance points
    coverage_array = np.array(coverage_points)

    plt.scatter(
        coverage_array[:, 0],
        coverage_array[:, 1],
        s=40,
        label="Surveillance Points"
    )

    # Start point
    plt.scatter(
        START[0],
        START[1],
        s=150,
        marker="o",
        label="UAV Start"
    )

    # Goal point
    plt.scatter(
        GOAL[0],
        GOAL[1],
        s=150,
        marker="*",
        label="Target"
    )

    # Labels
    plt.title(
        "RRT-Based UAV Surveillance Path Planning"
    )

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)

    plt.grid(True)
    plt.legend()

    plt.show()
