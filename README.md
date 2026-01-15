# Store Path Optimizer

A **Streamlit web app** that helps shoppers minimize walking distance in the Elkton Walmart Supercenter by computing and visualizing an efficient path through selected aisles. The app supports **entrance comparison**, **aisle autocompletion**, and **interactive map visualization**.

---

## Features

* **Interactive store map** rendered with Matplotlib
* **Greedy shortest-path routing** through selected aisles
* **Compare total walking distance** from *Entrance Left* vs *Entrance Right*
* Always ends at **Checkout**
* Flexible input: `A1` or `A1: Milk`
* **Autocomplete dropdown** for invalid aisle correction
* Visual path overlay starting at the selected entrance
* Deployed on **Streamlit Community Cloud**

---

## How It Works

1. User selects a starting entrance
2. User inputs a list of aisles (optionally with item names)
   * The aisles can be found by searching the desired items in the Walmart mobile app
4. The app:

   * Validates aisle IDs
   * Computes an efficient visiting order using Euclidean distance
   * Calculates total distance for **both entrances**
   * Visualizes the selected route on the store map

> The routing logic is greedy (nearest-neighbor), designed for clarity and speed rather than perfect optimality.


## Try it Out
https://store-path.streamlit.app/

---

## Local Development

### 1️⃣ Clone the repo

```bash
git clone https://github.com/rydezo/store-path-optimizer
cd store-path-optimizer
```

### 2️⃣ Install dependencies (Poetry)

```bash
poetry install
```

Or, if you prefer pip:

```bash
pip install streamlit matplotlib
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## Configuration Notes

* Store layout is defined in `data/store_coords.json`
* Coordinates use arbitrary units (consistent scale)
* Paths are rendered dynamically using Matplotlib
* JSON is loaded safely using `pathlib`

---

## Tech Stack

* **Python 3.10+**
* **Streamlit** – UI & deployment
* **Matplotlib** – Visualization
* **Poetry** – Dependency management

---

## Possible Enhancements

* Animated walking path
* Auto-select shortest entrance
* Arrowed routes / step numbers
* Mobile-optimized layout
* Save/share shopping routes

---

## License

MIT License

---

## Acknowledgments

Built as a learning-focused project combining:

* Algorithmic thinking
* Data visualization
* Practical UI deployment

I made this app to address a real-world problem I had. I would often spend much time going from aisle to aisle in my local Walmart, confused about where in the store to go next and where I had already been. This app attempts to solve that problem by providing clarity on which path to take in the store through the concise list of aisles and a plotted path for visualization.
