from PIL import Image, ImageDraw

def segment_image(image_path):
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 200, 200], outline="red", width=5)
    return image