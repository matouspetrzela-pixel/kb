from PIL import Image, ImageDraw, ImageFont

def create_icon(size):
    # RGB obrázek (bez průhlednosti)
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    # Gradient modrá → fialová
    for y in range(size):
        ratio = y / size
        r = int(37 + (124 - 37) * ratio)
        g = int(99 + (58 - 99) * ratio)
        b = int(235 + (237 - 235) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # Bílé písmeno "S"
    font_size = int(size * 0.65)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", font_size)
    except:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)

    text = "S"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2 - bbox[0]
    y = (size - text_height) // 2 - bbox[1]

    draw.text((x, y), text, fill='white', font=font)

    return img

# Vytvoř ikony
for size in [16, 48, 128]:
    icon = create_icon(size)
    icon.save(f'icons/icon{size}.png', 'PNG')
    print(f'Ikona {size}x{size} vytvorena')

print('Hotovo!')
