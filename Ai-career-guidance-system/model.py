# An ai model we are using it by API 
from google import genai

client = genai.Client(api_key=("AIzaSyBC0Rh5C4LQU9SbJXRrVmmzAA6AC0vbagc"))

def Ai_Model(prompt,user_data):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt,user_data], 
)
    return response.text

