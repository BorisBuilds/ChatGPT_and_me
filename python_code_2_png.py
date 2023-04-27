# This program creates a web application that allows users to enter Python code and get a syntax-highlighted PNG image of the code as output. 
# The web application is built using the Bottle micro web framework and uses Pygments for syntax highlighting and Pillow (a fork of PIL) to generate the PNG image. 

# Created by BorisBuilds and ChatGPT. © 2023

import io
import pygments
import pygments.lexers
import pygments.formatters
from PIL import Image, ImageDraw, ImageFont
from bottle import route, run, HTTPResponse, redirect, request, template

@route('/')
def index():
    # Render the HTML template for the form
    return template('''
        <html>
        <body>
            <form action="/highlight" method="get">
                <label for="code">Code:</label><br>
                <textarea id="code" name="code" rows="10" cols="50"></textarea><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

@route('/highlight')
def highlight():
    # Get the value of the "code" parameter, or use the default text if it's not provided
    code = request.query.get('code', "print('hello world')")

    # Define the syntax highlighting style and get the lexer for the provided code
    lexer = pygments.lexers.get_lexer_by_name('python', stripall=True)

    # Highlight the code using Pygments and get the image data
    formatter = pygments.formatters.ImageFormatter(font_name='DejaVu Sans Mono', line_numbers=False)
    image_data = pygments.highlight(code, lexer, formatter)

    # Load the image data into a PIL image
    image = Image.open(io.BytesIO(image_data)).convert('RGBA')

    # Create a blank image with the same size as the highlighted text image
    width, height = image.size
    bg_color = (255, 255, 255, 255)
    image_bg = Image.new('RGBA', (width, height), bg_color)

    # Draw the highlighted text image onto the blank image
    image_bg.paste(image, (0, 0), image)

    # Save the image to a buffer
    buffer = io.BytesIO()
    image_bg.save(buffer, format='PNG')
    image_bytes = buffer.getvalue()

    # Return the image bytes as a HTTP response
    response = HTTPResponse(body=image_bytes, status=200, headers={'Content-Type': 'image/png'})
    return response

# Run the webserver on localhost:8080
run(host='localhost', port=8080)
