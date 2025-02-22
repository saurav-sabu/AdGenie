import streamlit as st
from src.helper import *

st.set_page_config(
    page_title="AdGenie - AI Ad Copy Generator",
    page_icon="📝"  
)

# Streamlit UI
st.title("✨ AdGenie - AI-Powered Ad Copy Generator")
st.markdown("Create personalized ad copy based on your brand, product, and audience!")

brand_name = st.text_input("Brand Name", "Your Brand")
product_description = st.text_area("Product/Service Description", "Describe your product or service")
target_audience = st.text_input("Target Audience", "Who is your product for?")
tone = st.selectbox("Select Tone", ["Exciting", "Professional", "Casual"])

if st.button("Generate Ad"):
    if brand_name and product_description and target_audience:
        ad_copy = create_ad_response(brand_name, product_description, target_audience, tone)
        
        st.subheader("✨ Generated Ad Copy")
        st.write(ad_copy)
        
    else:
        st.warning("Please fill in all the fields to generate ad copy.")