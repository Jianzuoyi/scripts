import sys
from Bio import SeqIO

def main():
	for record in SeqIO.parse(sys.argv[1], 'fasta'):
		print(record.id, len(record))

if __name__ == '__main__':
	main()