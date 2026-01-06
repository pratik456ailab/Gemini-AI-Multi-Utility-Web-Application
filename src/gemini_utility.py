import os
import json

import google.generativeai as genai
from pandas.core.computation.common import result_type_many

#get a working directory
working_directory=os.path.dirname(os.path.abspath(__file__))

config_file_path=f"{working_directory}/config.json"
config_data=json.load(open(config_file_path))

#loading the api key
GOOGLE_API_KEY=config_data["GOOGLE_API_KEY"]
#configuring google.generativeai with apikey
genai.configuration(api_key=GOOGLE_API_KEY)

#function to load gemini-pro-model for chatbot 
def load_gemini_pro_model():
    gemini_pro_model=genai.GenerativeModel("gemini-pro")
    return gemini_pro_model
#function for image captioning

def gemini_pro_vision_response(prompt,image):
    gemini_pro_vision_model=genai.GenerativeModel("gemini-pro-vision")
    response=gemini_pro_vision_model.generate_content([prompt,image])
    result= response.text
    return result

image= Image.open("test_image.png")
prompt="Write a short caption for the image"
output=gemini_pro_vision_response(prompt,image)
print(output)

#function to get embidding for text
def embedding_model_response(input_text):
    embedding_model="model/embedding-001"
    embedding=genai.embed_content(model=embedding_model,
                                  content=input_text,
                                  task_type="retrival_document")
    embedding_list=embedding["embedding"]
    return embedding_list
output=embedding_model_response("Who is Thonas")
print(output)

# function to get a response from gemini-pro LLM
def gemini_pro_response(user_prompt):
    gemini_pro_model.generate_content(user_prompt)
    result=response.text
    return result

output=gemini_pro_response("What is machine learning ")
print(output)
