#!/usr/bin/env python

import daemon

from spam import do_main_program

with daemon.DaemonContext():
    do_main_program()

def compare(str1, str2):
    import collections
    if len(str1) != len(str2):
        return False
    d = collections.defaultdict(int)
    for c in str1:
        d[c] += 1
    for c in str2:
        d[c] -= 1
    return all(v == 0 for v in d.itervalues())

def downloads_scan():
    import os
    l = []
    fileExt = []
    i = 0
    os.system("cd /Users/Nicholas/Downloads")
    for file in os.listdir("/Users/Nicholas/Downloads"):
        fileExt = os.path.splitext(file)
        str1 = str(fileExt[-1])
        str2 = ".enw"
        if compare(str1, str2):
            l.append(fileExt[-2] + fileExt[-1])
        str2 = ".ris"
        if compare(str1, str2):
            l.append(fileExt[-2] + fileExt[-1])
        str2 = ".ovd"
        if compare(str1, str2):
            l.append(fileExt[-2] + fileExt[-1])
        str2 = ".cgi"
        if compare(str1, str2):
            l.append(fileExt[-2] + fileExt[-1])
        if file is science
            l.append(fileExt[-2])

    print l
    for filename in l:
        pathname = "/Users/Nicholas/Downloads/" + filename
        print(pathname)
        #os.environ["pathname"] = pathname#this passes the name of the varible, not the variable!
        os.system("open -a EndNote\ X7 %s" % (pathname,))

downloads_scan()

