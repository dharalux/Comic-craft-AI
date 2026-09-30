from pathlib import Path

from PIL import Image, ImageDraw

from app.config import get_settings


BASE_DIR = Path(__file__).resolve().parent.parent.parent

OUTPUT_DIR = (
    BASE_DIR /
    "static" /
    "panels"
)


def generate_image(
    prompt: str,
    panel_number: int
):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        f"panel_{panel_number}.png"
    )

    output = OUTPUT_DIR / filename


    settings = get_settings()


    if settings.mock_image_generation:

        image = Image.new(
            "RGB",
            (800, 500),
            "#f4ead7"
        )

        draw = ImageDraw.Draw(
            image
        )

        draw.rectangle(
            (10, 10, 790, 490),
            outline="#222222",
            width=5
        )

        draw.text(
            (40, 40),
            f"COMIC PANEL {panel_number}",
            fill="#222222"
        )

        draw.text(
            (40, 120),
            prompt[:500],
            fill="#333333"
        )

        image.save(output)

    else:

        raise RuntimeError(
            "Real image generation is "
            "not enabled in this simple version."
        )


    return (
        f"/static/panels/{filename}"
    )