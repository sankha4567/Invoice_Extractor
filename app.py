import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import base64
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from PIL import Image
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm=ChatGoogleGenerativeAI(
  model="gemini-3.5-flash",
  temperature=0.5
)
def get_gemini_response(input_prompt,uploaded_file,user_prompt):
 image_bytes=uploaded_file.getvalue()
 base64_image= base64.b64encode(
   image_bytes
 ).decode("utf-8")
 message=HumanMessage(
   content=[
     {
       "type":"text",
       "text":input_prompt
     },
     {
       "type":"image_url",
       "image_url":{
         "url":(
           f"data:{uploaded_file.type};base64,"
           f"{base64_image}"
         )
       }
     }
     ,{
       "type":"text",
      "text":user_prompt  
     }
   ]
 )
 parser=StrOutputParser()
 chain=llm | parser
 response=chain.invoke([message])
 return response





# Streamlit UI
st.set_page_config(
    page_title="Multi Language Invoice Extractor"
)

st.header("Invoice Extractor Demo")

user_input = st.text_input(
    "Input Prompt:",
    key="input_prompt"
)

uploaded_file = st.file_uploader(
    "Upload an image of the invoice",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Invoice",
        use_container_width=True
    )


submit_button = st.button("Tell me about the invoice")


input_prompt = """
You are an expert in understanding invoices.

We will upload an invoice image and you will have to
answer any questions related to the invoice.
"""


if submit_button:

    if image is None:
        st.error("Please upload an invoice image.")

    else:
        response = get_gemini_response(
            input_prompt,
              uploaded_file,
            user_input
        )

        st.subheader("Response from System")
        st.write(response)