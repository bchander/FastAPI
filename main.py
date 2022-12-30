# -*- coding: utf-8 -*-
"""
FastAPI for creating an API to read user-uploaded image and output 
an artistic image of the same by using k-means image clustering (quantition)

For prelimiery steps on how to make this code run, check the end of this code 


@author: Bhanu Chander V,
Github: bchander (https://github.com/bchander)
"""

#import io
from io import BytesIO
from PIL import Image
import numpy as np
#import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
#from pydantic import BaseModel

import matplotlib.pyplot as plt
import matplotlib.image as img
from sklearn.cluster import KMeans

#import matplotlib as mpl
#mpl.rcParams['figure.dpi']= 300

def read_image(file): #-> Image.Image:
    PIL_image = Image.open(BytesIO(file))
    return PIL_image


app = FastAPI()
#IMAGE = []
@app.post("/Upload_Image/")
async def create_upload_file(img_file: UploadFile = File(...)):
    
    #image = read_image(img_file)
    #image = await img_file.read()
    image = read_image(await img_file.read())
    image.save("image.png")
    #IMAGE.append(image)
    '''memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)'''
    return {"filename": img_file.filename}

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/Output_Image/", responses = {200: {"description": "output image form the code"}})
def generate_image() -> Image.Image:
    
    '''......Below code block does image classification...'''
    image = img.imread("image.png")
    if image.shape[2] ==4: 
        image = image[:,:, :-1]
    #image = image[:,:,:-1]
    h,w,d = image.shape[0], image.shape[1], image.shape[2]
    img_2D = image.reshape(h*w, d)
    #del img_input
    kmeans_model = KMeans(n_clusters=10) # we shall retain only 7 colors
    cluster_labels = kmeans_model.fit_predict(img_2D)
    rgb_cols = kmeans_model.cluster_centers_
    img_quant = np.reshape(rgb_cols[cluster_labels],(h,w,d))
    plt.imsave("output\img_art_leena.png", img_quant)
    #img_quant.save("img_art.png")

    return FileResponse("output\img_art_leena.png", media_type="image/png")
    #return FileResponse("image.png", media_type="image/png")


'''
Steps to run this code:

    I used Anaconda to run this code. we can do it in command prompt as well. Steps that I followed in Ananconda
    1. In your local disk (PC) Save The provided code with all the support files (requirement) in one folder. This will be your working directory. Also read through RaedMe.txt for more info
    2. Copy this folder's path. 
    3. Navigate to the environment that you nmay have created to run FastAPI. If you haven't, create one environment
    4. In Anaconda, you can do 'conda deactivate' then 'conda activate your_env_name'
    5. Then navigate to the directory using 'cd path_to_working_directory'
    6. If you are running for the first time you need to install the dependencies and libraries using requirements.txt
    7. Install requirements.txt by 'pip install -r requirements.txt'
    8. Now your environment is ready and laoded with the required dependencies. 
    9. It is time to run FastAPI. Uvicorn is what we use
    10. Uvicorn is an ASGI web server implementation for Python. It's (simplified) the binding element that handles the web connections from the browser or api client and then allows FastAPI to serve the actual request.
    11. using Uvicorn we run our main program. In the main program we have defined 'app' as our FastAPI class object we run the main by 'uvicorn main:app --reload' 
    (Note that --reload makes the server restart automatically after code changes)
    12. The code shall be running in the server and the link to the server will be displayed. You will see something like 'Application startup complete' 
    13. Now go the link in your browser 'http://127.0.0.1:8000' andd /docs, something like 'http://127.0.0.1:8000/docs'
    14. Click on Post > try It Out > Choose file and you can upload an image from your system's disk drive. Then hit 'execute' so that this post function will be executed
    15. Scroll down and click 'GET > try It Out > Execute' Now kmeans ML will be executed and the clustered image shall be visible. Note that I've coded ion a way to save the image in another folder 'output' You can play with the code as per convinience
    16. I will try to develop this code in the coming days to avoid the dependency on disk drive for images.

Hope this is interesting!

Refs: 
    https://www.youtube.com/watch?v=_BZGtifh_gw
    https://towardsdatascience.com/image-classification-api-with-tensorflow-and-fastapi-fc85dc6d39e8
    https://www.youtube.com/watch?v=23R2eI95S30&t=528s
    https://www.youtube.com/watch?v=vpTAqnAbowo
    
'''
