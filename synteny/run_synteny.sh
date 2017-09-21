#!/bin/bash

export PATH=/its1/GB_BT2/jianzuoyi/biosoft/mummer/bin/:/its1/GB_BT2/jianzuoyi/biosoft/gnuplot:/its1/GB_BT2/jianzuoyi/biosoft/gnuplot/bin:$PATH
NUCMER=/its1/GB_BT2/jianzuoyi/biosoft/mummer/bin/nucmer
REFERENCE=all_p_h_5k_1.fa
QUERY=all_p_h_5k_1.pilon.fasta
OUTBASE=pilon.synteny
THREADS=32

$NUCMER -p $OUTBASE -t $THREADS $REFERENCE $QUERY

delta-filter -r -q -g ${OUTBASE}.delta > ${OUTBASE}.delta.filter

mummerplot ${OUTBASE}.delta.filter -R $REFERENCE -Q $QUERY --postscript
