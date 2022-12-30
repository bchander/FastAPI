# FastAPI
Implementation of web API using FastAPI 

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
