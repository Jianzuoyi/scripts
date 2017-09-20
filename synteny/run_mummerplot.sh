#!/bin/bash
export PATH=/its1/GB_BT2/jianzuoyi/biosoft/mummer/bin/:/its1/GB_BT2/jianzuoyi/biosoft/gnuplot:/its1/GB_BT2/jianzuoyi/biosoft/gnuplot/bin:$PATH
mummerplot synteny.delta.filter -R ecoli_NC_002695.fasta -Q ecoli.contigs.fasta --postscript
