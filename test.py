#!/usr/bin/env python3

import glob
import os
import subprocess as sp
import sys
import time

# Zero-pad the beginning to match my filename formatting
def zeroPad(num):
    num = str(num)
    if len(num) == 1:
        num = "00%s" % num
    elif len(num) == 2:
        num = "0%s" % num
    return num

def run(compileCmd, runCmd):
    sp.run(compileCmd.split(' '))
    start = float(time.perf_counter())
    child = sp.Popen(runCmd, stdout=sp.PIPE)
    result = int(child.communicate()[0])
    run_time = float(time.perf_counter()-start)
    return [result, run_time]

def testHaskell(num):
    compileCmd = "ghc -o %s.hs.bin %s.hs" % (num, num)
    runCmd = "./%s.hs.bin" % (num)
    return run(compileCmd, runCmd)

def testPython(num):
    return [0, 0]

def testC(num):
    return [0, 0]

def getResults(num, lang):
    if lang.lower() in ("hs", "haskell"):
        [result, run_time] = testHaskell(num)
    elif lang.lower() in ("py", "python"):
        [result, run_time] = testPython(num)
    elif lang.lower() in ("c"):
        [result, run_time] = testC(num)

    return ("%s.hs in %.3f seconds (result: %d)" % \
            (num, run_time, result))

def progLang(filename):
    num = filename[0:3]
    lang = filename[4:]
    return [num, lang]

def testAll():
    outfile = open("results.txt", 'w')
    start_time = float(time.perf_counter())
    test_count = 0;
    for filename in sorted(glob.glob("[0-9][0-9][0-9].hs")):
        [num, lang] = progLang(filename)
        results = getResults(num, lang)
        print(results)
        outfile.write(results + '\n')
        test_count += 1
    total_time = float(time.perf_counter()) - start_time
    totals = "Ran and compiled %d solutions is %.3f seconds\n" % \
            (test_count, total_time)
    print(totals)
    outfile.write(totals)
    outfile.close()
    exit(0)

if __name__ == "__main__":
    # Must be given a number to test
    if len(sys.argv) == 1:
        exit(1)

    progNum = zeroPad(sys.argv[1])
    if progNum == "all":
        testAll()
    else:
        print(getResults(progNum, "hs"))

