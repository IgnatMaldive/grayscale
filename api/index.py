from flask import Flask, request, render_template_string, send_from_directory
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

HTML = '''
<!doctype html>
<html lang="en">
<head>
  <title>Image Upload and Process</title>
</head>
<body>
<h1>Upload an image to process into grayscale steps</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
<div>
  {% for image in images %}
  <img src="{{ image }}" style="width:200px;">
  {% endfor %}
</div>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    images = []
    if request.method == 'POST':
        # Save the uploaded file
        file = request.files['file']
        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            process_image(filename)
            # Add a timestamp to the image URL to prevent caching
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            images = [f'/processed/{i+1:02d}.jpg?{timestamp}' for i in range(10)]
    return render_template_string(HTML, images=images)


def process_image(image_path):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    gray_array = np.array(gray_image)
    num_steps = 10
    step_range = 256 // num_steps

    # Specify the path to a TrueType font (.ttf) and set the desired size
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this path to a valid one on your server
    font_size = 48  # You can adjust this size as needed
    font = ImageFont.truetype(font_path, font_size)

    for i in range(num_steps):
        lower_bound = i * step_range
        upper_bound = (i + 1) * step_range
        mask = (gray_array >= lower_bound) & (gray_array < upper_bound)

        # Create an RGB image with a black background
        output_image = np.zeros((*gray_array.shape, 3), dtype=np.uint8)
        output_image[mask] = [255, 0, 0]  # Set masked regions to red

        pil_image = Image.fromarray(output_image, 'RGB')
        draw = ImageDraw.Draw(pil_image)
        text = f'{i+1}'
        textwidth, textheight = draw.textsize(text, font=font)
        width, height = pil_image.size
        x, y = width - textwidth - 10, 10  # Ensure the text is not too close to the edge
        draw.text((x, y), text, font=font, fill="white")

        pil_image.save(os.path.join(PROCESSED_FOLDER, f'{i+1:02d}.jpg'))



@app.route('/processed/<filename>')
def send_file(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
