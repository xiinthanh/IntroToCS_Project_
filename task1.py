import cv2
import numpy as np
from keras.models import load_model
from camera import *


class StudentCardDetector:
    model_path = ".\\AI\\keras_Model.h5"
    labels_path = ".\\AI\\labels.txt"

    def __init__(self, _ID, _task_Ready, _task_Data, _camera):
        print("Init task 1")
        # Load model & labels
        self.model = load_model(self.model_path, compile=False)
        self.class_names = open(self.labels_path, "r").readlines()

        # camera object
        self.camera = _camera

        self.ID = _ID
        self.task_Ready = _task_Ready
        self.task_Data = _task_Data

    def Run(self):
        print("#"*30)
        print("Student Card detecting...")

        # Get and save to "self.camera.save_path" (".\images\from_cam.png")
        self.camera.Run()

        is_student_card = "False"

        # Open image
        image = cv2.imread(self.camera.save_path)
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

        # Qualified-Condition
        # If dectect student card with over 70% confidence, confirm
        if (index == 0 and confidence_score > 0.70):
            is_student_card = "True"

        return is_student_card
    

    def RunTask(self):
        # There is no data to run
        if (not self.task_Ready[self.ID]):
            return "[i]"

        is_student_card = self.Run()
        
        # Creating the cycle: task1 -> task2 -> task3 -> task4
        # First task in the chain
        if (is_student_card == "True"):
            self.task_Ready[self.ID + 1] = True
            self.task_Data[self.ID + 1] = is_student_card
            
            self.task_Ready[self.ID] = False

        return ("[0]" + is_student_card)


# Test
if __name__ == "__main__":
    import time

    camera = Camera()
    task_Ready = [True, True, True, True]
    task_Data = ["", "", "", ""]
    detector = StudentCardDetector(0, task_Ready, task_Data, camera)
    while True:
        print(detector.Run())
        time.sleep(3)

