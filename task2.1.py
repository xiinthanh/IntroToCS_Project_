import cv2
import os
from ultralytics import YOLO

class Task2:
    def __init__(self):
        print("Init task 2")
    
    def Task2_Run(self):
        print("Task 2 is activated!!!!")
        
        # Load the custom model
        model = YOLO('FaceRecognition.pt')
        
        # Open the webcam
        capture = cv2.VideoCapture(0)
        
        while True:
            # Read a frame from the webcam
            ret, frame = capture.read()
            
            # Perform classification on the frame
            results = model(frame)
            names_dict = results[0].names
            probs = results[0].probs.data
            predicted_name = names_dict[probs.argmax().item()]
            
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Print the desired output
            print("Init task 2")
            print("Task 2 is activated!!!!")
            print(predicted_name)
            
            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam
        capture.release()

# Create an instance of the Task2 class
task2 = Task2()

# Run Task2
task2.Task2_Run()