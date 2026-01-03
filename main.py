import json
import matplotlib.pyplot as plt
from math import sqrt

# store coordinates for each section in the store
with open("data/store_coords.json", "r") as f:
    store_coords = json.load(f)

# convert back to tuple
store_coords = {k: tuple(v) for k, v in store_coords.items()}

# plot the store layout
def plot_store_layout(coords):
    fig, ax = plt.subplots(figsize=(16, 10))

    for section, (x, y) in coords.items():
        ax.scatter(x, y, label=section)
        ax.text(x + 0.01, y + 0.01, section, fontsize=6)

    ax.set_title("Store Layout")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.grid(True)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)

    return fig

# find shortest path
def find_shortest_path(start_entrance, section_list):
    path = []
    visited = set()
    current_section = start_entrance
    while len(path) < len(section_list):
        distances = dict()
        for section in section_list:
            # check if section has not been visited and exists in store coordinates
            if section in visited:
                continue
            if section not in store_coords:
                print(f"Section '{section}' not found in store coordinates. Please input your section again.")
                section_list.remove(section)
                new_section = input("Enter a valid section to visit: ").strip()
                section_list.append(new_section.title())
                continue
            # use distance formula to calculate distance between sections
            distance = sqrt(
                (store_coords[current_section][0] - store_coords[section][0]) ** 2 +
                (store_coords[current_section][1] - store_coords[section][1]) ** 2
            )
            distances[section] = distance
        # find the closest section
        if distances:
            closest_section = min(distances, key=distances.get)
            path.append(closest_section)
            current_section = closest_section
            visited.add(current_section)

    path.append("Checkout")  # always end at Checkout
    return path

# get user input and find the shortest path
start = input("Enter starting entrance ('Left' or 'Right'): ")
start = start.strip().title()
sections = input("Enter sections to visit (comma-separated): ").split(',')
sections = [section.strip() for section in sections]

shortest_path = find_shortest_path('Entrance Left' if start == 'Left' else 'Entrance Right', [section.title() for section in sections])
print("Shortest path:", shortest_path)