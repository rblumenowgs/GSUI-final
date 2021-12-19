import streamlit
import streamlit as st
import sys
from streamlit import cli as stcli
from PIL import Image
from functions import *
from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
import flask
import hashlib
import base64
import os
from streamlit.state.session_state import SessionState

# other imports

from re import template
from pkg_resources import run_script
from streamlit.state.session_state import SessionState
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
import plotly.express as px
import plotly.graph_objs as gobj
import sys
from streamlit import cli as stcli
import streamlit
import os
from PIL import Image
from functions import *
import pandas as pd
from pandasgui import show
import plotly.graph_objects as go
import geopandas as gpd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import descartes
from shapely.geometry import Point, Polygon
import numpy
import flask


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

    conn = pg.connect(host="18ce09dd-7e85-4a95-9568-c7dfcf402eab.497129fd685f442ca4df759dd55ec01b.databases.appdomain.cloud", 
        dbname="ibmclouddb", 
        user="admin", 
        password="gL0BAl1StrAtos23",
        port="32034",
        sslmode= "verify-full",
        # sslrootcert = os.getcwd() + "/041baeec-1272-11e9-8c9b-ae2e3a9c1b17"
        sslrootcert = os.path.join(app.instance_path, "041baeec-1272-11e9-8c9b-ae2e3a9c1b17"))

    conn2 = create_engine("postgresql+psycopg2://admin:gL0BAl1StrAtos23@18ce09dd-7e85-4a95-9568-c7dfcf402eab.497129fd685f442ca4df759dd55ec01b.databases.appdomain.cloud:32034/ibmclouddb",
    connect_args={"sslmode":"verify-full", "sslrootcert": os.path.join(app.instance_path) + "/041baeec-1272-11e9-8c9b-ae2e3a9c1b17"})
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
        c.execute("SELECT * FROM logininfo")
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
            # st.markdown("<h1 style='text-align: center; color: green;'>"'Welcome to the Globalstratos Data Validation System'"</h1>", unsafe_allow_html=True)
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
        new_user = st.text_input("Username",key='1')
        new_password = st.text_input("Password",type='password',key='2')

        if st.button("Sign up"):
            st.success("You have successfully created a valid account")
            st.info("Go to Login Menu to login")
            # Insert into DB here

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

        c.execute("SELECT password FROM logininfo WHERE username =" + "'" + username + "'",(username,password))
        dbpassword = c.fetchall()

        if password == dbpassword[0][0]:
            # access = True
            SessionState.loggedin="Verified"
            SessionState.username = username
        else:
            access = False
            st.warning("Incorrect Username/Password")

    with login:

        try:
            
            if SessionState.loggedin == 'Verified':

                # st.success("Logged in as {}".format(username))
                st.success("Logged in as " + SessionState.username)
                print(SessionState.loggedin)

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

        except:
            pass

        with content:
            
            try:

                if SessionState.loggedin == 'Verified':

                    ### OLDER DB STARTS HERE

                    header3 = st.container()
                    dataset = st.container()
                    features = st.container()
                    siteinfo = st.container()
                    overviewmap = st.container()
                    model_training = st.container()

                    with header3:
                            #st.title('Globalstratos Dashboard')
                            st.markdown("<h1 style='text-align: center; color: green;'>Main Globalstratos Dashboard</h1>", unsafe_allow_html=True)
                            #st.text('This dashboard builds on a proprietary dataset gathered at source')
                            st.markdown("<p style='text-align: center; color: white;'>This dashboard builds on a proprietary dataset gathered at source</p>", unsafe_allow_html=True)

                    with dataset:

                        st.header("")
                        st.header("Data from primary collection")
                        st.text("Data sourced during direct interactions, during identity onboarding and site assessments.")

                        # dbcall()

                        identity = pd.read_sql_query("SELECT * FROM public.identity",conn)
                        sites = pd.read_sql_query("SELECT * FROM public.siteproductioninfo",conn)
                        sitestranspose = sites.transpose()
                        forms = pd.read_sql_query("SELECT * FROM public.generalformentry",conn)

                        st.write('First 5 sample records:')

                        st.write(identity.head())

                        respondents = pd.read_sql_query("SELECT COUNT(uuid) FROM public.generalformentry WHERE form_name = 'Registration' GROUP BY today", conn)
                        st.subheader("Number of registered identities")
                        st.markdown('* We consider first the total number of registered participants - **formalization at scale**')
                        st.line_chart(respondents)

                    with features:

                        header = st.container()
                        content = st.container()

                        with header:
                            st.header("Origin countries of registered individuals")
                            st.subheader("(top 3 African priorities)")

                        with content:
                            
                            sel_col, empty_col, disp_col = st.columns(3)

                            cursor.execute("SELECT COUNT(uuid) FROM public.identitydetails WHERE id_country = 'South Africa' GROUP BY id_country")
                            zar = cursor.fetchall()
                            cursor.execute("SELECT COUNT(uuid) FROM public.identitydetails WHERE id_country = 'Nigeria' GROUP BY id_country")
                            nigr = cursor.fetchall()
                            cursor.execute("SELECT COUNT(uuid) FROM public.identitydetails WHERE id_country = 'Kenya' GROUP BY id_country")
                            kenr = cursor.fetchall()

                            fig = go.Figure(data=go.Choropleth(
                                locations=['south africa','nigeria','kenya'], # Spatial coordinates
                                text= ['ZA','NIG','KEN'],
                                z = [(zar[0])[0], (nigr[0])[0], (kenr[0])[0]], # Data to be color-coded
                                locationmode = 'country names', # set of locations match entries in `locations`
                                colorscale = 'Portland',
                                colorbar_title = "Country intensity",
                            ))

                            cursor.execute("SELECT COUNT(which_province_state_is_the_site_located) FROM public.siteinfo WHERE which_province_state_is_the_site_located = 'Kaduna' GROUP BY which_province_state_is_the_site_located")
                            kaduna = cursor.fetchall()

                            fig.update_layout(
                                title_text = 'Number of registered individuals by country',
                                geo_scope='africa', # limit map scope to Africa
                            )

                            fig.data[0].colorbar.x=-0.1
                            sel_col.write(fig)

                            disp_col.markdown("<h3 style='text-align: center; color: black;'>The total number of registered individuals is:</h3>", unsafe_allow_html=True)
                            disp_col.markdown("<h1 style='text-align: center; color: green;'>" + str(identity['uuid'].count()) + "</h1>", unsafe_allow_html=True)

                            disp_col.markdown("<h3 style='text-align: center; color: black;'>The total number of registered sites is:</h3>", unsafe_allow_html=True)
                            disp_col.markdown("<h1 style='text-align: center; color: green;'>" + str(sites['uuid'].count()) + "</h1>", unsafe_allow_html=True)

                            disp_col.markdown("<h3 style='text-align: center; color: black;'>The total number of forms completed is:</h3>", unsafe_allow_html=True)
                            disp_col.markdown("<h1 style='text-align: center; color: green;'>" + str(forms['uuid'].count()) + "</h1>", unsafe_allow_html=True)

                    with siteinfo:
                        clmn1, clmn2, clmn3 = st.columns(3)

                        with clmn1:
                            cursor.execute("SELECT DISTINCT(site_name) FROM public.siteproductioninfo")
                            siteselections = cursor.fetchall()
                            selectedsite = st.selectbox("More site information - please choose site", siteselections, key="differentsite")
                            SessionState.selectedsite=selectedsite[0]
                            print(selectedsite)
                            def handle_click():
                                st.session_state.foo = 'Specific site information'
                                sitespecificinfo
                            moresitedetails = st.button("Tell me more about this site", on_click=handle_click)
                            moresitedetails2 = st.button("Let me analyze and compare sites")
                            if moresitedetails2 == True:
                                selectedsite = pd.read_sql_query('SELECT * FROM public.siteproductioninfo',conn)
                                gui=show(selectedsite)
                            
                        with clmn2:
                            pass

                        with clmn3:
                            morepeopleinfo = st.button("More information on individuals")
                            moresiteinfo = st.button("More information on sites")

                            if morepeopleinfo == True:
                                gui1 = show(identity)

                            if moresiteinfo == True:
                                gui2 = show(sites)

                    with overviewmap:

                        col = st.expander("More geographic information, including maps with site markers", expanded=False)

                        with col:

                            sitelocations = pd.read_sql_query("select distinct(site_location), site_name from public.siteinfo",conn)

                            # print(sitelocations)

                            for i in range(0, len(sitelocations['site_location'])):
                                sitelocs = sitelocations['site_location'].str.split(' ', expand=True)
                                sitelocations['lat'] = numpy.float16(sitelocs[0])
                                sitelocations['long'] = numpy.float16(sitelocs[1])
                            print(sitelocations['lat'])
                            print(sitelocations['long'])
                                # sitelocs[i][0] = float(sitelocs[i][0])
                                # sitelocs[i][1] = float(sitelocs[i][1])

                            # center on Abuja 
                            m = folium.Map(location=[9.0765, 7.3986], zoom_start=3)

                            # add marker for sites
                            for i in range(0, len(sitelocations['site_location'])):
                                tooltip = (sitelocations['site_name'])[i]
                                folium.Marker(
                                    [(sitelocations['lat'])[i], (sitelocations['long'])[i]], popup=(sitelocations['site_name'])[i], tooltip=tooltip
                                    ).add_to(m)

                            st.header("Overview map")

                            st.write("Use scroll wheel to zoom in or out")

                            # call to render Folium map in Streamlit
                            folium_static(m)

            except:
                pass
                        


if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        gsui.run()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())