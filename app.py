import gradio as gr
import stylecloud
from PIL import Image
import os

def create_stylecloud(file, language, icon):
    text = file.decode("utf-8")
    output_file = 'stylecloud.png'

    # Generate the word cloud
    stylecloud.gen_stylecloud(
        text=text,
        icon_name=icon,
        size=500,
        output_name=output_file,
    )

    # Load the generated image
    image = Image.open(output_file)
    #image = image.resize((300, 300))  # Resize the image to 300x300 pixels

    # Return the image
    return image

with gr.Blocks() as demo:
    gr.Markdown('Kelime Bulutu Oluşturucu')

    with gr.Row():
        file_input = gr.File(label='Metin dosyasını yükle', type='binary')
    
    with gr.Row():
        language = gr.Radio(choices=['TR', 'En'], label='Dil Seçimi', value='TR')

    with gr.Row():
        icon = gr.Dropdown(choices=["fas fa-car", "fas fa-star-and-crescent", "fas fa-trophy", "fas fa-heart"],
                           label='İkon seçimi', value="fas fa-car")
    with gr.Row():
        create_button = gr.Button('Oluştur')
        output_image = gr.Image(label='Kelime Bulutu')

    create_button.click(
        create_stylecloud,
        inputs=[file_input, language, icon],
        outputs=[output_image]
    )

demo.launch(share=True)