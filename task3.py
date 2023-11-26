import winsound
import gspread


class StudentIDChecker:
    def __init__(self, _ID, _task_Ready, _task_Data):
        print("Init task 3")

        # Open spreadsheet "BusList"
        gc = gspread.service_account(filename="./gspread/service_account.json")
        sheet = gc.open("BusList")
        work_sheet = sheet.worksheet("Bus List")

        self.records = work_sheet.get_all_records()
        # print(self.records[0]['Student ID'])


        self.ID = _ID
        self.task_Ready = _task_Ready
        self.task_Data = _task_Data

    def Run(self, student_id):
        '''Check if student_id has registered for bus service.
        Return the name of the student if YES, an empty string if NO.''' 
        
        print("#"*30)
        print(f"Checking if {student_id} has registered...")

        student_name = ""

        for row in self.records:  #Start form the second row, because the first one is title
            registered_id = str(row['Student ID'])
            if registered_id == student_id:
                student_name = row['Full Name']
                break

        if student_name:  # is not "": found in bus list
            print(f"{student_id}_{student_name} is in the bus list")
            
            #Print 'Beep' to notificate that the process ended and that student is in the bus list
            self.hz = 500   #Hz
            self.time = 600 #ms
            winsound.Beep(self.hz, self.time)
        else:
            print(f"{student_id} is not in the bus list\n")

        return student_name
    
    def RunTask(self):
        if (not self.task_Ready[self.ID]):
            return "[i]"

        student_id = self.task_Data[self.ID]
        student_name = self.Run(student_id)

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
