from PIL import Image, ImageDraw, ImageFont
import os

# Vytvoř složku icons
os.makedirs('icons', exist_ok=True)

def create_gradient_icon(size):
    # Vytvoř obrázek
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    # Gradient modrá → fialová
    for y in range(size):
        # Interpolace mezi barvami
        ratio = y / size
        r = int(37 + (124 - 37) * ratio)
        g = int(99 + (58 - 99) * ratio)
        b = int(235 + (237 - 235) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # Bílé písmeno "S"
    font_size = int(size * 0.6)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

    # Vycentruj text
    bbox = draw.textbbox((0, 0), "S", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.05)

    draw.text((x, y), "S", fill='white', font=font)

    # Zaoblené rohy
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    radius = int(size * 0.15)
    mask_draw.rounded_rectangle([(0, 0), (size, size)], radius=radius, fill=255)

    # Aplikuj masku
    output = Image.new('RGBA', (size, size))
    output.paste(img, (0, 0))
    output.putalpha(mask)

    return output

# Vytvoř všechny 3 ikony
for size in [16, 48, 128]:
    icon = create_gradient_icon(size)
    icon.save(f'icons/icon{size}.png')
    print(f'Vytvorena ikona {size}x{size}')

print('\nVsechny ikony vytvoreny!')
