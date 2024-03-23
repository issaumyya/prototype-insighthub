import streamlit as st
border_style = """
<style>
  .stContainer[data-testid="stColumn"][data-index="0"] {
    border: 2px solid #007bff;
    padding: 10px;
    border-radius: 5px;
  }
</style>
"""

# Display the CSS styles
st.markdown(border_style, unsafe_allow_html=True)
# Create initial columns with desired ratio (3:1:1)
col1, col2, col3 = st.columns([3, 1, 1])

# Create a container within the first column
with col1:
  nested_container = st.container()

# Create nested columns inside the container (visually appears within col1)
nested_col1, nested_col2, nested_col3 = nested_container.columns(3)

# Add content to columns and nested columns
with col2:
  st.write("Content in Column 2")

with col3:
  st.write("Content in Column 3")

with nested_col1:
  st.write("Nested Content 1")

with nested_col2:
  st.write("Nested Content 2")

with nested_col3:
  st.write("Nested Content 3")
