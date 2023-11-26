import gspread
import time
from datetime import datetime

class BusRecorder:
    number_of_student_on_bus = 0
    def __init__(self, _ID, _task_Ready, _task_Data):
        print("Init task 4")

        self.number_of_seats = 3
        gc = gspread.service_account(filename="./gspread/service_account.json")

        current_date = datetime.now().strftime("%Y-%m-%d") #the day 
        
        try:  # Try to open today's sheet
            sheet = gc.open(current_date)
            self.work_sheet = sheet.sheet1
        except:  # Today's sheet does not exist
            # Create a new one
            sheet = gc.create(current_date)
            # Share to your account to view
            sheet.share('10422075@student.vgu.edu.vn', perm_type='user', role='writer')
            self.work_sheet = sheet.sheet1

            # Add titles to columns
            content = ["Student ID", "Full Name", "Time"]
            (self.work_sheet).append_row(content, table_range="A1:C1")


        self.ID = _ID
        self.task_Ready = _task_Ready
        self.task_Data = _task_Data

    def Run(self, student_name, student_id):
        '''Return "Full" if the bus is full, "Available" if the bus still has empty seat(s).'''

        print("#"*30)
        print(f"Adding {student_name} to the bus log file...")
        
        if (self.number_of_student_on_bus < self.number_of_seats):
            current_time = time.strftime("%H:%M:%S %d-%m-%Y")

            content = [student_id, student_name, current_time]
            (self.work_sheet).append_row(content, table_range="A1:C1")

            self.number_of_student_on_bus +=1

        else:
            print("Already full\n")

        bus_state = str(self.number_of_student_on_bus) + '/' + str(self.number_of_seats)

        return bus_state
    

    def RunTask(self):        
        if (not self.task_Ready[self.ID]):
            return "[i]"

        student_id, student_name = self.task_Data[self.ID].split('|')
        bus_state = self.Run(student_id, student_name)

        # Last task in the chain
        self.task_Ready[self.ID] = False
        # Restart the cycle: return to the first task
        self.task_Ready[0] = True

        return "[3]" + bus_state


if __name__ == "__main__":
    bus = BusRecorder()
    print(bus.Run("10422117", "ABC"))

    print(bus.Run("10422075", "DEF"))

    print(bus.Run("10421101", "GHK"))

    print(bus.Run("10422052", "WWW"))

    print(bus.Run("10422118", "ZZZ"))
