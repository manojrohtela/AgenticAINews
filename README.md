# Agentic AI News Assistant

## Overview

This project is an agentic AI-powered news assistant built with Python and FastAPI. It classifies user queries (e.g., 'latest news', 'stock news', 'sports news'), fetches relevant articles from free RSS feeds, summarizes them using a Hugging Face transformer, and returns concise answers. Optional features include PDF report generation and email delivery.

## Features

- Query classification (latest, stock, sports)
- Fetches news from Google News, MoneyControl, ESPN, etc.
- Summarizes articles using Hugging Face transformers
- Modular agent logic, tools, and API endpoints
- Optional PDF report (ReportLab) and email delivery (SMTP)
- Error handling and rate-limiting

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Sample Queries

- Give me latest news
- Show me stock market news
- What are the top sports updates today

## Legal Disclaimer

This project is for educational and demonstration purposes only. News content is fetched from public RSS feeds. Please respect the terms of use of each news provider. No commercial use intended.
