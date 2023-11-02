# fortmat: "[<TaskID>]<data>"
# store as a list so that it can be changed anywhere in project (pass by reference)
latest_output = [""]

class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1


class Scheduler:
    TICK = 100
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0
    
    # TODO
    def __int__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
            return aTask.TaskID
        else:
            print("PrivateTasks are full!!!")
            return -1

    def SCH_Update(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                self.SCH_tasks_G[i].Delay -= 1
            else:
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1

    def SCH_Dispatch_Tasks(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                self.SCH_tasks_G[i].RunMe -= 1
                # Run task
                global latest_output
                output = self.SCH_tasks_G[i].pTask()
                if (output and output[:3] != '[i]'):  # [i]: ignore
                    latest_output[0] = output

    # TODO
    def SCH_Delete(self, aTask):
        return
    # TODO
    def SCH_GenerateID(self):
        return -1

if __name__ == "__main__":
    lst = ['a', 'b', 'c', 'd']
    print(lst)
    lst.remove('b')
    print(lst)
