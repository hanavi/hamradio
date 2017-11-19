#!/usr/bin/env python

fname = "logs.csv"
fd = open(fname)
data = fd.readlines()[1:]

def rst(my_rst):
    if my_rst == "0":
        return "+00"
    else:
        if my_rst[0] == "-":
            s = my_rst[0]
            n = int(my_rst[1:])
        else:
            s = "+"
            n = int(my_rst)
        return "{}{:02}".format(s,n)

for line in data:

    sline = line.split(",")
    dateon = sline[0].replace("/","")
    timeon = sline[1].replace(":","")
    call = sline[2]
    dateoff = sline[3].replace("/","")
    timeoff = sline[4].replace(":","")
    band = sline[5]
    freq = sline[6] + "000"
    gridsquare = sline[7]
    rst_sent = rst(sline[8])
    rst_rcvd = rst(sline[9].strip())

    dateoff = "20"+dateoff[4:] + dateoff[:4]
    dateon = "20"+dateon[4:] + dateon[:4]

    if len(timeon) == 5:
        timeon = "0" + timeon

    if len(timeoff) == 5:
        timeoff = "0" + timeoff

    output = ("<call:{}>{} "
              "<gridsquare:4>{} "
              "<mode:3>FT8 "
              "<rst_sent:3>{} "
              "<rst_rcvd:3>{} "
              "<qso_date:8>{} "
              "<time_on:6>{} "
              "<qso_date_off:8>{} "
              "<time_off:6>{} "
              "<band:3>{} "
              "<freq:{}>{} "
              "<station_callsign:6>KC4AAA "
              "<my_gridsquare:6>JA00aa "
              "<operator:5>AI4LX "
              "<my_country:10>Antarctica "
              "<my_name:5>James <eor>")
    output = output.format(len(call),call,
                           gridsquare,
                           rst_sent,
                           rst_rcvd,
                           dateon,
                           timeon,
                           dateoff,
                           timeoff,
                           band,
                           len(freq), freq)

    print(output)


