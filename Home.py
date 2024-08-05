import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Shreyas Thirthahalli")
    content = """Hello Guys..., This is Shreyas, a student of PES University persuing B Tech in CSE.
    Working to learn Python Development."""  # Triple quotes for multiline texts
    st.write(content)   # Instead of write we can use 'st.info(content)'

content_2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content_2)     # Instead of using string variable we can directly write the content inside bracket

col3, empty_col, col4 = st.columns(3)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("Images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")

with empty_col:
    pass

with col4:
    for index, row in df[10:21].iterrows():
        st.header(row["title"])
        st.image("Images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")

