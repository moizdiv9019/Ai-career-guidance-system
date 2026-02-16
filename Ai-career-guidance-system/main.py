import streamlit as st
import ui
import model
from myprompts import prompt_1 ,prompt_2


for key in ['user_data','careers_ui','roadmap_ui','ai_careers','ai_roadmap','roadmap_doc','user_email','user_selected_career']:
    if key not in st.session_state:
        st.session_state[key]=None

# Step 1 user input
user_data = ui.user_info_ui()

if user_data:
    st.session_state['user_data']=user_data
    st.session_state['user_email']=user_data['email']
    

# Step 2 AI careers
if st.session_state['user_data'] and not st.session_state['ai_careers']:
     with st.spinner("🚀 Generating career paths..."):
       st.session_state['ai_careers']=model.Ai_Model(
           prompt_1,
           st.session_state['user_data'],
           st.secrets['new']
       )

# Step 3 career selection
if st.session_state['ai_careers']:
       if st.session_state['ai_careers']['status']=='success':
          st.session_state['user_selected_career']=ui.career_recommendations_ui(
              st.session_state['ai_careers']['data']
          )
           
       else:
           st.error(st.session_state['ai_careers']['message'],icon='🚨')
           st.stop()

# Step 4 roadmap
if st.session_state['user_selected_career'] and not st.session_state['ai_roadmap']:
    with st.spinner("🚀Generating your  career roadmap"):
      data={'target_career':st.session_state['user_selected_career']['career_name'],
      'existing_skills':st.session_state['user_data']['skills'],
      'skills_to_learn':st.session_state['user_selected_career']['skills_to_learn']}
      st.session_state['ai_roadmap']=model.Ai_Model(
          prompt_2,
          data,
          st.secrets['new']
      )

# # Step 5 display
if st.session_state['ai_roadmap']:
    if st.session_state['ai_roadmap']['status']=='success':
        ui.Roadmap_display(st.session_state['ai_roadmap']['data'])

    else:    
        st.error(st.session_state['ai_roadmap']['message'])


