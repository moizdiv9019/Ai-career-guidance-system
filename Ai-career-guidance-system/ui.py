import streamlit as st
import doc
from  pathlib import Path


def Roadmap_display(roadmap):

    st.header("🚀 Career Guidance: 6-months Roadmap")
    
    for month_data in roadmap:
        

        st.header(f"Month {month_data['month']}: {month_data['focus']}")
        
        
        for week in month_data['weeks']:
            with st.expander(f"📅 Week {week['week_number']}: {week['week_title']}"):
                
                st.subheader("Learning Objectives")
                

                cols = st.columns(len(week['learning_objectives']) // 3 + 1)
                for i, obj in enumerate(week['learning_objectives']):
                    cols[i % len(cols)].markdown(f"- {obj}")
    
                st.markdown("---")
                
               
                st.info(f"🛠️ **Tools:** {', '.join(week['tools'])}")
                st.success(f"🎯 **Practice Task:** {week['practice_task']}")
    
    
    Roadmap_file(roadmap)

    
def user_info_ui():  
    st.header("AI Career Guidance System")
    st.info("This website guides you in finding the correct path and mastering it.")

    # 1. Start the form
    with st.form(key="user_info_form"):
        # Define inputs inside the form
        name = st.text_input("Enter your name")
        email = st.text_input("Email ID")
        education = st.text_input("Education level", placeholder='Diploma / UG / PG / Other')
        branch = st.text_input("Stream or branch", placeholder='CSE / E&C / MECH / CIVIL / Other')
        skills = st.text_input("Skills")
        
        # Optional Fields
        interest = st.text_input("🎯 Interests (Optional)", placeholder="e.g., Data Science")
        about = st.text_area("📝 About You (Optional)", placeholder="Tell us more about your career goals...")

        # 2. Use st.form_submit_button instead of st.button
        submit_clicked = st.form_submit_button("Generate Guidance")

    if submit_clicked:
      user_data = {
          "name": name,
          "email": email,
          "education": education,
          "branch": branch,
          "skills": skills,
          "interest": interest,
          "about": about
      }
  
      # 3. Logic only runs when the button is pressed
      if submit_clicked:
          required_fields = ["name", "email", "education", "branch", "skills"]
          missing = [key for key in required_fields if not user_data[key]]
          
          if missing:
              st.error(f"Please fill these required fields: {', '.join(missing)}")
              return None # Return None if validation fails
          else:
              return user_data   
      return user_data      


def career_recommendations_ui(data):
    st.title("🎯 Career Recommendations")
    
    # We use a variable to capture the selection within this rerun
    selected_data = None

    # Using a 2-column layout for better readability
    cols_per_row = 2
    for i in range(0, len(data), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j in range(cols_per_row):
            index = i + j
            if index < len(data):
                career = data[index]
                
                with cols[j]:
                    with st.container(border=True):
                        st.subheader(f"✨ {career['career_name']}")
                        
                        st.markdown("**Job Roles:**")
                        roles_list = "".join([f"- {role}\n" for role in career["job_roles"]])
                        st.markdown(roles_list)
                        
                        st.info(f"**Why?** {career['reason']}")
                        
                        with st.expander("🔍 View Future Scope"):
                            st.write(career["future_scope"])
                        
                        st.markdown(f"**🛠️ Skills to Learn:**\n `{', '.join(career['skills_to_learn'])}` ")
                        
                        if st.button("Generate Roadmap 🚀", key=f"btn_{index}", use_container_width=True, type="primary"):
                            selected_data = career

    
    return selected_data


def Roadmap_file(roadmap):
   
    filename = doc.generate_roadmap_docx(roadmap)
    if isinstance(filename, tuple): 
        filename = filename[0]
        
    file_path = Path(__file__).parent / filename
    
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2: 
        with open(file_path, 'rb') as file:
            st.download_button(
                label="Download Roadmap",
                data=file,
                file_name=filename,
                icon='🛣️',
                use_container_width=True, 
                type="primary"           
            )

def setup_ui():
    return st.button("lets go🛣️")
    

