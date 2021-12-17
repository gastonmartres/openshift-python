from filelock import FileLock

with FileLock("myfile.txt"):
    # work with the file as it is now locked
    print("Lock acquired.")
