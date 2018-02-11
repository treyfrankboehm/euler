#!/usr/bin/env python3

import glob
#import os
import subprocess as sp
import sys
import time

def extension(filename):
    return filename.split('.')[1]

def testHaskell(filename):
    compileCmd = "ghc -o %s.bin -i hs/Euler.hs %s --make -j2" % \
            (filename, filename)
    runCmd = "./%s.bin" % (filename)
    return run(compileCmd, runCmd)

def testPython(filename):
    compileCmd = "sleep 0"
    runCmd = "pypy %s" % (filename)
    return run(compileCmd, runCmd)

def testC(filename):
    compileCmd = "gcc -lm -o %s.out %s" % (filename, filename)
    runCmd = "./%s.out" % filename
    return run(compileCmd, runCmd)

def run(compileCmd, runCmd):
    sp.run(compileCmd.split(' '))
    start = float(time.perf_counter())
    child = sp.Popen(runCmd.split(' '), stdout=sp.PIPE)
    result = int(child.communicate()[0])
    run_time = float(time.perf_counter()-start)
    return [result, run_time]

def getResults(filename):
    lang = extension(filename)
    if lang == "hs":
        [result, run_time] = testHaskell(filename)
    elif lang == "py":
        [result, run_time] = testPython(filename)
    elif lang == "c":
        [result, run_time] = testC(filename)
    else:
        print("Unable to test file.")
        exit(1)

    return ("%s in %.3f seconds (result: %d)" % \
            (filename, run_time, result))

def testAll(lang):
    outfilename = "results-%s.txt" % lang
    outfile = open(outfilename, 'w')
    start_time = float(time.perf_counter())
    test_count = 0;
    for filename in sorted(glob.glob("%s/[0-9][0-9][0-9].%s" % \
                          (lang, lang))):
        results = getResults(filename)
        print(results)
        outfile.write(results + '\n')
        test_count += 1
    total_time = float(time.perf_counter()) - start_time
    totals = "Compiled and ran %d solutions is %.3f seconds\n" % \
            (test_count, total_time)
    print(totals)
    outfile.write(totals)
    outfile.close()
    exit(0)

if __name__ == "__main__":
    progNum = sys.argv[1]
    # If passed a language file type, test all solutions in that language
    if progNum == "hs":
        testAll("hs")
    elif progNum == "py":
        testAll("py")
    elif progNum == "c":
        testAll("c")
    else:
        # Otherwise, test the specific program passed
        print(getResults(progNum))

