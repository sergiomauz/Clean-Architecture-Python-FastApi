"""
    ToDo: DocString
"""

from fastapi import FastAPI
from presentation.routes import router as api_router

app = FastAPI(
    title = "Clean Architecture",
    description = "Prueba de FastApi",
    version = "1.0"
)
app.include_router(api_router)

if __name__ == "__main__":
    app.run(debug = True)
