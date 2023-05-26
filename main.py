from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from uno import *
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

SECRET = os.getenv("SECRET")

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")
async def root():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/homepage")
async def demo_get():
    driver=createDriver()
    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


