
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, EmailStr
from app.agent.agent import NewsAgent
from app.tools import pdf_tool, email_tool

router = APIRouter()

agent = NewsAgent()

@router.get("/ping")
def ping():
    return {"message": "pong"}

class QueryRequest(BaseModel):
    query: str

class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    body: str
    query: str

@router.post("/news")
def get_news(req: QueryRequest):
    result = agent.plan_and_execute(req.query)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/news/pdf")
def get_news_pdf(req: QueryRequest):
    result = agent.plan_and_execute(req.query)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    filename = "news_report.pdf"
    pdf_tool.generate_pdf_report(result["summaries"], filename)
    # In real app, return file response
    return {"pdf": filename, "message": "PDF generated (placeholder)"}

@router.post("/news/email")
def send_news_email(req: EmailRequest):
    result = agent.plan_and_execute(req.query)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    filename = "news_report.pdf"
    pdf_tool.generate_pdf_report(result["summaries"], filename)
    email_tool.send_email(req.recipient, req.subject, req.body, attachment=filename)
    return {"message": f"Email sent to {req.recipient} (placeholder)"}
