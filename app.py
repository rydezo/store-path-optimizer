import streamlit as st
from main import (
    load_store_coords,
    plot_store_layout,
    find_shortest_path
)

st.title("Store Path Optimizer")

# Load data
store_coords = load_store_coords()

# Sidebar inputs
st.sidebar.header("Navigation Settings")

entrance = st.sidebar.selectbox(
    "Starting Entrance",
    ["Entrance Left", "Entrance Right"]
)

sections_input = st.sidebar.text_input(
    "Sections to visit (comma-separated)",
    placeholder="Produce, Dairy, Bakery"
)

sections = [s.strip().title() for s in sections_input.split(",") if s.strip()]

# Compute path
if sections:
    path = find_shortest_path(entrance, sections, store_coords)
    st.subheader("Shortest Path")
    st.write(" → ".join(path))

# Plot store
st.subheader("Store Map")
fig = plot_store_layout(store_coords)
st.pyplot(fig)