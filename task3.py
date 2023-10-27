class Task3: 
  def __init__(self, student_list_file):
    self.Student_ = self.load_student_list(student_list_file)
    self.attendance_count = [0] * len(self.Student_)

  def load_student_list(self, file_path):
    with open(file_path, 'r') as file:
      student_list = [line.strip() for line in file]
      return student_list
  
  def Task3_Run(self, student_ID):
    print("Task 3 is activated!!!")
    if student_ID in self.Student_:
      index = self.Student_.index(student_ID)
      self.attendance_count[index] += 1
      print(f"Student {student_ID} is in the bus list.")
      print(f"Attendance if {student_ID} is increased to {self.attendance_count[index]}.")
      return True
    else:
      print(f"Student {student_ID} is not in the bus list.")
      return False

task3 = Task3("studentIist.txt")
student_ID = "10421102"
print(task3.Task3_Run(student_ID))
