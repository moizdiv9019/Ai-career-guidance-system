import streamlit as st

def user_data_ui():  
   st.header("AI career guidance system")
   st.info("This website guides you in finding the correct path and mastering it.")

   # Define inputs
   name = st.text_input("Enter your name")
   email = st.text_input("Email ID",)
   education = st.text_input("Education level",placeholder='Diploma UG PG /  Other ')
   branch = st.text_input("Stream or branch",placeholder='CSE E&C MECH CIVIL / OTHER')
   skills = st.text_input("Skills")
   
   # Optional Fields (Visual cues added)
   interest = st.text_input("🎯 Interests (Optional)", placeholder="e.g., Data Science")
   about = st.text_area("📝 About You (Optional)", placeholder="Tell us more about your career goals...")

   user_data = {
       "name": name,
       "email": email,
       "eduction": education,
       "branch": branch,
       "skills": skills,
       "intrest": interest,
       "Any thing about user": about
   }

   if st.button("Generate"):
       # Only check for missing values in required fields
       required_fields = ["name", "email", "eduction", "branch", "skills"]
       missing = [key for key in required_fields if not user_data[key]]
       
       if missing:
           st.error(f"Please fill these required fields: {', '.join(missing)}")
       else:
           st.success("All details submitted successfully")
   
   return user_data


def Career_recommedations(data):
       
       st.title("Career Recommendations")
       
       cols = st.columns(len(data))
       
       for i, career in enumerate(data):
           with cols[i]:
       
               with st.container(border=True):
                   st.subheader(career["career_name"])
                   
                   
                   st.markdown("**Job Roles:**")
                   for role in career["job_roles"]:
                       st.markdown(f"- {role}")
                   
                   st.write(f"**Why?** {career['reason']}")
                   
                  
                   with st.expander("View Future Scope"):
                       st.write(career["future_scope"])
                       
                   st.info(f"**Remaining skills:** {', '.join(career['skills_to_learn'])}")
                   if st.button(f"Generate Roadmap", key=f"btn_{i}", use_container_width=True):
                       user_selected_career=data[i]
       return user_selected_career
