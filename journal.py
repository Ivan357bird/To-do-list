


class Diary(object):
    def __init__(self, path):
        self.path = path
        f = open(path,"r",encoding="utf-8")
        self.tasks = f.read().split("|")
        f.close()
    def get_tasks(self):
        return self.tasks
    def add_task(self,task):
        self.tasks.append(task)
        self.update_file()
    def update_file(self):
        f = open(self.path,"w",encoding="utf-8")
        f.write('|'.join(self.tasks))
        f.close()
    def delete_task_by_index(self,index):
        self.tasks.pop(index)
        self.update_file()
    def delete_task_by_name(self,name):
        self.tasks.remove(name)
        self.update_file()


Diary1 = Diary("file.txt")
print(Diary1.get_tasks())
# string = input("Enter task: ")
# Diary1.add_task(string)
# string1 = int(input("Enter index: "))
string2 = str(input("Enter name: "))
# Diary1.delete_task_by_index(string1)
Diary1.delete_task_by_name(string2)







