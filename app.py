import gradio as gr
from PIL import Image
import pytesseract

def perform_ocr(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')
    return text

interface = gr.Interface(fn=perform_ocr, inputs="image", outputs="text")
interface.launch(share=True)

def search_text(keyword, text):
    if keyword.lower() in text.lower():
        return f'Keyword "{keyword}" found!'
    return f'Keyword "{keyword}" not found.'

def process_image_with_search(image, keyword):
    text = perform_ocr(image)
    search_result = search_text(keyword, text)
    return text, search_result

interface = gr.Interface(fn=process_image_with_search, 
                         inputs=["image", "text"], 
                         outputs=["text", "text"])
interface.launch(share=True)