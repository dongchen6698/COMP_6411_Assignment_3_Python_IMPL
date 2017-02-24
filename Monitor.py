from threading import RLock
from threading import Condition


class FileControl:
    def __init__(self):
        self.__lock = RLock()
        self.__readers = Condition(self.__lock)
        self.__writers = Condition(self.__lock)
        self.__isReading_Count = 0
        self.__waitingWriters_Count = 0
        self.__isWriting = False

    def ReaderEntry(self, ReaderID):
        self.__lock.acquire()

        if self.__isWriting or self.__waitingWriters_Count > 0:
            print("Reader thread %s : waiting to read" % ReaderID)
            self.__readers.wait()
        print("Reader thread %s : ready to read" % ReaderID)
        self.__isReading_Count += 1

        self.__lock.release()

    def ReaderExit(self, ReaderID):
        self.__lock.acquire()

        print("Reader thread %s: finished reading" % ReaderID)
        self.__isReading_Count -= 1
        if self.__isReading_Count == 0:
            if self.__waitingWriters_Count > 0:
                self.__writers.notify()
            else:
                pass
                self.__readers.notify()

        self.__lock.release()

    def WriterEntry(self, WriterID):
        self.__lock.acquire()

        if self.__isWriting or self.__isReading_Count > 0:
            print("Writer thread %s : waiting to write" % WriterID)
            self.__waitingWriters_Count += 1
            self.__writers.wait()
            self.__waitingWriters_Count -= 1
        print("Writer thread %s : ready to write" % WriterID)
        self.__isWriting = True

        self.__lock.release()

    def WriterExit(self, WriterID):
        self.__lock.acquire()

        print("Writer thread %s : finished writing" % WriterID)
        if self.__waitingWriters_Count > 0:
            self.__writers.notify()
        else:
            self.__isWriting = False
            self.__readers.notify()

        self.__lock.release()

# Simply way to implement singleton
monitor = FileControl()
