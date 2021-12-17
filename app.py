from filelock import FileLock
import time,os,random



while True:
    for x in range(0,9999): 
        f = open("/tmp/myfile.txt","+a")
        string = str(random.randrange(9999,99999999))
        print(string)
        f.write(string)
        f.close
    with FileLock("/tmp/myfile.txt"):
        # work with the file as it is now locked
        print("Lock acquired.")
        os.remove("/tmp/myfile.txt")
        time.sleep(.1)

