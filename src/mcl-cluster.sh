#!/bin/bash
for i in ./edges/*.txt
do
    ## Get the file name
    fname="${i##*/}"
    echo "processing $fname"
    mcl ./edges/$fname --abc -o clusters_$fname.tsv

done
