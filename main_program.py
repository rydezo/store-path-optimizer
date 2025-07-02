# import matplotlib for coordinate data visualization and sqrt function for distance calculation
import matplotlib.pyplot as plt
from math import sqrt

# store coordinates for each section in the store
store_coords = {
    # blue sections
    "Entrance Left": (6, 0),
    "Entrance Right": (14, 0),
    "Checkout": (10, 2),
    "Outdoor": (2, 2),
    "Personal Care & Beauty": (4, 2),
    "Pharmacy": (6, 2),
    "Tools & Hardware": (4, 3),
    "Auto Accessories": (4, 6),
    "Auto Care Center": (3, 7),
    "Kitchen & Dining": (6, 3),
    "Bath Storage & Laundry": (6, 5),
    "Furniture & Bedding": (6, 6),
    "Home": (6, 7),
    "Sports & Outdoors": (4, 8),
    "Toys & Games": (6, 8),
    "Electronics": (8, 8),
    "Home Office": (10, 8),
    "Paper & Cleaning": (11, 8),
    "Pet Care": (12, 8),
    "Seasonal": (7, 3),
    "Celebrate": (7, 5),
    "Arts & Crafts": (7, 6),
    "Books": (7, 7),
    "Mens": (9, 3),
    "Ladies": (12, 3),
    "Shoes": (9, 5),
    "Boys": (9, 6),
    "Girls": (10, 6),
    "Baby": (12, 6),

    # green sections
    "Bakery": (14, 3),
    "Fresh Produce": (15, 3),
    "Frozen": (14, 4),
    "Meat": (16, 5),
    "Grocery": (14, 5),
    "Candy": (14, 6),
    "Snacks": (14, 7),
    "Deli": (16, 7),
    "Adult Beverages": (14, 8),
    "Dairy": (14, 9),

    # yellow sections
    "Vision Center": (8, 1),
    "Restrooms (Entrance)": (9, 1),
    "Customer Center": (10, 1),
    "Tenant": (11, 1),
    "Hair Salon": (12, 1),
}

# plot the store layout
def plot_store_layout(coords):
    plt.figure(figsize=(12, 8))
    for section, (x, y) in coords.items():
        plt.scatter(x, y, label=section)
        plt.text(x + 0.1, y + 0.1, section, fontsize=8)

    plt.title("Store Layout")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
    plt.xlim(0, 20)
    plt.ylim(-1, 10)
    plt.show()

plot_store_layout(store_coords)

# find shortest path
def find_shortest_path(start_entrance, section_list):
    path = []
    visited = {}
    current_section = start_entrance
    for section in section_list:
        distance = sqrt(
            (store_coords[current_section][0] - store_coords[section][0]) ** 2 +
            (store_coords[current_section][1] - store_coords[section][1]) ** 2
        )


# potential deque algorithm
'''
def find_shortest_path(start_entrance, section_list):
    from collections import deque

    # BFS to find shortest path
    queue = deque([(start_entrance, [start_entrance])])
    visited = {}

    while queue:
        current_section, path = queue.popleft()
        if current_section in section_list:
            return path
        
        visited.add(current_section)

        for neighbor in store_coords.keys():
            if neighbor not in visited and neighbor != current_section:
                queue.append((neighbor, path + [neighbor]))

    return None
'''