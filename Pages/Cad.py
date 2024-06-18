import streamlit as st
import pandas as pd
from MainPage import markdown

#Create a list of CAD Knowledge
skills = ["Fusion 360", "Onshape", "Solidworks", "Blender", "Airshaper"]
fullSkills = [
    dict(
        name = "Fusion 360",
        experience = "4",
        logo = "https://seeklogo.com/images/A/autodesk-fusion-360-logo-7F72A76397-seeklogo.com.png"
    ),
    dict(
        name = "Onshape",
        experience = "5",
        logo = "https://play-lh.googleusercontent.com/yAS9WJJnjlCx77RxIvJSssrixhCdUxnBlM3CuPnQpl8QI3Ez19KreBL4xREc1gtmK_Y"
    )
]

#Title and subheader
markdown("Welcome to the CAD page", "h1", "Center")
st.write("These are my skills")

#Columns
left, middle, right = st.columns(3)
counter = 0
with left:
    for skill in fullSkills:
        st.subheader(skill["name"])
        st.write("logo", use_column_width=True)
        st.write(f"Experience {skill["experience"]}/5")
        counter += 1