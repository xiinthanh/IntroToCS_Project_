import cv2
import numpy as np
from keras.models import load_model

class StudentCardDetector:
    def __init__(self, model_path, labels_path):
        self.model = load_model(model_path, compile=False)
        self.class_names = open(labels_path, "r").readlines()
        self.camera = cv2.VideoCapture(0)

    def detect(self):
        while True:
            ret, image = self.camera.read()
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            cv2.imshow("Webcam Image", image)
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1
            prediction = self.model.predict(image)
            index = np.argmax(prediction)
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
            keyboard_input = cv2.waitKey(1)
            if keyboard_input == 27:
                break
        self.camera.release()
        cv2.destroyAllWindows()
      

detector = StudentCardDetector("keras_Model.h5", "labels.txt")
if detector.detect():
    print("True")
else:
    print("False")
