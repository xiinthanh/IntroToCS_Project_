import cv2
import matplotlib.pyplot as plt
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
        
        # Matplotlib figure setup
        fig, ax = plt.subplots()
        image = ax.imshow(cv2.cvtColor(capture.read()[1], cv2.COLOR_BGR2RGB))  # Display the first frame
        
        while True:
            # Read a frame from the webcam
            ret, frame = capture.read()
            
            # Update the image in the figure
            image.set_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            plt.pause(0.01)  # Pause for a short duration to allow the figure to update
            plt.draw()
            
            # Perform classification on the frame
            results = model(frame)
            names_dict = results[0].names
            probs = results[0].probs.data
            predicted_name = names_dict[probs.argmax().item()]
            
            # Print the predicted name
            print(predicted_name)
            
            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam, close the window, and release the figure
        capture.release()
        cv2.destroyAllWindows()
        plt.close(fig)

# Create an instance of the Task2 class
task2 = Task2()

# Run Task2
task2.Task2_Run()