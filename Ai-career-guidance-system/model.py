# An ai model we are using it by API 
from google import genai
import json

client = genai.Client(api_key=)
def Ai_Model(prompt,user_data):
    json_userdata=json.dumps(user_data)
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt,json_userdata] 
)
    
    return response.text


