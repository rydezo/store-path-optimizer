import json
import matplotlib.pyplot as plt
from math import sqrt
from pathlib import Path

# ---------- data loading ----------
BASE_DIR = Path(__file__).resolve().parent

def load_store_coords():
    with open(BASE_DIR / "data" / "store_coords.json", "r") as f:
        coords = json.load(f)
    return {k: tuple(v) for k, v in coords.items()}

# ---------- plotting ----------
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

# ---------- pathfinding ----------
def find_shortest_path(start_entrance, section_list, store_coords):
    path = []
    visited = set()
    current_section = start_entrance

    # Remove invalid sections safely
    section_list = [s for s in section_list if s in store_coords]

    while len(path) < len(section_list):
        distances = {}

        for section in section_list:
            if section in visited:
                continue

            distance = sqrt(
                (store_coords[current_section][0] - store_coords[section][0]) ** 2 +
                (store_coords[current_section][1] - store_coords[section][1]) ** 2
            )
            distances[section] = distance

        if not distances:
            break

        closest_section = min(distances, key=distances.get)
        path.append(closest_section)
        visited.add(closest_section)
        current_section = closest_section

    path.append("Checkout")
    return path