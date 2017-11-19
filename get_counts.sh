#!/bin/bash

ssb_uniq=$(cat 2017_11_17.xml \
  | sed 's/ /_/g' \
  | tr -d "\n"  \
  | tr -d "\r" \
  | sed 's/<Row>/\n/g' \
  | tr  "\t" " "\
  | sed 's/<Cell>//g' \
  | sed 's/<\/Cell>//g' \
  | sed -e 's/ss:Type="[^>]*">//g' \
  | sed 's/<Data//g' \
  | sed 's/<\/Data>//g' \
  | awk '{print $104, $12, $58}' \
  | grep James \
  | tr -d "_" \
  | grep -v '^2015' \
  | grep -v '2017-01-\(01\|02\|15\|16\)' \
  | awk '{print $2}' \
  | sort \
  | tee /tmp/ssb_total.dat \
  | uniq \
  | tee /tmp/count.dat\
  | wc -l)

ssb_total=$(cat /tmp/ssb_total.dat |wc -l)


ft8_total=$(cat logs.csv |wc -l)

ft8_uniq=$(cat logs.csv \
  | awk -F , '{print $3}' \
  | sort \
  | uniq \
  | tee -a /tmp/count.dat \
  | wc -l)


total=$(expr ${ssb_total} + ${ft8_total})
uniq=$(cat /tmp/count.dat \
  | sort \
  | uniq \
  | wc -l)

echo "-----------------------------------"
echo "Total SSB:  ${ssb_total} QSOs"
echo "Unique SSB: ${ssb_uniq} Callsigns"
echo "Total FT8:  ${ft8_total} QSOs"
echo "Unique FT8: ${ft8_uniq} Callsigns"
echo "-----------------------------------"
echo "Total:  ${total} QSOs"
echo "Unique: ${uniq} Callsigns"
echo "-----------------------------------"
