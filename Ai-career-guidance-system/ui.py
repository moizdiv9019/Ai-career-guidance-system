import streamlit as st

def user_data_ui():
   st.header("AI career guidence system")
   st.badge("This website guides you in finding the correct path and mastering it.",color='violet')
   data={
   "name": st.text_input("Enter your name"),
   "email":st.text_input("email Id"),
   "eduction":st.text_input(" Education level"),
   "branch":st.text_input("stream or branch"),
   "skills":st.text_input("skills"),
   "intrest":st.text_input("interests"),
   "Any thing about user":st.text_area("Any thing about you")
   }
   if st.button("Generate"):
       missing=[key for key,value in data.items() if not value]
       if missing:
           st.error(f"Please fill these fields:{', '.join(missing)}")
       else:
           st.success("All details submitted successfully")
   
   return data

user_data_ui()


