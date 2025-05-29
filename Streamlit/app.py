import os
import streamlit as st
st.set_page_config(page_title ="동아수리논리학", page_icon=":material/person:", layout="wide")
from streamlit_navigation_bar import st_navbar
from util.state import *
import my_pages as pg
from css.theme import * 
from util.menu import *
import my_pages as pg

#page_names = ["Home"] + list(pg.my_pages.keys)
#default = "Home"
#page_config = pg.get_page_config(page_name = default)
##st.set_page_config(
#    page_title=page_config["title"],
#    page_icon=page_config["icon"]
#)

load_css()
clear_state()
menu_mk2()
pages = ["홈", "강의 노트", "게시판"]

nav_style = {
    "nav": {
        "justify-content" : "left",
    },
    "active": {
        "color" : "#2766C2",
    },
    "hover": {
        "color" : "lightblue",
    },
    "div" : {
        "width" : "25%;"
    },
}

options = {
    "show_menu" : False,
    "show_sidebar": True,
}

icons = {"홈": ":material/home:",
                "강의 노트": ":material/notes:",
                "게시판" : ":material/dashboard:"}

page = st_navbar(
    pages,
    styles = nav_style,
    options=options,
    icons=icons
)



fuctions = {
    "홈": pg.show_home,
    "강의 노트": pg.show_input,
    "게시판" : pg.show_board,
}


if page != st.session_state['page']:
    st.session_state['page'] = page
    
if st.session_state['page'] == "홈" :
    pg.show_home()
elif st.session_state['page'] == "강의 노트" :
    pg.show_input()
elif st.session_state['page'] == "게시판":
    pg.show_board()
