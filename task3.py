import winsound
import openpyxl

class StudentIDChecker:
    def __init__(self, _ID, _task_Ready, _task_Data):
        print("Init task 3")

        # Load the buslist.xlsx file
        self.source_excel_file = ".\\excel\\buslist.xlsx"

        workbook = openpyxl.load_workbook(self.source_excel_file)  #Open file
        self.sheet = workbook['Sheet1']  #Access sheet

        self.ID = _ID
        self.task_Ready = _task_Ready
        self.task_Data = _task_Data

    def Run(self):
        '''Check if student_id has registered for bus service.
        Return the name of the student if YES, an empty string if NO.''' 
        
        if (not self.task_Ready[self.ID]):
            return "[i]"

        student_id = self.task_Data[self.ID]

        print("#"*30)
        print(f"Checking if {student_id} has registered...")

        student_name = ""
        student_found = False
        for row in self.sheet.iter_rows(min_row=2, values_only=True):  #Start form the second row, because the first one is title
            id_in_list = str(row[0])
            if id_in_list == student_id:
                student_name = row[1]
                student_found = True  # Found
                break

        if student_found:
            print(f"{student_id}_{student_name} is in the bus list")
            
            #Print 'Beep' to notificate that the process ended and that student is in the bus list
            self.hz = 500   #Hz
            self.time = 600 #ms
            winsound.Beep(self.hz, self.time)
        else:
            print(f"{student_id} is not in the bus list\n")


        # Creating the cycle: task1 -> task2 -> task3 -> task4
        if (student_name != ""):
            self.task_Ready[self.ID + 1] = True
            self.task_Data[self.ID + 1] = student_id + "|" + student_name
        else:
            # Restart the cycle: return to the first task
            self.task_Ready[0] = True

        self.task_Ready[self.ID] = False

        return "[2]" + student_name
        

if __name__ == "__main__":
    checker = StudentIDChecker()
    print(checker.Run("10422075"))
    
    print(checker.Run("10422076"))
