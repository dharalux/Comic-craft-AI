from pathlib import Path
from datetime import datetime

from fpdf import FPDF


BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXPORT_DIR = (
    BASE_DIR /
    "static" /
    "exports"
)


def save_pdf(
    panels,
    title
):

    EXPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        "comic_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".pdf"
    )

    output = EXPORT_DIR / filename


    pdf = FPDF(
        "P",
        "mm",
        "A4"
    )

    pdf.set_auto_page_break(
        True,
        15
    )


    for panel in panels:

        pdf.add_page()

        pdf.set_font(
            "Helvetica",
            "B",
            20
        )

        pdf.cell(
            0,
            12,
            f"Panel {panel.panel_number}",
            ln=True
        )


        image_path = (
            BASE_DIR /
            panel.image_path.lstrip("/")
        )


        if image_path.exists():

            pdf.image(
                str(image_path),
                w=180
            )


        pdf.ln(5)

        pdf.set_font(
            "Helvetica",
            "B",
            13
        )

        pdf.multi_cell(
            0,
            8,
            panel.title
        )


        pdf.set_font(
            "Helvetica",
            "",
            11
        )

        pdf.multi_cell(
            0,
            7,
            panel.narration
        )


    pdf.output(
        str(output)
    )


    return (
        f"/static/exports/{filename}"
    )