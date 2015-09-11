#!/usr/bin/env python

__version__ = 1.0

INFO = """
fastatools - FASTA sequence manipulation tools
version: %s

Zuoyi Jian (jianzuoyi@gmail.com)

""" % __version__

import sys
import argparse

from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio import SeqIO

def _translate(args):
	for record in SeqIO.parse(args.fasta, 'fasta'):
		print(">"+record.id)
		print(record.seq.translate())

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=INFO)
	subparser = parser.add_subparsers(help="sub-commands")

	# parse translation arguments 
	parser_fasta = subparser.add_parser('translate', help=("translate FASTA file"))
	parser_fasta.add_argument('fasta', type=argparse.FileType('r'), help=("FASTA file"))
	parser_fasta.set_defaults(func=_translate)

	# Parse arguments and run the sub-command 
	args = parser.parse_args()
	args.func(args)
