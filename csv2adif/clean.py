#!/usr/bin/env python

import re
import sys
import datetime

#fname = "W8AKS.txt"
fname = sys.argv[1]

class qso(object):
    def __init__(self,call):
        self.call = call
        self.start_time = 0
        self.end_time = 0
        self.location = None
        self.sent = 0
        self.recv = 0
        self.band = None
        self.freq = None

    def __str__(self):
        ret = "{}, {}, {}, {}, {}, {}, {}, {}".format(self.start_time,
                                          self.call,
                                          self.end_time,
                                          self.band,
                                          self.freq,
                                          self.location,
                                          self.sent,
                                          self.recv)
        return ret

    def clean_sig(self,sig):
        clean_sig = sig
        if sig[0] == 'R':
            clean_sig = sig[1:]
        return clean_sig

    def parse(self, line):


        search = re.compile("[A-Z][A-Z][0-9][0-9]")
        if line[-1] == '73':
            self.end_time = self.get_time(line[0])
        elif search.match(line[-1]):
            self.location = line[-1]
        elif line[-1] != 'RRR':
            if line[-2] == "KC4AAA":
                self.sent = self.clean_sig(line[-1])
            else:
                self.recv = self.clean_sig(line[-1])

        if line[1] == 'Transmitting' and self.start_time == 0:
            self.start_time = self.get_time(line[0])
            self.freq = line[2]
            if line[2] == '7.074':
                self.band = '40m'
            elif line[2] == '14.074':
                self.band = '20m'

    def get_time(self,in_time):
        if len(in_time) == 13:
            year = int(in_time[:2]) + 2000
            month = int(in_time[2:4])
            day = int(in_time[4:6])
            hour = int(in_time[7:9])
            minute = int(in_time[9:11])
            sec = int(in_time[11:13])
        else:
            year = self.start_time.year
            month = self.start_time.month
            day = self.start_time.day
            hour = int(in_time[:2])
            minute = int(in_time[2:4])
            sec = int(in_time[4:6])
        return datetime.datetime(year,month,day,hour,minute,sec)


if __name__ == "__main__":
    fd = open(fname)
    my_qso = qso(fname[:-4])
    data = fd.readlines()
    for line in data:
        n_line = line.strip()
        my_qso.parse(n_line.split())
    print(my_qso)


