import streamlit as st
from main import load_store_coords, plot_store_layout, find_shortest_path

st.title("Store Path Optimizer")

# load data
store_coords = load_store_coords()
valid_sections = set(store_coords.keys())

# session state
if "sections" not in st.session_state:
    st.session_state.sections = []

if "invalid_section" not in st.session_state:
    st.session_state.invalid_section = None

# inputs
entrance = st.selectbox(
    "Starting Entrance",
    ["Entrance Left", "Entrance Right"]
)

sections_input = st.text_input(
    "Sections to visit (comma-separated)",
    placeholder="A1, B3, C15"
)

if st.button("Submit Sections"):
    st.session_state.sections = [
        s.strip().title() for s in sections_input.split(",") if s.strip()
    ]
    st.session_state.invalid_section = None

# validation
for section in st.session_state.sections:
    if section not in valid_sections:
        st.session_state.invalid_section = section
        break

# invalid section replacement
if st.session_state.invalid_section:
    st.error(
        f"Section '{st.session_state.invalid_section}' not found in store coordinates."
    )

    replacement = st.text_input(
        "Enter a valid section to visit:",
        key="replacement_input"
    )

    if st.button("Replace Section"):
        if replacement.title() in valid_sections:
            idx = st.session_state.sections.index(
                st.session_state.invalid_section
            )
            st.session_state.sections[idx] = replacement.title()
            st.session_state.invalid_section = None
            st.rerun()
        else:
            st.warning("That section is also invalid. Please try again.")

# compute path
elif st.session_state.sections:
    path = find_shortest_path(
        entrance,
        st.session_state.sections,
        store_coords
    )

    st.subheader("Shortest Path")
    st.write(" → ".join(path))

# plot
st.subheader("Store Map")
fig = plot_store_layout(store_coords)
st.pyplot(fig)