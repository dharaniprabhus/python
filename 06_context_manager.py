import sys
import os

class StdoutRedirectFile:
    def __init__(self,name):
        self.file = open(name, "w")

    def __enter__(self):
        self.out = sys.stdout
        sys.stdout = self.file
        return self

    def __exit__(self, ex_type, ex_val, traceback):
        self.file.close()
        sys.stdout = self.out

with StdoutRedirectFile("out.txt") as ctx:
    print("Writing to file\n")
    print("Another line")

print("back to console")


from contextlib import contextmanager

@contextmanager
def stdout_redirect_file(name):
    out = sys.stdout
    file = open(name, "w")
    try:
        sys.stdout = file
        yield
    finally:
        print("finally called")
        sys.stdout = out
        file.close()

with stdout_redirect_file("out2.txt") as ctx:
    print("Writing to file\n")

print("back to console again")


def copy_src_dest(src,dst):
    with open(src,"r") as r, open(dst,"w") as w:
        while True:
            line = r.readline()
            if not line:
                break
            if not line.startswith("#"):
                w.write(line)

copy_src_dest("src.txt", "dst.txt")

@contextmanager
def push_do_pop_dir(path):
    curpath = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(curpath)

with push_do_pop_dir("/"):
    print(os.getcwd())
print(os.getcwd())
