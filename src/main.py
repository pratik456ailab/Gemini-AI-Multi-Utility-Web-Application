import os

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
from  gemini_utility import load_gemini_pro_model

from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_response,
                            gemini_pro_vision_response,
                            embeddings_model_response)


working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered",
)

with st.sidebar:
    selected = option_menu('Gemini AI',
                           ['ChatBot',
                            'Image Captioning',
                            'Embed text',
                            'Ask me anything'],
                           menu_icon='robot', icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0
                           )
#function to translate role between gemini-pro and streamlit treminal
def translate_role_for_streamlit(user_role):
    if user_role=='model':
        return "assistant"
    else:
        return user_role

if selected=='ChatBot':

    model= load_gemini_pro_model()

    #Initilize chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session=model.start_chat(history=[])
    #streamllit page title
    st.title("🤖 ChatBot")

    #Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.part[0].text)


    # input field for user message
    user_prompt=st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response= st.session_state.chat_session.send_message(user_prompt)

        #Display Gemini pro response
        with st.chat_message("assistant "):
            st.markdown(gemini_response.text)
# Image captioning page
if  selected=="Image Captioning"
    #Streamlit page title
    st.title("Snap Narrate")

    uploaded_image=st.file_uploader("Upload on image....",type=["jpg,jpeg","png"])

    if st.button("Generate Caption"):
        image= Image.open(uploaded_image)
        col1,col2=st.columns(2)
        with col1:
            resized_image=image.resize(800,500)
            st.image(resized_image)
            default_prompt="write a short caption for this image"

            # getting the response from gemini -pro model
            caption =gemini_pro_vision_response(default_prompt,image)
        with col2:
            st.info(caption)

# text embedding page
if selected== "Embed text":
    st.title("Embed Text")

    #input text box
    input_text=st.text_area(label="",placeholder="Enter the text embedding ")

    if st.button("get Embeddings"):
        response=embeddings_model_response(input_text)
        st.marksdown(response)

#question and answer page
if selected=="Ask me anything":
    st.title("? Ask me question ")
    #text box to enter prompt
    user_prompt=st.text_area(label="",placeholder="Ask Gemini-Pro....")

    if st.button("Get an answer"):
        resposne=gemini_pro_response(user_prompt)
        st.markdown(response)
