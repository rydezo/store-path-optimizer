import streamlit as st
from main import load_store_coords, plot_store_layout, find_shortest_path

st.title("Store Path Optimizer")

# ---------- load data ----------
store_coords = load_store_coords()
valid_sections = sorted(store_coords.keys())

# ---------- session state ----------
if "shopping_items" not in st.session_state:
    # each entry: {"section": str, "item": str}
    st.session_state.shopping_items = []

if "invalid_index" not in st.session_state:
    st.session_state.invalid_index = None

# ---------- inputs ----------
entrance = st.selectbox(
    "Starting Entrance",
    ["Entrance Left", "Entrance Right"]
)

raw_input = st.text_input(
    "Items to pick up (Section or Section: Item)",
    placeholder="A1, B3: Milk, C15: Bread"
)

if st.button("Submit Items"):
    parsed = []
    st.session_state.invalid_index = None

    for part in raw_input.split(","):
        part = part.strip()
        if not part:
            continue

        # Split section and optional item
        if ":" in part:
            section, item = part.split(":", 1)
            item = item.strip().title()
        else:
            section = part
            item = "Item"

        parsed.append({
            "section": section.strip().upper(),
            "item": item
        })

    st.session_state.shopping_items = parsed

# ---------- aisle validation ----------
for idx, entry in enumerate(st.session_state.shopping_items):
    if entry["section"] not in valid_sections:
        st.session_state.invalid_index = idx
        break

# ---------- invalid aisle replacement (AUTOCOMPLETE) ----------
if st.session_state.invalid_index is not None:
    bad_entry = st.session_state.shopping_items[st.session_state.invalid_index]

    st.error(f"Aisle '{bad_entry['section']}' not found in store layout.")

    replacement = st.selectbox(
        "Select a valid aisle:",
        options=valid_sections,
        index=0
    )

    if st.button("Replace Aisle"):
        st.session_state.shopping_items[
            st.session_state.invalid_index
        ]["section"] = replacement

        st.session_state.invalid_index = None
        st.rerun()

# ---------- compute + render ----------
elif st.session_state.shopping_items:
    sections = [e["section"] for e in st.session_state.shopping_items]

    path = find_shortest_path(
        entrance,
        sections,
        store_coords
    )

    # ---- Shortest Path ----
    st.subheader("Shortest Path")
    for step in path:
        matching_items = [
            e["item"]
            for e in st.session_state.shopping_items
            if e["section"] == step
        ]

        if matching_items:
            for item in matching_items:
                st.write(f"🟦 **{step}** — {item}")
        else:
            st.write(f"➡️ **{step}**")

    # ---- Store Map ----
    st.subheader("Store Map")
    fig = plot_store_layout(store_coords, path)
    st.pyplot(fig)

# ---------- fallback ----------
else:
    st.subheader("Store Map")
    fig = plot_store_layout(store_coords)
    st.pyplot(fig)