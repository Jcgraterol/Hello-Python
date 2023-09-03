from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI!"


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

#app.mount("/static", StaticFiles(directory="static"), name="static")
