from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from agents.orchestrator import OrchestratorAgent
from agents.revenue import RevenueAgent
from agents.tax import TaxAgent
import uvicorn

app = FastAPI()

# Setup paths
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Agents
orchestrator = OrchestratorAgent()
revenue_agent = RevenueAgent()
tax_agent = TaxAgent()

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: str = Form(...)):
    # 1. Orchestrate
    routing = orchestrator.route_request(message)
    dept = routing["target_department"]
    lang = routing["detected_language"]
    
    # 2. Delegate
    if dept == "revenue":
        response = revenue_agent.process_task(message, lang)
    elif dept == "tax":
        response = tax_agent.process_task(message, lang)
    else:
        response = orchestrator.process(message)
        
    return {
        "reply": response,
        "department": dept.upper(),
        "language": lang.capitalize()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
