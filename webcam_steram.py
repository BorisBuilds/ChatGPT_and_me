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

# Pfad zur Webcam (in diesem Beispiel wird die erste Webcam verwendet)
cap = cv2.VideoCapture(0)

@route('/')
def index():
    # Erfasse ein Bild von der Webcam
    ret, frame = cap.read()

    # Konvertiere das Bild in das JPEG-Format
    ret, jpeg = cv2.imencode('.jpg', frame)

    # Kodiere das JPEG-Bild in Base64
    b64 = base64.b64encode(jpeg.tobytes())

    # Rendere das Template mit dem Base64-kodierten Bild
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
