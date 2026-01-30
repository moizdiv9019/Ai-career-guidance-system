# An ai model we are using it by API 
from google import genai
import json


def Ai_Model(prompt,user_data,api):
 try:
    client = genai.Client(api_key=api)
    json_userdata=json.dumps(user_data)
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt,json_userdata]
)
 except Exception:
    return -1
 else:
    return response.text


