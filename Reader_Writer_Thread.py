import threading
import os
import random
from Monitor import monitor


class Reader_Writer_Thread(threading.Thread):

    def __init__(self, n_threadID):
        threading.Thread.__init__(self)
        self.threadID = n_threadID

    def run(self):
        for i in range(4):
            random_number = random.randint(0, 7)
            if random_number % 2 is 0:
                monitor.WriterEntry(self.threadID)
                self.WriteFile()
                monitor.WriterExit(self.threadID)
            else:
                monitor.ReaderEntry(self.threadID)
                self.ReadFile()
                monitor.ReaderExit(self.threadID)

    def ReadFile(self):
        filepath = '_SharedFile.txt'
        if os.path.getsize(filepath) is not 0:
            with open(filepath, 'r') as f:
                print([line for line in f][-1])
        else:
            print("File is Empty")

    def WriteFile(self):
        with open('_SharedFile.txt', 'a') as f:
            f.write("Thread : %s is writing\n" % self.threadID)




