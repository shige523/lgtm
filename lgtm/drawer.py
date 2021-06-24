from PIL import Image, ImageDraw, ImageFont

# 画面全体に対する目サージ描画エリアの比率
MAX_RATIO = 0.8

# フォント関連の定数
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24
# winの場合はdir C:\windows\fonts\*.*で表示されるフォントファイル名称を使用する
# FONT_NAME = "arial.ttf"
FONT_NAME = "/Library.Fonts/Arial Bold.ttf"
FONT_COLOR_WHITE = (255, 255, 255, 0)

# output関連の定数
OUTPUT_NAME = "output.png"
OUTPUT_FORMAT = "PNG"


def save_with_message(fp, message):
    """[summary]

    Args:
        fp ([type]): [filepath]
        message ([string]): [displaymessage]
    """
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    # メッセージを描画できる領域のサイズ
    # タプルの要素ごとに計算する
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)

        text_width, text_height = draw.textsize(message, font=font)
        # print(message_area_width)
        # print(text_width)
        # print(message_area_height)
        # print(text_height)
        # 描画に必要なサイズ
        w = message_area_width - text_width
        h = message_area_height - text_height

        if w > 0 and h > 0:
            position = (
                ((image_width - text_width) / 2),
                ((image_height - text_height) / 2),
            )

            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break

    # 画像の保存
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
