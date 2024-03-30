import streamlit as st
import pandas

st.set_page_config(layout="wide")

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg",use_column_width="always")

with col2:
    st.title("JC Elayron")
    st.write("Welcome to my portfolio! "\
            "I am a passionate Python developer "\
            "with two years of professional experience, "\
            "having graduated from Mapua University "\
            "with a solid foundation in computer science. "\
            "My journey in the realm of software development "\
            "has been marked by an insatiable curiosity and "\
            "a commitment to delivering high-quality solutions. ")
    st.write("""With a strong foundation in Python development
             and a versatile skill set encompassing other 
             languages and frameworks, I am equipped to tackle 
             diverse challenges in the world of software 
             development. Whether it's crafting elegant web 
             applications, optimizing database performance, or 
             solving complex algorithmic problems, I am 
             committed to delivering innovative solutions that 
             exceed expectations. Thank you for exploring my 
             portfolio, and I look forward to the opportunity 
             to collaborate on exciting projects in the future.""")

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, emptycol,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df.iterrows():
        if index%2 == 1:
            st.header(row["title"])
            st.image(f"images/{row['image']}")
            st.write(row["description"])
            st.page_link(row["url"],label = "Source Code")

with col4:
    for index, row in df.iterrows():
        if index%2 != 1:
            st.header(row["title"])
            st.image(f"images/{row['image']}")
            st.write(row["description"])
            st.page_link(row["url"],label = "Source Code")

