import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username, password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password=?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

def main():
    """ Simple Login App"""
    st.title("Simple Login App")
    menu = ["Home", "Login", "SignUP"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Login"):

            create_table()
            result = login_user(username,password)
            if result:
                st.success("Logged in as {}".format(username))
                task = st.selectbox("Task",["Add Post", "Analytics", "Profile"])
                if task == "Add Post":
                    st.subheader("Add Your Post")
                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profile":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username", "Password"])
                    st.dataframe(clean_db)
            else:

                st.warning("Incorrect Username or password")
    elif choice == "SignUP":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")

        if st.button("Signup"):
            create_table()
            add_userdata(new_user,new_pass)
            st.success("You have successfully created an Account")
            st.info("Go to Login Menu to login")

if __name__  == '__main__' :
    main()