"""
Create an application icon for the PDF Splitter
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 256x256 image with a gradient background
size = 256
image = Image.new('RGB', (size, size), '#4A90E2')

draw = ImageDraw.Draw(image)

# Draw a simple PDF icon design
# Background rectangle (representing a document)
doc_color = '#FFFFFF'
doc_x1, doc_y1 = 50, 30
doc_x2, doc_y2 = 206, 226

# Draw document shadow
shadow_offset = 4
draw.rectangle([doc_x1 + shadow_offset, doc_y1 + shadow_offset,
                doc_x2 + shadow_offset, doc_y2 + shadow_offset],
               fill='#00000040')

# Draw document
draw.rectangle([doc_x1, doc_y1, doc_x2, doc_y2], fill=doc_color, outline='#333333', width=3)

# Draw folded corner
corner_size = 30
corner_points = [
    (doc_x2 - corner_size, doc_y1),
    (doc_x2, doc_y1 + corner_size),
    (doc_x2 - corner_size, doc_y1 + corner_size)
]
draw.polygon(corner_points, fill='#E0E0E0', outline='#333333')
draw.line([(doc_x2 - corner_size, doc_y1), (doc_x2 - corner_size, doc_y1 + corner_size)],
          fill='#333333', width=2)

# Draw scissors/split symbol
scissors_color = '#FF6B6B'
# Scissors blades (using lines to create X shape)
center_x, center_y = 128, 128
blade_length = 40
draw.line([(center_x - blade_length, center_y - blade_length),
           (center_x + blade_length, center_y + blade_length)],
          fill=scissors_color, width=8)
draw.line([(center_x + blade_length, center_y - blade_length),
           (center_x - blade_length, center_y + blade_length)],
          fill=scissors_color, width=8)

# Draw circles at scissors pivot points
draw.ellipse([center_x - 10, center_y - 10, center_x + 10, center_y + 10],
             fill=scissors_color, outline='#FFFFFF', width=2)

# Draw horizontal lines representing text on document
line_color = '#666666'
line_y_start = 60
line_spacing = 20
for i in range(3):
    y = line_y_start + (i * line_spacing)
    draw.line([(doc_x1 + 20, y), (doc_x2 - 40, y)], fill=line_color, width=3)

# Draw lines below scissors
line_y_start = 160
for i in range(3):
    y = line_y_start + (i * line_spacing)
    draw.line([(doc_x1 + 20, y), (doc_x2 - 40, y)], fill=line_color, width=3)

# Save as ICO file (Windows icon format)
icon_path = os.path.join(os.path.dirname(__file__), 'pdf_splitter_icon.ico')
image.save(icon_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])

print(f"Icon created successfully: {icon_path}")
