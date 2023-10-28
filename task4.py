import os
import winsound
import openpyxl
import time
from datetime import datetime

class Task3:
    def __init__(self):
        self.folder_path = ".\\" #The path to the folder that contains file "Danh sach sinh vien di xe bus"
        # Nên để cái file code với cái file excel chung 1 folder luôn.
        # thì nó sẽ đỡ phải set cái path này!

        # Comment nào dài dài thì để nó như này cho dễ nhìn nè.
        #Acess file Danh sanh sinh vien di xe bus
        self.source_excel_file = os.path.join(self.folder_path,"Danh_sach_sinh_vien_di_xe_bus.xlsx")
        

        # Mấy cái mở file này thuộc phần set up (init)
        self.source_workbook = openpyxl.load_workbook(self.source_excel_file) #Open file
        self.source_sheet = self.source_workbook['Sheet1']#Access sheet


    def check_bus_list(self, student_id):
        # Cái student_found không cần là 1 phần của object đâu, nó là biến để đánh dấu kết quả thôi thì cho nó là
        # biến bình thường là được rồi
        student_found = False
        
        for row in self.source_sheet.iter_rows(min_row=2, values_only=True):  #Start form the second row, because the first one is title
            if row[0] == student_id:
                self.name = row[1]
                student_found = True
                # Khỏi đóng, để lần sau xài tiếp
                # self.source_workbook.close()
                break

        if student_found:
            print(f"{student_id}_{self.name} is in the bus list")
            
            #Print 'Beep' to notificate that the process ended and that student is in the bus list
            self.hz = 500   #Hz
            self.time = 600 #ms
            winsound.Beep(self.hz, self.time)
            return True
        else:
            print(f"{student_id} is not in the bus list\n")
            return False


class Bus:
    number_of_student_on_bus = 0
    def __init__(self):
        self.number_of_seats = 3

        # Cái này chắc do ông sợ mỗi lần chạy là 1 ngày khác nhau.
        # Nhưng mà mình cho là xài trong ngày xong mình sẽ tắt máy,
        # ngày hôm sau mới mở lên lại. Cho nên mỗi lần Task4_Run là trong cùng 1 ngày.
        # Mình chỉ cần tạo lúc mở máy thôi (init).


        self.folder_path = ".\\" #the path to the folder that contains this program
        current_date = datetime.now().strftime("%Y-%m-%d") #the day 
        self.excel_file_path = os.path.join(self.folder_path, f"{current_date}.xlsx") #the path to the file excel of current day
        
        #if the file excel of current day is not exists, it will create ones_ this can ensure that one day only has one 1 file Excel
        if not os.path.exists(self.excel_file_path):
            self.workbook = openpyxl.Workbook()
            self.sheet = self.workbook.active
            self.sheet.title = "Danh_sach_len_xe_bus"
            self.row_to_insert = ["Student ID", "Full name", "Time"]
            self.workbook['Danh_sach_len_xe_bus'].append(self.row_to_insert)
            self.workbook.save(self.excel_file_path)
            # self.workbook.close() 


    def Run(self, student_id, student_name):        

        #update information to file Excel
        
        if (Bus.number_of_student_on_bus < self.number_of_seats):
            self.workbook = openpyxl.load_workbook(self.excel_file_path)
            self.current_sheet = self.workbook['Danh_sach_len_xe_bus']
            
            # Đừng có cái gì cũng khai báo self..., như này là 1 biến của object.
            # Với mấy biến chỉ để đánh dấu xài 1 lần như này thì khai báo bình thường thôi.
            # self.update = False
            update = False

            for row in self.current_sheet.iter_rows(min_row=2, values_only=True):  #Start form the second row, because the first one is title
                if row[0] == student_id:
                    update = True
                    break

            if not update:
                current_time = time.strftime("%H:%M:%S %d-%m-%Y")
                
                # Cái này rắc rối lắm, mình có cách khác đơn giản hơn
                # self.row_to_insert = [student_id, self.task3.name, self.time] #self.name from Task 3
                # Mình bỏ student_name vào hàm Run luôn
                
                row_to_insert = [student_id, student_name, current_time] #self.name from Task 3
                
                self.current_sheet.append(row_to_insert)
                self.workbook.save(self.excel_file_path)
                # self.workbook.close()
                Bus.number_of_student_on_bus +=1
            print(f"==> {self.number_of_seats - Bus.number_of_student_on_bus} seat(s) left \n \n ")
            if Bus.number_of_student_on_bus == self.number_of_seats:
                message = "Fulled passengers, let's gooooooooo!"
                print("=" * len(message))
                print(f"{message}\n")
                print("=" * len(message))

        else:
            print("Not accepted\n")
            

            

#Try:===========================================================================
student = Task3()
student_id = int("10422117") #the number will be replaced by the result of Task2
bus = Bus()

if student.check_bus_list(student_id):
    bus.Run(student_id, "ABC")

student_id2 = int("10422075") 
if student.check_bus_list(student_id2):
    bus.Run(student_id2, "DEF")

student_id5 =int ("10421101")
if student.check_bus_list(student_id5):
    bus.Run(student_id5, "GHK")

student_id3 = int("10422052")
if student.check_bus_list(student_id3):
    bus.Run(student_id3, "WWW")
    
student_id4 =int ("10422118")
if student.check_bus_list(student_id4):
    bus.Run(student_id4, "ZZZ")    

