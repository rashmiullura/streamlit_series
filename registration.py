import streamlit as st

st.title("Registration form")

first,last = st.beta_columns(2)
first.text_input("First name")
last.text_input("Last name")

email,mob = st.beta_columns([3,1])
email.text_input("Email ID")
mob.text_input("Mobile No.")

user,pwd,pwd2 = st.beta_columns(3)
user.text_input("Username")
pwd.text_input("Passowrd",type="password")
pwd2.text_input("Retype your password",type="password")

ch,bl,sub=st.beta_columns(3)
ch.checkbox("I agree")
sub.button("Submit")