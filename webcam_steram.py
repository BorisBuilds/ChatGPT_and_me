# This program captures an image from the webcam and renders it on a web page
# that refreshes every 5 seconds.

# The program uses OpenCV library to capture the image from the webcam and 
# encode it in JPEG format. It also uses the Bottle web framework to create 
# a web server and render an HTML template with the Base64-encoded image.

# To use this program, simply run it in a Python environment with the 
# required libraries installed. Then, open a web browser and navigate to 
# "http://localhost:8080" to view the live stream of the webcam.

# Made by BorisBuilds and ChatGPT.

from bottle import route, run, template
import cv2
import base64

# Path to the webcam (in this example, we are using the first webcam)
cap = cv2.VideoCapture(0)

@route('/')
def index():
    # Capture an image from the webcam
    ret, frame = cap.read()

    # Convert the image to JPEG format
    ret, jpeg = cv2.imencode('.jpg', frame)

    # Encode the JPEG image in Base64
    b64 = base64.b64encode(jpeg.tobytes())

    # Render the template with the Base64-encoded image
    return template('''
    <html>
        <head>
            <style>
                html, body {
                    height: 100%;
                }
                body {
                    background-color: #333;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                img {
                    max-height: 100%;
                    max-width: 100%;
                }
            </style>
        </head>
        <body>
            <meta http-equiv="refresh" content="5">
            <img src="data:image/jpeg;base64,{{data}}"/>
        </body>
    </html>
    ''', data=b64.decode())

run(host='localhost', port=8080)
