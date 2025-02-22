# AdGenie

## 📌 Overview
This AI-powered ad copy generator, **AdGenie**, is a **Streamlit-based web application** that generates personalized ad copies for brands, products, and services. The tool allows users to specify their **brand name, product description, target audience, and preferred tone**.

## 🚀 Features
- **Personalized ad copy generation** tailored to your brand
- **Adjustable tone** selection (Exciting, Professional, Casual)
- **Call-to-action suggestions** to drive engagement
- **Hashtag generator** for better social media reach
- **Sentiment analysis** to fine-tune the output

## 🛠️ Setup & Installation

### 1️⃣ Create Conda Environment
```bash
conda create -p venv python=3.12 -y
```

### 2️⃣ Activate Conda Environment
```bash
conda activate venv/
```

### 3️⃣ Add API Key to `.env`
Create a `.env` file and add your **Google Gemini API key**:
```plaintext
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📋 Usage
1. Enter your **Brand Name**
2. Provide a **Product/Service Description**
3. Specify your **Target Audience**
4. Select a **Tone** for the ad copy
5. Click **"Generate Ad"**

## 🔧 Tech Stack
- **Python**
- **Streamlit** (for UI)
- **Google Gemini API** (for text generation)
- **Langchain** (LLM Framework)


## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss the proposed modifications.

---
🎯 **Developed with ❤️ to make your brand's voice stand out!**

