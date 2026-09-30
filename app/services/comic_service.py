from app.models import PromptRequest

from app.services.gemini_flash import generate_outline
from app.services.gemini_pro import generate_story
from app.services.image_generator import generate_image
from app.services.layout_builder import build_layout
from app.services.exporters import save_pdf


def create_comic(request: PromptRequest):

    # STEP 1: Generate comic outline
    outline = generate_outline(request)

    # STEP 2: Generate full story
    story = generate_story(
        request,
        outline
    )

    # STEP 3: Generate images for all 5 panels
    images = []

    for number in range(1, 6):

        image_prompt = f"""
{request.art_style}

Character:
{request.character_name}

Setting:
{request.setting}

Story:
{request.story_prompt}

Panel:
{number}

Create a clear comic scene.
Do not include text, captions, or speech bubbles inside the image.
"""

        image = generate_image(
            image_prompt,
            number
        )

        images.append(image)

    # STEP 4: Build comic layout
    panels = build_layout(
        outline,
        story,
        images
    )

    # STEP 5: Create title
    title = (
        f"{request.character_name}'s "
        "Comic Adventure"
    )

    # STEP 6: Export PDF
    pdf = save_pdf(
        panels,
        title
    )

    return (
        title,
        panels,
        pdf
    )