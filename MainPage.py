import streamlit as st
import pandas as pd
from streamlit_carousel import carousel

#Session state variables
if 'userName'  not in st.session_state:    
    st.session_state.userName = "Observer"

# Defining HTML functions we will use to make website a bit more organized
def markdown(text, size, where):
    st.markdown(f'<{size} style ="text-align: {where};">{text}</{size}>', unsafe_allow_html=True)
def alignText(text, size, where):
    return f'<{size} style ="text-align: {where};">{text}</{size}>'

#The title and logo for the webpage
st.logo("https://upload.wikimedia.org/wikipedia/en/4/4e/Kirby_Nintendo.png")
st.markdown(alignText("Welcome to Trinidad's Treasure Trove", "h1", "center"), unsafe_allow_html=True)

#Sidebar for page selection
st.sidebar.subheader('Main Page')

#Saying hello to the costumer with their name
greeting_placeholder = st.empty()
greeting_placeholder.markdown(alignText(f"Welcome {st.session_state.userName}", "h3", "right"), unsafe_allow_html=True)
with st.popover("Sign in"):
    name = st.text_input("Input your name here", placeholder="Write your username here")
    if name: 
        if st.button("Submit name"): 
            st.session_state.userName = name.strip()
            greeting_placeholder.markdown(alignText(f"Welcome {st.session_state.userName}", "h3", "right"), unsafe_allow_html = True)

#Introduction to Trinidad Segovia
markdown("I'm Trinidad", "p", "center")

#Image carousel of projects built, with photos and url links, and also access to pngs
WelcomeCarouselImages = [
    dict(
        title = "",
        text = "",
        img = "https://robot.mbhs.edu/user/pages/01.HOME/03._about/_MG_0216_Original.jpg",
        link = "none"
    ),
    dict(
        title = "",
        text = "",
        img =     "https://conecta.tec.mx/sites/default/files/styles/header_full/public/2023-02/nuts-%26-volts-listos-para-regional-de-first-2023.jpg.webp?itok=K1NR5FQi",
        link = "none"
    ),
    dict(
        title = "",
        text = "",
        img = "https://media.team254.com/2017/01/979007e8-254_2160.jpg",
        link = "none"
    )
    
]
test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
        link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
    ),
]
carousel(WelcomeCarouselImages, width = 1)

#Making columns for Different Projects
left, center, right = st.columns(3)
with left:
    markdown("Programming","h5","center")

with center:
    markdown("CAD","h5","center")

with right:
    markdown("Mentorships","h5","center")
