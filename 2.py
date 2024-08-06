import requests
import gradio as gr
def fetch_mars_rover_photos(sol):
    api_key = "Rn9JeYsKtgwLx0sYMy2Bexeh8x5ZVRUJjEeQYgVY"
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={api_key}'
    response = requests.get(url)
    return response.json()

def a(text):
    return fetch_mars_rover_photos(text)
iface = gr.Interface(fn=a, inputs="text",outputs="text")

iface.launch()