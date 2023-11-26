import cv2

class Camera:
    save_path = ".\\images\\from_cam.png"
    def __init__(self, ID = 0):
        # Set camera
        self.camera = cv2.VideoCapture(ID)

    def Run(self):
        # Take image
        ret, image = self.camera.read()
        # Resize image for detecting
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        # Save image        
        cv2.imwrite(self.save_path, image)
