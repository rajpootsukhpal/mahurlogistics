from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files (CSS/JS/images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Mahur Logistics"})

@app.post("/contact")
async def contact(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Here you can save to DB or send email
    return {"status": "success", "name": name, "email": email, "message": message}
