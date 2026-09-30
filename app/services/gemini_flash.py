from app.config import get_settings

from app.models import (
    ComicOutline,
    PromptRequest
)

from app.services.gemini_client import (
    get_gemini_client
)


def generate_outline(
    request: PromptRequest
):

    settings = get_settings()

    client = get_gemini_client()

    prompt = f"""
Create a five panel comic outline.

Story:
{request.story_prompt}

Character:
{request.character_name}

Setting:
{request.setting}

Tone:
{request.tone}

Art style:
{request.art_style}

Rules:

1. Exactly 5 panels.
2. Keep the same main character.
3. Create a clear beginning.
4. Create a problem.
5. Show the character solving the problem.
6. Finish with a satisfying ending.
7. Provide an image prompt for every panel.
8. Do not put text or speech bubbles inside images.
"""

    response = client.models.generate_content(
        model=settings.gemini_flash_model,
        contents=prompt
    )

    text = response.text

    return text