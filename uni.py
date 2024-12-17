import streamlit as st
import pandas as pd

# Streamlit app
def main():
    st.title("CSV Upload and Data Filtering")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Load CSV into a DataFrame
            df = pd.read_csv(uploaded_file)

            # Display basic file details
            st.write(f"### File Details:")
            st.write(f"Rows: {len(df)}")
            st.write(f"Columns: {len(df.columns)}")

            # Display full DataFrame
            st.write("### Full Data Table:")
            st.dataframe(df)

            # Filtering interface
            st.write("### Filter Data")

            # Dropdown to select column for filtering
            filter_column = st.selectbox("Select a column to filter by:", df.columns)

            if filter_column:
                # Dropdown for unique values in the selected column
                unique_values = df[filter_column].dropna().unique()
                filter_value = st.selectbox(f"Select a value from '{filter_column}'", unique_values)

                if filter_value:
                    # Filter the DataFrame
                    filtered_df = df[df[filter_column] == filter_value]

                    # Display filtered data
                    st.write(f"### Filtered Data (Rows: {len(filtered_df)})")
                    st.dataframe(filtered_df)

        except Exception as e:
            st.error(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()

