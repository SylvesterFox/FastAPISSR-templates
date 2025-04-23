from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn


class App:
    def __init__(self):
        self.app = FastAPI() 
        self.templates = Jinja2Templates(directory="templates") # Папка с html шаблонами
        self._setup_routes() # Инициирование путей

    def _setup_routes(self):
        # Тут у нас ролты
        # Пример с get запросом 
        @self.app.get("/", response_class=HTMLResponse)
        async def root_route(request: Request):
            return self.templates.TemplateResponse("index.html", {
                "request": request,
                "title": "Hello Gondonio!"
            })
        
        @self.app.get("/aboutme", response_class=HTMLResponse)
        async def about_me_page(request: Request):
            return self.templates.TemplateResponse("about.html", {"request": request})
        
        # Пример с post запросом
        @self.app.post("/aboutme", response_class=HTMLResponse)
        async def post_exemple(request: Request, name: str =  Form(...)):
            message = f"Я, {name}"
            return self.templates.TemplateResponse("about.html", {
                "request": request,
                "message": message
            })


if __name__ == "__main__":
    # Запуск сервера через uvicorn
    server = App()
    uvicorn.run(server.app, host="localhost", port=8080, workers=True)