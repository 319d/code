"""
API文档: https://api.nasa.gov/ (Mars Rover Photos栏中)

申请API KEY: https://api.nasa.gov/
"""
import requests
import gradio as gr

# Function to fetch Mars Rover photos
def fetch_mars_rover_photos(api_key, cam, sol=1000, page=1):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    
    params = {
        'api_key': api_key,
        'camera':cam,
        'sol': sol,
        'page': page
    }
    print(params)
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Gradio interface setup
def mars_rover_photo_interface(sol,page,cam):
    """
    本函数主要调用API请求函数, 并处理API请求得到的JSON数据, 提取出图片的URL并返回
    
    通常一个API文档要说清楚它的输入参数和输出数据格式, 但NASA这个API文档没说清楚输出数据格式
    我们可以通过把返回的数据打印出来, 分析它的JSON结构, 用Key作为索引, 提取出我们需要的数据
    关于JSON: https://www.runoob.com/json/json-syntax.html
    """
    
    api_key = "KKDMzTTxJzgLJBkaMqw0ZfMAyTBtLdKUmneFbPD8" # 请替换为你自己的API KEY
    data = fetch_mars_rover_photos(api_key, cam=cam,sol=sol,page=page)
    print(data)
    if data:
        print(1)
        photos = data.get('photos', [])
        photo_urls = [photo['img_src'] for photo in photos]
        print(photo_urls)
        return photo_urls
    else:

        return []

# Define the input components for the Gradio interface
sol_input = gr.Number(label="Martian Sol", value=1000)
page_input = gr.Number(label="Page", value=1)
cam_input = gr.Text(label="Camera",value="FHAZ")

# Create the Gradio interface
gr.Interface(fn=mars_rover_photo_interface, 
        inputs=[sol_input,  page_input, cam_input],
        outputs=gr.Gallery(label="Mars Rover Photos")).launch()
