import json
import matplotlib.pyplot as plt
from math import sqrt
from pathlib import Path

# data loading
BASE_DIR = Path(__file__).resolve().parent

def load_store_coords():
    with open(BASE_DIR / "data" / "store_coords.json", "r") as f:
        coords = json.load(f)
    return {k: tuple(v) for k, v in coords.items()}

# plotting
def plot_store_layout(coords, path=None):
    fig, ax = plt.subplots(figsize=(16, 10))

    # Plot all sections
    for section, (x, y) in coords.items():
        ax.scatter(x, y)
        ax.text(x + 0.5, y + 0.5, section, fontsize=6)

    # Draw path if provided
    if path:
        path_x = [coords[section][0] for section in path]
        path_y = [coords[section][1] for section in path]

        ax.plot(path_x, path_y, linewidth=2, linestyle='--')

        # Start marker
        ax.scatter(
            path_x[0], path_y[0],
            s=120, marker='o'
        )
        ax.text(path_x[0] + 1, path_y[0] + 1, "START", fontsize=9)

        # End marker (Checkout)
        ax.scatter(
            path_x[-1], path_y[-1],
            s=120, marker='X'
        )
        ax.text(path_x[-1] + 1, path_y[-1] + 1, "CHECKOUT", fontsize=9)

    ax.set_title("Store Layout with Optimized Path")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.grid(True)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 80)

    return fig

def distance(a, b, coords):
    return sqrt(
        (coords[a][0] - coords[b][0]) ** 2 +
        (coords[a][1] - coords[b][1]) ** 2
    )

# pathfinding
def find_shortest_path(start_entrance, section_list, store_coords, return_distance=False):
    path = []
    visited = set()
    current_section = start_entrance
    total_distance = 0.0

    remaining = section_list.copy()

    while remaining:
        distances = {
            section: distance(current_section, section, store_coords)
            for section in remaining
        }

        closest = min(distances, key=distances.get)
        total_distance += distances[closest]

        path.append(closest)
        visited.add(closest)
        remaining.remove(closest)
        current_section = closest

    # always end at Checkout
    total_distance += distance(current_section, "Checkout", store_coords)
    path.append("Checkout")

    if return_distance:
        return path, round(total_distance, 2)

    return path