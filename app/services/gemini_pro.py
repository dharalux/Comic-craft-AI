from app.config import get_settings

from app.models import PromptRequest

from app.services.gemini_client import (
    get_gemini_client
)


def generate_story(
    request: PromptRequest,
    outline: str
):

    settings = get_settings()

    client = get_gemini_client()

    prompt = f"""
Create narration and dialogue for a
five panel comic.

Original story:
{request.story_prompt}

Character:
{request.character_name}

Setting:
{request.setting}

Tone:
{request.tone}

Comic outline:
{outline}

Rules:

- Keep five panels.
- Give every panel narration.
- Give every panel a short caption.
- Add natural dialogue.
- Keep the story simple.
- Keep the character consistent.
- Give the comic a satisfying ending.
"""

    response = client.models.generate_content(
        model=settings.gemini_pro_model,
        contents=prompt
    )

    return response.text