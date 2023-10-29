import cv2
import numpy as np
from keras.models import load_model

model_path = "keras_Model.h5"
labels_path = "labels.txt"

class StudentCardDetector:
    def __init__(self):
        print("#"*30)
        print("Init student card detector")
        # Load model & labels
        self.model = load_model(model_path, compile=False)
        self.class_names = open(labels_path, "r").readlines()

        # Set camera
        self.camera = cv2.VideoCapture(0)

    def detect(self):
        print("Student Card detecting...")
        is_student_card = False
        # Try scanning for 5 times
        for i in range(5):
            print(f" * Attemp {i+1}th:")

            # Take image
            ret, image = self.camera.read()
            # Resize image
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            # Save image
            cv2.imwrite("task1_image.png", image)
            # Modify the image for detection
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1
            
            # Predict
            prediction = self.model.predict(image)
            index = np.argmax(prediction)
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            # If dectect student card with over 70% confidence, confirm
            if (index == 0 and confidence_score > 0.70):
                is_student_card = True
                break
        
        return is_student_card


if __name__ == "__main__":
    detector = StudentCardDetector()
    print(detector.detect())

