from app.models import ComicPanel


def build_layout(
    outline,
    story,
    image_paths
):

    panels = []

    for index in range(5):

        panels.append(
            ComicPanel(
                panel_number=index + 1,

                title=f"Panel {index + 1}",

                scene_description=(
                    outline
                ),

                image_prompt=(
                    f"Comic illustration "
                    f"for panel {index + 1}"
                ),

                image_path=image_paths[index],

                caption=(
                    f"Panel {index + 1}"
                ),

                narration=story,

                dialogue=[]
            )
        )

    return panels