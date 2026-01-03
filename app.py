import streamlit as st
from main import plot_store_layout, store_coords

fig = plot_store_layout(store_coords)

st.title('Store Map')
st.pyplot(fig)