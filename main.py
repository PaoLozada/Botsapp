from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from appExecution import *
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse


app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://paolozada.com/"
    "http://127.0.0.1:8000",
    "https://paolozadabot.up.railway.app/",
    "https://botpaolozada.onrender.com/",
    # Agrega aquí los orígenes permitidos adicionales
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
SECRET = os.getenv("SECRET")

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")
async def root():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/botSearchOffer")
async def demo_get():
    driver=createDriver()
    listOffers = getBotSearchOffer(driver)
    driver.close()
    return JSONResponse(content={"listOffer": listOffers})

@app.get("/botSearchNewProducts")
async def demo_get(selectItem: str, categorys: str, options: str):
    driver=createDriver()
    listProducts = getBotSearchNewProducts(driver, selectItem, categorys, options)
    driver.close()
    return JSONResponse(content={"Products": listProducts})

@app.get("/botSearchJobs")
async def demo_get(city: str, filter_date: str, filter_job: str):
    driver=createDriver()
    listJobs = getBotSearchJob(driver, city, filter_date, filter_job)
    driver.close()
    return JSONResponse(content={"Jobs": listJobs})

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


