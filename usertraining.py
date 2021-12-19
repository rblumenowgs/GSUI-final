import streamlit as st
from streamlit.state.session_state import SessionState
import flask

### USER TRAINING ###

def train():

    app = flask.Flask(__name__)
    resources = flask.Flask(__name__, instance_path=app.root_path + "\Resources")
    mappath = flask.Flask(__name__, instance_path=app.root_path + "\Maps")

    header1pg5 = st.container()
    infosection = st.container()
  
    with header1pg5:

        col1,col2,col3 = st.columns(3)
        with col1:
            pass
        with col2:
            st.markdown("<h1 style='text-align: center; color: green;'>"'How to use the UI'"</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center; color: green;'>"'Training and FAQ'"</h2>", unsafe_allow_html=True)
            # st.header("How to use the UI")
        with col3:
            pass

    with infosection:
        st.header("Sections of the UI")
        sections = st.expander("Components of the system", expanded=False)
        with sections:
            st.write("Sections of this system include:\n"
            "\n1. The main landing page\n"
            "\n\tThis is the main control and navigation hub, and includes the ability to launch forms as well as the various analytical systems."
            "\n2. The dashboard\n"
            "\n\tThis presents key analytical information."
            "\n3. Data validation\n"
            "\n\tThis allows the user to validate data collected on the ground and ingested into our database.\n"
            "\n\n"
            "\n\tIncluded functionality with other assorted controls are the capability to log changes made by users, log a bug or issue into our tracker, and generalized access control/security."
            )
        st.header("How to view and edit data")
        viewedit = st.expander("More information on data validation tool", expanded=False)
        with viewedit:
            st.write("Data validation happens in 3 steps - first, the user selects what data they wish to validate. Then, in the data table, changes are made directly, with the user able to amend data as well as perform some basic operations such as sorting and filtering. Finally, once the user is happy that the data reflects reality accurately, they are offered the option to commit their changes to the database, which will then be staged into the clean (not live) partition of the database.")
            st.write("Please view [this video](https://www.youtube.com/watch?v=jYlwwNycVh8) for an example of a similar data validation tool.")
        st.header("FAQ")
        viewedit = st.expander("Common questions", expanded=False)
        with viewedit:
            st.write("Is validated data automatically commited to the database?\n"
            "\n\tNo. The user must complete the validation process, and then manually select to commit the changes to the staging area of the database. This is a security feature implemented to prevent data and user errors.")
