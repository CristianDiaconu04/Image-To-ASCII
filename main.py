import sys
from PIL import Image
import tkinter as tk

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def imageToASCII(image_path):
    # Open and convert the image to grayscale
    greyedIMG = Image.open(image_path).convert('L')
    width, height = greyedIMG.size

    asciiPic = []

    # Get all the ASCII characters based on pixel brightness
    for y in range(height):
        line = ""
        for x in range(width):
            brightness = greyedIMG.getpixel((x, y))
            line += ASCII_CHARS[brightness // 25]
        asciiPic.append(line)

    return asciiPic

def drawASCIIArt(asciiPic, canvas, canvas_width, canvas_height):
    canvas.delete("all")
    font_size = min(canvas_width // len(asciiPic[0]), canvas_height // len(asciiPic))
    font = ('Courier', font_size)
    text = "\n".join(asciiPic)
    canvas.create_text(canvas_width // 2, canvas_height // 2, text=text, font=font, anchor=tk.CENTER)

if len(sys.argv) != 2:
    print("Usage: python main.py <image_path>")
    sys.exit(1)

# Get the filepath from command line
filePath = sys.argv[1]

# Generate the ASCII image
asciiPic = imageToASCII(filePath)

# Create a display window
root = tk.Tk()
root.title("ASCII Art")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Redraw the image whenever window is resized
def on_resize(event):
    canvas_width = event.width
    canvas_height = event.height
    drawASCIIArt(asciiPic, canvas, canvas_width, canvas_height)

canvas.bind("<Configure>", on_resize)

root.mainloop()
