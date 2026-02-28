import google.generativeai as genai
import gradio as gr

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-pro")

def search(question):
    response = model.generate_content(question)
    return response.text

gr.Interface(
    fn=search,
    inputs="text",
    outputs="text",
    title="BharatSearch",
    description="Ask anything in Hindi, Kannada, or English"
).launch()
