from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime
import openpyxl
import os

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модели данных
class Homework(BaseModel):
    subject: str
    date: str  # "YYYY-MM-DD"
    text: str

# Данные предметов
subjects_map = {
    1: ["Белорусский", "Английский", "Математика", "История"],
    2: ["Русский", "Литература", "Математика", "Биология"],
    3: ["Математика", "Белорусский", "Химия"],
    4: ["Английский", "Химия", "Физика"],
    5: ["Физика", "Биология", "География"]
}

# API endpoints
@app.get("/subjects/{day_num}")
def get_subjects(day_num: int):
    if day_num not in subjects_map:
        raise HTTPException(status_code=404, detail="День не найден")
    return {"subjects": subjects_map[day_num]}

@app.post("/save_homework")
def save_homework(hw: Homework):
    # Здесь должна быть ваша логика сохранения в Excel
    # Например:
    try:
        # Код для сохранения в Excel
        return {"status": "ok", "message": f"ДЗ по {hw.subject} сохранено!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_homework/{date}")
def get_homework(date: str):
    try:
        # Здесь должна быть ваша логика чтения из Excel
        # Заглушка для примера:
        return {"homeworks": ["Математика: стр. 50", "Физика: задача 3"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)