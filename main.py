import time
from scheduler import *
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task_Ready = [False, False, False, False]
task_Data = ["", "", "", ""]

camera = Camera()

task1 = StudentCardDetector(0, task_Ready, task_Data, camera)
task2 = FaceRecognizer(1, task_Ready, task_Data, camera)
task3 = StudentIDChecker(2, task_Ready, task_Data)
task4 = BusRecorder(3, task_Ready, task_Data)
task5 = AdafruitServer(latest_output)

scheduler.SCH_Add_Task(task5.Run, 1000,500)
scheduler.SCH_Add_Task(task1.RunTask, 1000,5000)
scheduler.SCH_Add_Task(task2.RunTask, 2000,1000)
scheduler.SCH_Add_Task(task3.RunTask, 3000,1000)
scheduler.SCH_Add_Task(task4.RunTask, 4000,1000)

# Run the first task
task_Ready[0] = True

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
