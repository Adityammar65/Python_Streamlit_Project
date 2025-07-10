import streamlit as st
import pandas as pd

st.title('Mean,Median,Mode calculator')

upload_file=st.file_uploader("Upload your file here", type=["xlsx","csv"])
if upload_file is not None:
    if upload_file.name.endswith('.xlsx'):
        df=pd.read_excel(upload_file)
    else:
        df=pd.read_csv(upload_file)

    st.write("Uploaded data:")
    st.dataframe(df)

    numeric_cols=df.select_dtypes(include='number').columns.tolist()
    selected_col=st.selectbox("Choose column",numeric_cols)

    if selected_col:
        st.subheader(f"Result: {selected_col}")
        st.write("**Mean:**",df[selected_col].mean())
        st.write("**Median:**",df[selected_col].median())
        st.write("**Mode:**",df[selected_col].mode().iloc[0])
