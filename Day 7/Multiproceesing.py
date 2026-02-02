import multiprocessing
import os

def task():
    print(f"Process ID: {os.getpid()}")

def main():
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()

