from pathlib import Path
import traceback

from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.models import PromptRequest
from app.services.comic_service import create_comic


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

router = APIRouter()


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "error": None
        }
    )


@router.post("/generate")
def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        data = PromptRequest(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style
        )

        title, panels, pdf_path = create_comic(data)

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "title": title,
                "layout": panels,
                "pdf_path": pdf_path
            }
        )

    except Exception as error:
        print("\n========== COMICCRAFT ERROR ==========")
        traceback.print_exc()
        print("=======================================\n")

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "error": str(error)
            },
            status_code=500
        )