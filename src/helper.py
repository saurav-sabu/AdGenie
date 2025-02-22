from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from src.prompt import *

load_dotenv()

def create_ad_response(brand_name,product_description,target_audience,tone):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    chain = ad_prompt | llm | StrOutputParser()
    response = chain.invoke({"brand_name": brand_name, "product_description": product_description, "target_audience": target_audience, "tone": tone})
    return response
    