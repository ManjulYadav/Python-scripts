#!/usr/bin/env python

import numpy as np
import os
import re
from re import search
from random import randint
import sys

def aver(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    lines = [l.strip() for l in lines if not search ('[~!@#$%^&*]', l)]
    lines = np.array([l.split() for l in lines], dtype='float64')
    print "The input file has %d rows and %d columns" % (len(lines), len(lines[0]))
    selrowcol = raw_input("Do you want to average across: 1. rows\t or \t2. columns?\n")
    if selrowcol == str(1):
        savedat = raw_input("I'm going to average all entries in a given row for all the rows. Do you want the results: 1. printed\t or \t2. saved?\n")
        if savedat == str(1):
            for a in np.arange(len(lines)):
                print "Line no: %d\tAverage: %.3f\tStd.Err.: %.3f\tMin: %.3f\tMax: %.3f" % (a+1, np.average(lines[a]), np.std(lines[a])/np.sqrt(len(lines[a])), np.min(lines[a]), np.max(lines[a]))
        elif savedat == str(2):
            output = raw_input("Enter output file name (default ext is .dat): ")
            results = open(os.getcwd()+'/'+str(output)+'.dat', 'a')
            choice = raw_input("Do you want: 1. Average\t2.Average and Std. Error ?\n")
            if choice == str(1):
                for a in np.arange(len(lines)):
                    results.write("%.3f\n" % (np.average(lines[a])))
                results.close()
            elif choice == str(2):
                for a in np.arange(len(lines)):
                    results.write("%.3f\t%.3f\n" % (np.average(lines[a]), np.std(lines[a])/np.sqrt(len(lines[a]))))
                results.close()
            else:
                print "You have entered wrong choice. I'm quiting. Bye Bye ..........."
                raise
                sys.exit()
        else:
            print "You have entered wrong choice. I'm quitting. Bye Bye ..............."
            raise
            sys.exit()
    elif selrowcol == str(2):
        savedat = raw_input("Do you want an average for : 1. all columns\t2. specific ones?\n")
        if savedat == str(1):
            colout = raw_input("I'm going to calculate averages for all columns. Do you want the results: 1. printed\t2.saved?\n")
            if colout == str(1):
              print "Averages:\tStd. Error"
              for a in np.arange(len(lines[0])):
                  print "%.3f\t\t%.3f" % (np.average(lines[:,a]), np.std(lines[:,a])/np.sqrt(len(lines[:,a])))
            elif colout == str(2):
                output = raw_input("Enter output file name (default ext is .dat): ")
                results = open(os.getcwd()+'/'+str(output)+'.dat', 'a')
                choice = raw_input("Do you want: 1. Average\t2. Average and Std. Error ?\n")
                if choice == str(1):
                    for a in np.arange(len(lines[0])):
                        results.write("%.3f\n" % (np.average(lines[:,a])))
                    results.close()
                elif choice == str(2):
                    for a in np.arange(len(lines[0])):
                        results.write("%.3f\t%.3f\n" % (np.average(lines[:,a]), np.std(lines[:,a])/np.sqrt(len(lines[:,a]))))
                    results.close()
                else:
                    print "You have entered wrong choice. I'm quitting. Bye Bye ............"
                    raise
                    sys.exit()
        elif savedat == str(2):
            colnos = raw_input("Which are the columns that you want the averages for (Enter column no. separated by single space)?\n")
            colarray = np.zeros(len(colnos.split()), dtype='int32')
            for b in np.arange(len(colnos.split())):
                colarray[b] += int(colnos.split()[b])-1
            colout = raw_input("Calculating averages for columns entered. Do you want the results: 1. printed\t2.saved?\n")
            if colout == str(1):
                print "Averages:\tStd. Error"
                for a in colarray:
                    print "%.3f\t\t%.3f" % (np.average(lines[:,a]), np.std(lines[:,a])/np.sqrt(len(lines[:,a])))
            elif colout == str(2):
                output = raw_input("Enter output file name (default ext is .dat): ")
                results = open(os.getcwd()+'/'+str(output)+'.dat', 'a')
                choice = raw_input("Do you want: 1. Average\t2. Average and Std. Error ?\n")
                if choice == str(1):
                    for a in colarray:
                        results.write("%.3f\n" % (np.average(lines[:,a])))
                    results.close()
                elif choice == str(2):
                    for a in colarray:
                        results.write("%.3f\t%.3f\n" % (np.average(lines[:,a]), np.std(lines[:,a])/np.sqrt(len(lines[:,a]))))
                    results.close()
                else:
                    print "You have entered wrong choice. I'm quitting. Bye Bye ................"
                    raise
                    sys.exit()
            else:
                print "You have entered wrong choice. I'm quitting. Bye Bye ..................."
                raise
                sys.exit()
        else:
            print "You have entered wrong choice. I'm quitting. Bye Bye ...................."
            raise
            sys.exit()
    else:
        print "You have entered wrong choice. I'm quitting. Bye Bye ....................."                
            
if len(sys.argv) != 2:
    print 'M> Usage: python average.py filename.dat'
    sys.exit()

try:
    myfile = sys.argv[1]

except:
    print 'M> Failed due to several reasons'
    sys.exit()

try:
    aver(myfile)
    print "                                                                                                                                          "
    print "=========================================================================================================================================="
    quote = randint(0,3)
    if quote == 0:
        print "                                               No way                                                                                  "
    elif quote == 1:
        print "                                               To hell                                                                                 "
    elif quote == 2:
        print "                                               Go back                                                                                 "
    elif quote == 3:
        print "                                          Give me the answer                                                                           " 
    elif quote == 3:
        print "                                          Could you please keep it down. I'm trying to get some sleep here                            " 
    print "=========================================================================================================================================="
    print "                                                                                                                                          "
except:
    print 'M> Something went wrong. Please try again'
    raise
