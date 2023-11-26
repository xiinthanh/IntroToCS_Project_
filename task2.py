import cv2
from ultralytics import YOLO
from camera import *
import time

class FaceRecognizer:
    file_path = '.\\AI\\FaceRecognition.pt'

    def __init__(self, _ID, _task_Ready, _task_Data, _camera):
        print("Init task 2")
        
        # Load the custom model
        self.model = YOLO(self.file_path)
        self.camera = _camera

        self.ID = _ID
        self.task_Ready = _task_Ready
        self.task_Data = _task_Data

    def Run(self):
        '''return a string student id if recognizable, "Unkown" otherwise'''
        print("#"*30)
        print("Face detecting...")
        
        result = "Unknown"

        for i in range(10):  # Try detect for 10 times
            time.sleep(0.2)
            print(f"Attempt {i+1}th")
            # Get and save to "self.camera.save_path" (".\images\from_cam.png")
            self.camera.Run()

            # Open image
            image = cv2.imread(self.camera.save_path)
            
            # Perform classification on the frame
            results = self.model(image)
            names_dict = results[0].names
            probs = results[0].probs.data
            predicted_id = names_dict[probs.argmax().item()]

            # Calculate confidence as a percentage
            confidence = probs.max().item() * 100

            # Print the predicted name and confidence
            print(predicted_id, "  confidence: {:.2f}%".format(confidence))

            # Confirm if confidence score over 70% 
            if (confidence > 70):
                result = predicted_id
                break
        
        return result
    

    def RunTask(self):
        if (not self.task_Ready[self.ID]):  # There is no data
            return "[i]"

        result = self.Run()

        # Creating the cycle: task1 -> task2 -> task3 -> task4
        if (result != "Unknown"):
            self.task_Ready[self.ID + 1] = True
            self.task_Data[self.ID + 1] = result
        else:
            # Restart the cycle: return to the first task
            self.task_Ready[0] = True

        self.task_Ready[self.ID] = False

        return ("[1]" + result)
    
# Create an instance of the Task2 class
if __name__ == "__main__":

    task_Ready = [False, True, False, False]
    task_Data = ["", "", "", ""]

    camera = Camera()

    task2 = FaceRecognizer(1, task_Ready, task_Data, camera)
    while True:
        print(task2.Run())
        time.sleep(3)
