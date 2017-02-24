from Reader_Writer_Thread import Reader_Writer_Thread
import os


def main():
    if not os.path.exists('_SharedFile.txt'):
        open('_SharedFile.txt', 'a').close()
    else:
        os.remove('_SharedFile.txt')
        open('_SharedFile.txt', 'a').close()

    reader_writer = {}
    for i in range(7):
        reader_writer[i] = Reader_Writer_Thread(str(i))

    for i in range(7):
        reader_writer[i].start()


if __name__ == '__main__':
    main()




