# This program takes a PNG file and a JPEG file, and merges them into a new PNG file.
# The JPEG file is centered in front of the PNG file, and scaled to 70% of the PNG file width while maintaining its aspect ratio.
# The resulting image is saved as a new PNG file in the same directory as this program.
# Created by ChatGPT and BorisBuilds.

from PIL import Image

# Open the PNG and JPEG files
png_image = Image.open("code.png")
jpg_image = Image.open("webcam.jpg")

# Get the dimensions of the PNG image
png_width, png_height = png_image.size

# Calculate the width of the JPEG image at 70% of the width of the PNG image
jpg_width = int(0.7 * png_width)

# Calculate the height of the JPEG image while maintaining its aspect ratio
jpg_height = int(jpg_width * jpg_image.height / jpg_image.width)

# Calculate the x and y coordinates to center the JPEG image
x = int((png_width - jpg_width) / 2)
y = int((png_height - jpg_height) / 2)

# Create a new RGBA image with a transparent background and paste the PNG and JPEG images onto it
new_image = Image.new("RGBA", (png_width, png_height), (0, 0, 0, 0))
new_image.paste(png_image, (0, 0))
new_image.paste(jpg_image.resize((jpg_width, jpg_height)), (x, y))

# Save the new image as a PNG file
new_image.save("collage.png", "PNG")
