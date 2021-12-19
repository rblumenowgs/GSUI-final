from numpy.core.numeric import identity
import streamlit as st
from streamlit.state.session_state import SessionState
import flask
from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
import base64
import os

### USER TRAINING ###

def validation():

    app = flask.Flask(__name__)
    resources = flask.Flask(__name__, instance_path=app.root_path + "\Resources")
    mappath = flask.Flask(__name__, instance_path=app.root_path + "\Maps")

    conn = pg.connect(host="SG-Globalstratos1-2053-pgsql-master.servers.mongodirector.com", 
    dbname="identity", 
    user="sgpostgres", 
    password="rUMw2uAud&vh60qH" ,
    port="5432",
    sslmode= "verify-full",
    sslrootcert = os.path.join(app.instance_path, "scalegridsslcert")
)

    conn2 = create_engine("postgresql+psycopg2://sgpostgres:rUMw2uAud&vh60qH@SG-Globalstratos1-2053-pgsql-master.servers.mongodirector.com:5432/identity")
    connect_args={"sslmode":"verify-full", "sslrootcert": os.path.join(app.instance_path) + "/scalegridsslcert"}
    connection = conn2.raw_connection()
    cursor = connection.cursor()

    header1pg5 = st.container()
    infosection = st.container()
  
    with header1pg5:

        col1,col2,col3 = st.columns(3)
        with col1:
            pass
        with col2:
            pass
        with col3:
            pass

    with infosection:
        
        try:

            if SessionState.loggedin == 'Verified':

                ### OLDER DB STARTS HERE

                header3 = st.container()
                inputfeature = st.container()
                validation = st.container()

                with header3:
                        #st.title('Globalstratos Dashboard')
                        st.markdown("<h1 style='text-align: center; color: green;'>Globalstratos Data Validation</h1>", unsafe_allow_html=True)
                        
                with inputfeature:

                    st.header("Choose data to validate")

                    validationfeature = st.selectbox("Available data", ['Identity', 'Sites'], key='vldtnfeature')

                    individuals = pd.read_sql_query("SELECT * FROM public.identity", conn)

                    sites = pd.read_sql_query("SELECT * FROM public.siteproductioninfo",conn)

                with validation:

                    if validationfeature == "Identity":

                        st.write("")
                        st.write("")
                        st.write("")
                        
                        st.header("Identity data available to be validated (edit directly below):")

                        gb = GridOptionsBuilder.from_dataframe(individuals)
                        gb.configure_pagination()
                        gb.configure_side_bar()

                        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                        gridOptions = gb.build()

                        newidentityinfo = AgGrid(individuals, 
                        gridOptions=gridOptions, 
                        enable_enterprise_modules=True, 
                        allow_unsafe_jscode=True, 
                        update_mode=GridUpdateMode.VALUE_CHANGED,
                        key='identityvldtn')

                        st.write("")
                        st.write("")
                        st.write("")
                        
                        st.header("Validated data:")
                        st.markdown("<h3 style='text-align: left; color: green; font-size=14px'>Changes made by " + SessionState.username + "</h3>", unsafe_allow_html=True)

                        st.write(newidentityinfo['data'])

                    if validationfeature == "Sites":

                        st.write("")
                        st.write("")
                        st.write("")
                        
                        st.header("Site data available to be validated (edit directly below):")

                        gb = GridOptionsBuilder.from_dataframe(sites)
                        gb.configure_pagination()
                        gb.configure_side_bar()

                        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                        gridOptions = gb.build()

                        newsiteinfo = AgGrid(sites, 
                        gridOptions=gridOptions, 
                        enable_enterprise_modules=True, 
                        allow_unsafe_jscode=True, 
                        update_mode=GridUpdateMode.VALUE_CHANGED,
                        key='sitesvldtn')

                        st.write("")
                        st.write("")
                        st.write("")
                        
                        st.header("Validated data:")
                        st.markdown("<h3 style='text-align: left; color: green; font-size=14px'>Changes made by " + SessionState.username + "</h3>", unsafe_allow_html=True)

                        st.write(newsiteinfo['data'])
                    
        except:
            pass