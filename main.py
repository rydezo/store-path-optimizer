# import matplotlib for coordinate data visualization and sqrt function for distance calculation
import matplotlib.pyplot as plt
from math import sqrt

# store coordinates for each section in the store
store_coords = {

# ---------- A (Grocery Wall) ----------
"A1": (72, 18), "A3": (72, 20), "A5": (72, 22), "A7": (72, 24),
"A9": (72, 26), "A11": (72, 28), "A13": (72, 30), "A15": (72, 32),
"A17": (72, 34), "A19": (72, 36), "A21": (72, 38), "A23": (72, 40),
"A25": (72, 42), "A27": (72, 44), "A29": (72, 46),

# ---------- B (Women) ----------
"B5": (55, 14), "B7": (57, 14), "B9": (59, 14),
"B11": (61, 14), "B13": (63, 14), "B15": (65, 14),

# ---------- C (Mens / Intimates) ----------
"C1": (60, 20), "C3": (58, 20), "C5": (56, 20), "C7": (54, 20),
"C9": (52, 20), "C11": (50, 20), "C13": (48, 20),
"C15": (46, 20), "C17": (44, 20),

# ---------- D (Boys / Girls) ----------
"D1": (60, 24), "D3": (58, 24), "D5": (56, 24), "D7": (54, 24),
"D9": (52, 24), "D11": (50, 24), "D13": (48, 24),
"D15": (46, 24), "D17": (44, 24), "D19": (42, 24),
"D21": (40, 24), "D23": (38, 24), "D25": (36, 24),
"D27": (34, 24), "D29": (32, 24),

# ---------- E (Baby / Paper / Cleaning) ----------
"E1": (66, 26), "E3": (66, 28), "E5": (66, 30),
"E7": (66, 32), "E9": (66, 34), "E11": (66, 36),
"E13": (66, 38), "E15": (66, 40), "E17": (66, 42),
"E19": (66, 44),

# ---------- F (Seasonal / Party / Clearance) ----------
"F3": (46, 12), "F5": (48, 12), "F7": (50, 12),
"F9": (52, 12), "F11": (54, 12), "F13": (56, 12),
"F15": (58, 12), "F17": (60, 12), "F19": (62, 12),

# ---------- G (Health / Beauty) ----------
"G3": (40, 8), "G5": (42, 8), "G7": (44, 8),
"G9": (46, 8), "G11": (48, 8), "G13": (50, 8),
"G15": (52, 8), "G17": (54, 8),

# ---------- H (Home / Kitchen / Laundry) ----------
"H1": (30, 14), "H3": (30, 16), "H5": (30, 18),
"H7": (30, 20), "H9": (30, 22), "H11": (30, 24),
"H13": (30, 26), "H15": (30, 28), "H17": (30, 30),

# ---------- I (Toys / Sports) ----------
"I5": (18, 18), "I7": (18, 20), "I9": (18, 22),
"I11": (18, 24), "I13": (18, 26), "I15": (18, 28),
"I17": (18, 30),

# ---------- J (Shoes / Pet) ----------
"J7": (56, 40), "J9": (58, 40), "J11": (60, 40),
"J13": (62, 40), "J15": (64, 40), "J17": (66, 40),

# ---------- K (Electronics) ----------
"K3": (36, 46), "K5": (38, 46), "K7": (40, 46),
"K9": (42, 46), "K11": (44, 46), "K13": (46, 46),
"K15": (48, 46), "K17": (50, 46), "K19": (52, 46),
"K21": (54, 46),

# ---------- L (Paint / Hardware) ----------
"L3": (20, 48), "L5": (22, 48), "L7": (24, 48),
"L9": (26, 48), "L11": (28, 48), "L13": (30, 48),
"L15": (32, 48), "L17": (34, 48), "L19": (36, 48),
"L21": (38, 48), "L23": (40, 48),

# ---------- Y (Garden) ----------
"Y3": (10, 6), "Y5": (12, 6), "Y7": (14, 6),
"Y9": (9, 15), "Y11": (1, 1), "Y13": (17, 5), # done
"Y15": (15, 6), "Y17": (24, 6), "Y19": (26, 6),
"Y21": (28, 6), "Y23": (30, 6), "Y25": (32, 6)
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