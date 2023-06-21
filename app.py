pip install -r requirements.txt

import pandas as pd
import streamlit as st
import base64

def filter_items(df, item):
    data = df[['accountnum', 'siteaddress', 'itemdescription']]
    filtered_df = data[data['itemdescription'] == item]
    result = filtered_df[['accountnum', 'siteaddress', 'itemdescription']].drop_duplicates()
    return result

# Streamlit app
def main():
    st.title("Item Filter App")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read uploaded CSV file
        df = pd.read_csv(uploaded_file)
        
        # Show the uploaded data
        st.subheader("Uploaded Data")
        st.dataframe(df)
        
        # Get unique item options
        unique_items = df['itemdescription'].unique()
        
        # Item selection
        item = st.selectbox("Select an item", unique_items)
        
        # Filter items
        filtered_result = filter_items(df, item)
        
        # Display filtered result
        st.subheader("Filtered Result")
        st.dataframe(filtered_result)
        
        # Download filtered result as CSV
        if st.button("Download Filtered Result"):
            csv = filtered_result.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="filtered_result.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
