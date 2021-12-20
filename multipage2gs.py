# This file is the framework for generating multiple Streamlit applications through an object oriented framework.

# Import necessary libraries 
from mainui import gsui
from usertraining import train
from datavalidation import validation
from DBDashboardStreamlit import dbrd
import streamlit as st
from streamlit.state.session_state import SessionState
from PIL import Image
from functions import *
import keyboard
import os
import signal
import streamlit.components.v1 as components
from bokeh.models.widgets import Div

# Define the multipage class to manage the multiple apps in our program 

class MultiPage: 
    # Framework for combining multiple streamlit applications.

    def __init__(self) -> None:
        # Constructor class to generate a list which will store all our applications as an instance variable.
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        # Class Method to Add pages to the project

        # Args:
        #     title ([str]): The title of page which we are adding to the list of apps 
            
        #     func: Python function to render this page in Streamlit

        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        # Dropdown to select the page to run

        html = """
        <style>
            .reportview-container {
            flex-direction: row-reverse;
            }

            header > .toolbar {
            flex-direction: row-reverse;
            left: 1rem;
            right: auto;
            }

            .sidebar .sidebar-collapse-control,
            .sidebar.--collapsed .sidebar-collapse-control {
            left: auto;
            right: 0.5rem;
            }

            .sidebar .sidebar-content {
            transition: margin-right .3s, box-shadow .3s;
            }

            .sidebar.--collapsed .sidebar-content {
            margin-left: auto;
            margin-right: -21rem;
            }

            @media (max-width: 991.98px) {
            .sidebar .sidebar-content {
                margin-left: auto;
            }
            }
        </style>
        """

        htmlpgui = '''
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!-- load MUI -->
            <link href="//cdn.muicss.com/mui-0.10.3/css/mui.min.css" rel="stylesheet" type="text/css" />
            <script src="//cdn.muicss.com/mui-0.10.3/js/mui.min.js"></script>
        </head>
        <body>
            <!-- example content -->
            <div class="mui-container">
            <div class="mui-panel">
                <h1>My Title</h1>
                <button class="mui-btn mui-btn--primary mui-btn--raised">My Button</button>
            </div>
            </div>
        </body>
        </html
        '''

        # st.markdown(html, unsafe_allow_html=True)

        # st.title("New Sidebar")
        st.sidebar.text("Globalstratos functions")

        preheader = st.container()
        header1 = st.container()

        with preheader:
            # bg colour used to be #A7A9AA;
            # sidebar colour used to be #818181;
            # sidebar hover used to be #f1f1f1;
            
            components.html('''
            <!DOCTYPE html>
            <html>

            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

                <style>
                    body {
                        font-family: "Lato", sans-serif;
                    }
                    
                    .sidebar {
                        height: 100%;
                        width: 39px;
                        position: fixed;
                        z-index: 1;
                        top: 0;
                        left: 0;
                        background-color: #f0f0f5;
                        overflow-x: hidden;
                        transition: 0.5s;
                        padding-top: 60px;
                        white-space: nowrap;
                    }
                    
                    .sidebar a {
                        padding: 1px 1px 1px 8px;
                        text-decoration: none;
                        font-size: 18px;
                        color: #A7A9AA;
                        display: block;
                        transition: 0.3s;
                    }
                    
                    .sidebar a:hover {
                        color: #CECECE;
                    }
                    
                    .sidebar .closebtn {
                        position: absolute;
                        top: 0;
                        right: 14px;
                        font-size: 14px;
                        margin-left: 5px;
                    }
                    
                    .material-icons,
                    .icon-text {
                        vertical-align: middle;
                    }
                    
                    .material-icons {
                        padding-bottom: 1px;
                    }
                    
                    #main {
                        transition: margin-left .5s;
                        padding: 19px;
                        margin-left: 39px;
                    }
                    /* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
                    
                    @media screen and (max-height: 450px) {
                        .sidebar {
                            padding-top: 5px;
                        }
                        .sidebar a {
                            font-size: 14px;
                        }
                    }
                </style>
            </head>

            <body>

                <div id="mySidebar" class="sidebar" onmouseover="toggleSidebar()" onmouseout="toggleSidebar()">
                    <a href="http://www.globalstratos.com/who-we-are/" target="_blank"><span><i class="material-icons">info</i><span class="icon-text">&nbsp;&nbsp;&nbsp;&nbsp;About</span></a><br>
                    <a href="https://spherio.io/" target="_blank"><i class="material-icons">spa</i><span class="icon-text"></span>&nbsp;&nbsp;&nbsp;&nbsp;Services</a></span>
                    </a><br>
                    <a href="http://www.globalstratos.com/contact-us/" target="_blank"><i class="material-icons">email</i><span class="icon-text"></span>&nbsp;&nbsp;&nbsp;&nbsp;Contact<span></a>
                </div>

                <div id="main">
                    <h2></h2>
                    <p></p>
                    <p></p>
                </div>

                <script>
                    var mini = true;

                    function toggleSidebar() {
                        if (mini) {
                            console.log("opening sidebar");
                            document.getElementById("mySidebar").style.width = "250px";
                            document.getElementById("main").style.marginLeft = "250px";
                            this.mini = false;
                        } else {
                            console.log("closing sidebar");
                            document.getElementById("mySidebar").style.width = "39px";
                            document.getElementById("main").style.marginLeft = "39px";
                            this.mini = true;
                        }
                    }
                </script>

            </body>

            </html>''')

        footercontent = '''Copyright (c) Globalstratos 2021'''

        customize_footer = """
        <style>
        footer{
            visibility:hidden;
        }
        footer:after{
            content:'Copyright (c) Globalstratos 2021';
            display:block;
            position:relative;
            color:dark-green;
            padding:5px;
            top:3px;
        }
        </style>
        """

        st.markdown(customize_footer, unsafe_allow_html=True)

        ### HIDING HAMBURGER MENU
        
        # hide_streamlit_style = """
        #     <style>
        #     #MainMenu {visibility: hidden;}
        #     footer {visibility: hidden;}
        #     footer:after{
        #     content: ' """ + footercontent + """'; 
        #     visibility: visible;
        #     display: block;
        #     position: relative;
        #     #background-color: red;
        #     padding: 5px;
        #     top: 2px;
        #     }
        #     </style>
        #     """

        # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        ### CUSTOMIZED HAMBURGER MENU https://www.kdnuggets.com/2021/07/streamlit-tips-tricks-hacks-data-scientists.html

        hide_streamlit_style = """
        <style>
        ul[data-testid=main-menu-list] > li:nth-of-type(3), /* Deploy this app */
        ul[data-testid=main-menu-list] > li:nth-of-type(4), /* Documentation */
        ul[data-testid=main-menu-list] > li:nth-of-type(5), /* Ask a question */
        ul[data-testid=main-menu-list] > li:nth-of-type(7), /* Report a bug */
        ul[data-testid=main-menu-list] > li:nth-of-type(8), /* Streamlit for Teams */
        ul[data-testid=main-menu-list] > li:nth-of-type(6), /* Ask a question */
        ul[data-testid=main-menu-list] > li:nth-of-type(10), /* About */
        ul[data-testid=main-menu-list] > div:nth-of-type(2) /* 2nd divider */
            {display: none;}
        </style>
        """

        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        with header1:
            clm1, clm2, clm3, clm4, clm5 = st.columns(5)
            with clm1:
                pass
            with clm2:
                pass
            with clm3:
                # image1 = Functions.set_svg_image('GSlogo.jpg')
                image2 = Image.open('GSLogo.jpg')
                st.image(image2, width=283)
            with clm4:
                pass
            with clm5:
                quitapp = st.button("Exit", key="multipgexit")
                reportbug = st.button("Report a bug", key='reportbug')
        
        if quitapp==True:
            keyboard.press_and_release('ctrl+w')
            os.kill(os.getpid(), signal.SIGTERM)

        if reportbug==True:
            js = "window.open('https://github.com/conceptualee/issue-tracking/issues')"  # New tab or window
            # js = "window.location.href = 'https://github.com/conceptualee/issue-tracking/issues'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

        # else:
        seloption = st.selectbox('Globalstratos UI Navigation', ['Main Globalstratos UI', 'Dashboard', 'Data validation', 'Show me how'], key='foo') # format_func=lambda page: page['title'],
        if seloption == 'Main Globalstratos UI':
            page = {'title': 'Main Globalstratos UI', 'function' : gsui}
        if seloption == 'Dashboard':
            page = {'title': 'Dashboard', 'function' : dbrd}
        if seloption == 'Data validation':
            page = {'title': 'Data validation', 'function' : validation}
        if seloption == 'Show me how':
            page = {'title': 'Show me how', 'function' : train}
        
        # run the selected app function

        def handle_click():
            st.session_state.foo = 'Main Globalstratos UI'

        def handle_click1():
            st.session_state.foo = 'Dashboard'

        def handle_click2():
            st.session_state.foo = 'Data validation'
        
        def handle_click3():
            st.session_state.foo = 'Show me how'

        mainbtn = st.sidebar.button("Main Globalstratos UI", on_click=handle_click)
        dashboard = st.sidebar.button("Dashboard", on_click=handle_click1)
        vldtn = st.sidebar.button("Data validation", on_click=handle_click2)
        how = st.sidebar.button("Show me how", on_click=handle_click3)
        
        if mainbtn == True:
            page={'title': 'Main Globalstratos UI', 'function': gsui}
        if dashboard == True:
            page={'title': 'Dashboard', 'function': dbrd}
        if vldtn == True:
            page={'title': 'Data validation', 'function': validation}
        if how == True:
            page={'title': 'Show me how', 'function': train}
            

        page['function']()
        


