from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
import math
import io

baseW = 504
baseH = 384


def build_image(graph_blob, conf):
    """
    Using the graph data from before, and the data frame we want to build an
    easily digestible image showing key metrics to help assess current status.
    """
    with Image(width=baseW, height=baseH, background='#ffffff') as base:
        with Image(blob=graph_blob) as grph:
            base.composite(grph, math.floor(
                baseW / 7), math.floor(baseH / 5))

        draw_header(base, conf)
        base.format = 'png'
        base.save(filename=f"fig-{conf['name'].replace(' ','_')}.png")


def draw_header(base, conf):

    # Draw a header background.
    with Drawing() as draw:
        draw.fill_color = '#d38fc5'
        draw.rectangle(left=0, top=0, width=baseW, height=math.floor(baseH/8))
        draw(base)

    # Layer header text ontop of background.
    with Drawing() as draw:
        draw.font_size = 24
        draw.text(0, 36, f"COVID-19 in {conf['name']}: New Cases Daily")
        draw(base)
