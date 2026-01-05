import streamlit as st
from main import load_store_coords, plot_store_layout, find_shortest_path

st.title("Store Path Optimizer")

# load data
store_coords = load_store_coords()
valid_sections = set(store_coords.keys())

# ---------- session state ----------
if "shopping_items" not in st.session_state:
    # each item: {"section": str, "item": str}
    st.session_state.shopping_items = []

if "invalid_section" not in st.session_state:
    st.session_state.invalid_section = None

# ---------- inputs ----------
entrance = st.selectbox(
    "Starting Entrance",
    ["Entrance Left", "Entrance Right"]
)

items_input = st.text_input(
    "Items to pick up (format: Section: Item, Section: Item)",
    placeholder="A1: Apples, B3: Milk, C15: Bread"
)

if st.button("Submit Items"):
    parsed_items = []
    st.session_state.invalid_section = None

    for part in items_input.split(","):
        part = part.strip()
        if ":" not in part:
            st.session_state.invalid_section = part
            break

        section, item = part.split(":", 1)
        section = section.strip().upper()
        item = item.strip().title()

        if section not in valid_sections:
            st.session_state.invalid_section = section
            break

        parsed_items.append({"section": section, "item": item})

    if not st.session_state.invalid_section:
        st.session_state.shopping_items = parsed_items

# ---------- validation / replacement ----------
if st.session_state.invalid_section:
    st.error(
        f"Section '{st.session_state.invalid_section}' not found in store coordinates."
    )

    replacement = st.text_input(
        "Enter a valid section to visit:",
        key="replacement_input"
    )

    if st.button("Replace Section"):
        replacement = replacement.strip().upper()
        if replacement in valid_sections:
            for entry in st.session_state.shopping_items:
                if entry["section"] == st.session_state.invalid_section:
                    entry["section"] = replacement

            st.session_state.invalid_section = None
            st.rerun()
        else:
            st.warning("That section is also invalid. Please try again.")

# ---------- compute path ----------
elif st.session_state.shopping_items:
    sections = [entry["section"] for entry in st.session_state.shopping_items]

    path = find_shortest_path(
        entrance,
        sections,
        store_coords
    )

    st.subheader("Shortest Path")
    for step in path:
        matching_items = [
            entry["item"]
            for entry in st.session_state.shopping_items
            if entry["section"] == step
        ]

        if matching_items:
            for item in matching_items:
                st.write(f"🟦 **{step}** — {item}")
        else:
            st.write(f"➡️ **{step}**")

# ---------- plot ----------
st.subheader("Store Map")
fig = plot_store_layout(store_coords)
st.pyplot(fig)