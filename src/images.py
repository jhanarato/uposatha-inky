from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

WIDTH = 400
HEIGHT = 300

WHITE = 0
BLACK = 1
YELLOW = 2

def make_image(content: str) -> Image:
    image = Image.new(mode="P", size=(WIDTH, HEIGHT), color=WHITE)
    draw = ImageDraw.Draw(image)
    draw_heading(draw, "Uposatha")
    draw_underline(draw)
    draw_content(draw, content)
    return image

def draw_heading(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=36)
    x_coord = centered_x_coord(font.getlength(text))
    y_coord = 10
    draw.text((x_coord, y_coord), text, BLACK, font)

def draw_underline(draw: ImageDraw):
    y_coord = 70
    draw.line([50, y_coord, WIDTH - 50, y_coord], BLACK, 2)

def draw_content(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold,
                              size=32)
    y_coord = 100
    width = draw.textbbox((0,0), text, font)[2]
    x_coord = centered_x_coord(width)

    draw.multiline_text(
        xy=(x_coord, y_coord),
        text=text,
        font=font,
        fill=BLACK,
        align="center",
        spacing=20
    )

def centered_x_coord(object_width: int) -> int:
    return round((WIDTH / 2) - (object_width / 2))
