from fastapi import FastAPI

app = FastAPI(title="Mini CRM")

@app.get("/")
def root():
    return {"message": "Welcome to Mini CRM API"}
