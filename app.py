from filelock import FileLock
import time

while True:
    with FileLock("myfile.txt"):
        # work with the file as it is now locked
        print("Lock acquired.")
        time.sleep(10)

