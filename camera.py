import cv2
import numpy as np

class Camera:
    def __init__(self, ID = 0):
        # Set camera
        self.camera = cv2.VideoCapture(ID)
        pass
    def Run(self):
        # Take image
        ret, image = self.camera.read()
        # Resize image for detecting
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        # Save image
        cv2.imwrite(".\\images\\from_cam.png", image)