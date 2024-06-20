from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_prompt, image):
    # Assuming generate_content can handle a PIL Image directly
    response = model.generate_content([input_prompt, image])
    return response.text

st.set_page_config(
    page_title="AI-Calories Doctor",
    page_icon="🧑‍⚕️",
    layout="centered",
    
)
st.title("AI-Calories Advisor 🧑‍⚕️")

uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", 'png'])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image....", use_column_width=True)

submit = st.button("Tell me about the total calories!")

input_prompt = """
You are an expert in nutrition where you need to see the food items from the image
and calculate the total calories, also provide the details of every food items with calories intake in the format below:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----

Finally, you can also mention whether the food is healthy or not and also mention the percentage split
of the ratio of carbohydrates, fats, fibers, sugar, and other important things required in our diet.

give some suggestion which food item names and calories with it so i can replace and add to balanced the healthy diet. 
"""

##### Streamlit Initalization ####


if submit and image is not None:
    response = get_gemini_response(input_prompt, image)
    st.header("Advice from AI-Nutritionist : 🍴")
    with st.container(border=True):
        st.write(response)
st.write("----------------------------------------------------------------------")
link='AI-Nutritionist Doctor 💪❤️ : [Click and get a healthy DIET PLAN !](https://ai-dietplan-doctor-by-kartavya.streamlit.app/)'
st.markdown(link,unsafe_allow_html=True)



st.header('', divider='rainbow')
with st.container(border=True):
    st.markdown('''
        Developed by KARTAVYA MASTER :8ball:
    ''')

    link='PORTFOLIO : [CLICK ME](https://mydawjbhdas.my.canva.site/aiwithkartavya)'
    st.markdown(link,unsafe_allow_html=True)
    
    
