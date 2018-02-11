#!/usr/bin/env python3

import os
import textwrap
from html.parser import HTMLParser

start = 1
stop  = 10
parsed = []

def downloadAndParse(low, high):
    for n in range(low, high+1):
        filename = "problems/problem%d.html" % n
        urlCmd = "curl https://projecteuler.net/problem=%d -s -o %s" \
                % (n, filename)
        os.system(urlCmd)
        parseProblemHTML(filename)
        os.system("rm %s" % filename)

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if not data.strip(' \n'):
            pass
        elif "<h2" in str(self.get_starttag_text()):
            parsed.append(data)
        elif "<div" in str(self.get_starttag_text()):
            parsed.append(data)
        elif "<p" in str(self.get_starttag_text()):
            parsed.append(data)
        elif "<h3" in str(self.get_starttag_text()):
            parsed.append(data)
        elif "<span" in str(self.get_starttag_text()):
            parsed.append(data)
        elif "<br" in str(self.get_starttag_text()):
            parsed.append(data)

def parseProblemHTML(filename):
    global parsed
    htmlfile = open(filename, 'r')
    parser = MyHTMLParser()
    parser.feed(''.join(htmlfile))
    parser.close()

    proper = []
    for field in parsed:
        if not field in [".net", "Project Euler", "\nProject Euler: "]:
            proper.append(field)

    number = ''
    title = ''
    publish = ''
    difficulty = ''
    description = ''
    for i in range(len(proper)):
        if i == 0:
            title = proper[i]
        elif i == 1:
            number = proper[i]
        elif i == 2:
            publish = proper[i]
            publish = publish.replace('; ', ' -- ')
            publish = publish.replace(';', '')
        elif i == 3:
            difficulty = proper[i]
        else:
            description = description + proper[i] + '\n'

    description = textwrap.fill(description, 72)
    formatted = "%s: %s (%s)\n%s\n\n%s\n" % (number, title, difficulty, publish, description)

    probnum = int(number[8:])
    if probnum < 10:
        probnum = "00%d" % probnum
    elif probnum < 100:
        probnum = "0%d" % probnum

    print("%s\n%s" % ('-'*72, formatted))
    outfile = open("problems/problem%s.txt" % probnum, 'w')
    outfile.write(formatted)
    outfile.close()
    htmlfile.close()

    parsed = []

if __name__ == "__main__":
    downloadAndParse(start, stop)

