import streamlit
import streamlit as st
import sys
from streamlit import cli as stcli
from PIL import Image
from DBDashboardStreamlit import dbrd
from functions import *
from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
import flask
import hashlib
import base64
import os
from streamlit.state.session_state import SessionState
import pandas as pd
from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
import random
from datetime import date

def gsui():

    app = flask.Flask(__name__)
    resources = flask.Flask(__name__, instance_path=app.root_path + "\Resources")
    mappath = flask.Flask(__name__, instance_path=app.root_path + "\Maps")
    formimages = flask.Flask(__name__, instance_path=app.root_path + "\\form-images")

    if 'model' not in st.session_state:
        st.session_state.model = "None"
    if 'loggedin' not in st.session_state:
        st.session_state.loggedin = ""

    header1 = st.container()
    header2 = st.container()
    login = st.container()
    content = st.container()
    assessments = st.container()
    questionnaires = st.container()

    # conn = pg.connect(host="18ce09dd-7e85-4a95-9568-c7dfcf402eab.497129fd685f442ca4df759dd55ec01b.databases.appdomain.cloud", 
    #     dbname="ibmclouddb", 
    #     user="admin", 
    #     password="gL0BAl1StrAtos23",
    #     port="32034",
    #     sslmode= "verify-full",
    #     # sslrootcert = os.getcwd() + "/041baeec-1272-11e9-8c9b-ae2e3a9c1b17"
    #     sslrootcert = os.path.join(app.instance_path, "041baeec-1272-11e9-8c9b-ae2e3a9c1b17"))

    # conn2 = create_engine("postgresql+psycopg2://admin:gL0BAl1StrAtos23@18ce09dd-7e85-4a95-9568-c7dfcf402eab.497129fd685f442ca4df759dd55ec01b.databases.appdomain.cloud:32034/ibmclouddb",
    # connect_args={"sslmode":"verify-full", "sslrootcert": os.path.join(app.instance_path) + "/041baeec-1272-11e9-8c9b-ae2e3a9c1b17"})
    # connection = conn2.raw_connection()
    # cursor = connection.cursor()

    conn = pg.connect(host="SG-Globalstratos1-2053-pgsql-master.servers.mongodirector.com", 
    dbname="identity", 
    user="sgpostgres", 
    password="rUMw2uAud&vh60qH" ,
    port="5432",
    sslmode= "verify-full",
    sslrootcert = os.path.join(app.instance_path, "scalegridsslcert")
)

    # conn2 = create_engine("postgresql+psycopg2://SG-Globalstratos1-2053-pgsql-master.servers.mongodirector.com:5432/identity",
    conn2 = create_engine("postgresql+psycopg2://sgpostgres:rUMw2uAud&vh60qH@SG-Globalstratos1-2053-pgsql-master.servers.mongodirector.com:5432/identity")
    connect_args={"sslmode":"verify-full", "sslrootcert": os.path.join(app.instance_path) + "/scalegridsslcert"}
    connection = conn2.raw_connection()
    cursor = connection.cursor()

    # def create_usertable():
    #     c.execute(‘CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)’)

    # def add_userdata(username,password):
    #     c.execute(‘INSERT INTO userstable(username,password) VALUES (?,?)’,(username,password))
    #     conn.commit()

    def login_user(username,password):
        cursor.execute("SELECT password FROM logininfo WHERE username =" + "'" + username + "'",(username,password))
        data = cursor.fetchall()
        return data

    def view_all_users():
        cursor.execute("SELECT * FROM logininfo")
        data = cursor.fetchall()
        return data

    with header1:
            clm1, clm2, clm3, clm4, clm5 = st.columns(5)
            with clm1:
                pass
            with clm2:
                pass
            with clm3:
                pass
            with clm4:
                pass
            with clm5:
                pass

    with header2:

        col1,col2,col3 = st.columns(3)
        with col1:
            pass
        with col2:
            # st.markdown("<h1 style='text-align: center; color: green;'>"'Welcome to the Globalstratos Advanced Analytics System'"</h1>", unsafe_allow_html=True)
            pass
        with col3:
            pass

    # st.title("Please login")

    menu = ["Home","Login","Sign up"]
    choice = st.sidebar.selectbox("Menu",menu, key="choice")

    if choice == "Home":
        st.write("")
        st.text("Chosen page: Home")

    if choice == "Login":
        SessionState.loggedin = ""

    if choice == "Sign up":
        st.subheader("Create New Account")
        new_name = st.text_input("First name", key="firstname")
        new_surname = st.text_input("Surname/family name", key="surname")
        new_user = st.text_input("Username",key='user')
        new_password = st.text_input("Password",type='password',key='password')
        uuid = str(random.randint(random.randint(0,100), random.randint(100,100000)))

        if st.button("Sign up"):
            # Insert into DB here
            # cursor.execute('''INSERT INTO logininfo(username, password, uuid, name, surname) VALUES (''' + "'" + new_user + "'" + "," + "'" + new_password + "'" + "," + "'" + + uuid + "'" + "," + "'" + new_name + "'" + "," + "'" + new_surname + "'" + ")" )
            # sql = "INSERT INTO logininfo (username, password, uuid, name, surname) VALUES (%s, %s, %s, %s, %s)"
            sql = "INSERT INTO public.logininfo (username, password, uuid, name, surname, dateentered) VALUES ({},{},{},{},{},{})".format("'" + new_user + "'", "'" + new_password + "'", "'" + uuid + "'", "'" + new_name + "'", "'" + new_surname + "'", "'" + str(date.today()) + "'")
            # val = (new_user, new_password, uuid, new_name, new_surname)
            cursor.execute(sql) # Used to be execute(sql,val)
            connection.commit()
            st.success("You have successfully created a valid account")
            st.info("Go to Login Menu to login")

    placeholder1 = st.sidebar.empty()
    placeholder2 = st.sidebar.empty()
    placeholder3 = st.sidebar.empty()

    username = placeholder1.text_input("User Name")
    password = placeholder2.text_input("Password",type='password')

    # #passlib,hashlib,bcrypt,scrypt
    # def make_hashes(password):
    #     return hashlib.sha256(str.encode(password)).hexdigest()

    # def check_hashes(password,hashed_text):
    #     if make_hashes(password) == hashed_text:
    #         return hashed_text
    #         return False

    loginbtn = placeholder3.button("Login", key="loginbtn")
        
    if loginbtn:
        # #if password == '12345':
        # hashed_pswd = make_hashes(password)

        # result = login_user(username,check_hashes(password,hashed_pswd))

        cursor.execute("SELECT password FROM logininfo WHERE username =" + "'" + username + "'",(username,password))
        dbpassword = cursor.fetchall()

        if password == dbpassword[0][0]:
            # access = True
            SessionState.loggedin="Verified"
            SessionState.username = username
        else:
            access = False
            st.error("Incorrect Username/Password")

    with login:

        try:
            
            if SessionState.loggedin == 'Verified':

                # st.success("Logged in as {}".format(username))
                st.success("Logged in as " + SessionState.username)
                print(SessionState.loggedin)
                task = st.selectbox("Task",["Launch forms","Analytics"])

                placeholder1.empty()
                placeholder2.empty()
                placeholder3.empty()
                
                # username = placeholder1.text_input("User Name", value = '')
                # password = placeholder2.text_input("Password",type='password', key='loginbtn', value='')

                @st.cache(allow_output_mutation=True)
                def get_base64_of_bin_file(bin_file):
                    with open(bin_file, 'rb') as f:
                        data = f.read()
                    return base64.b64encode(data).decode()

                @st.cache(allow_output_mutation=True)
                def get_img_with_href(local_img_path, target_url):
                    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
                    bin_str = get_base64_of_bin_file(local_img_path)
                    html_code = f'''
                        <a href="{target_url}" target="_blank">
                            <img src="data:image/{img_format};base64,{bin_str}" />
                        </a>'''
                    return html_code
            
                if task == "Launch forms":
                    print(SessionState.loggedin + " launch forms")
                    st.header("Launch forms")
                     
                    with assessments:

                        col1,col2,col3 = st.columns(3)
                        with col1:
                            pass
                        with col2:
                            st.image("onboardinghead.png")
                        with col3:
                            pass

                        col1,col2,col3,col4,col5 = st.columns(5)

                        with col1:

                            gif_html = get_img_with_href('Registrationsmall.png', 'https://ee.humanitarianresponse.info/x/3bVU0wCr')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col2:
                            gif_html = get_img_with_href('Initasssmall.png', 'https://ee.humanitarianresponse.info/x/aFfVuRhL')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col3:
                            gif_html = get_img_with_href('Siteprodsmall.png', 'https://ee.humanitarianresponse.info/x/lXET0HJy')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col4:
                            gif_html = get_img_with_href('Artsitesmall.png', 'https://ee.humanitarianresponse.info/x/jYibP0Rx')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col5:
                            gif_html = get_img_with_href('Prodcompsmall.png', 'https://ee.humanitarianresponse.info/x/qyCcvg9p')
                            st.markdown(gif_html, unsafe_allow_html=True)

                    with questionnaires:

                        st.write("")

                        col1,col2,col3 = st.columns(3)
                        with col1:
                            pass
                        with col2:
                            st.image("Supportingques.png")
                        with col3:
                            pass
                        
                        col1,col2,col3 = st.columns(3)

                        with col1:
                            gif_html = get_img_with_href('Stakeholderquessmall.png', 'https://ee.humanitarianresponse.info/x/PKD2QrAg')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col2:
                            gif_html = get_img_with_href('Supportingdocssmall.png', 'https://ee.humanitarianresponse.info/x/EgT4PhTp')
                            st.markdown(gif_html, unsafe_allow_html=True)

                        with col3:
                            gif_html = get_img_with_href('Orgidsmall.png', 'https://ee.humanitarianresponse.info/x/7A1AExO6')
                            st.markdown(gif_html, unsafe_allow_html=True)
                    
                if task == "Analytics":
                    print(SessionState.loggedin + " analytics")
                    st.header("Analytics")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        pass
                    with col2:
                        gif_html = get_img_with_href('Analyticsplatform.png', 'http://www.google.com')
                        st.markdown(gif_html, unsafe_allow_html=True)
                        launchanalytics = st.button("Launch analytics platform", key='analyticslaunch', on_click=dbrd)
                    st.write("")
                    if not launchanalytics:
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            pass
                        with col2:
                            gif_html = get_img_with_href('Modellingsmall2.png', 'http://www.google.com')
                            st.markdown(gif_html, unsafe_allow_html=True)
                        with col3:
                            pass
                        st.write("")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            gif_html = get_img_with_href('Finmodel.png', 'http://www.google.com')
                            st.markdown(gif_html, unsafe_allow_html=True)
                        with col2:
                            gif_html = get_img_with_href('Scenarioanalysis.png', 'http://www.google.com')
                            st.markdown(gif_html, unsafe_allow_html=True)
                        with col3:
                            gif_html = get_img_with_href('Parsing.png', 'http://www.google.com')
                            st.markdown(gif_html, unsafe_allow_html=True)
                        choice = st.sidebar.selectbox("Menu",menu, value="Home", key="choice")
            
        except:
            if st.session_state.loggedin != 'Verified':
                st.header("Please log in using the panel on the left")

if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        gsui.run()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
    if st.session_state.loggedin != 'Verified':
        st.header("Please log in using the panel on the left")