import sys
from Bio import SeqIO

def reverse_complement(faa_filename):
	for record in SeqIO.parse(faa_filename, 'fasta'):
		print('>'+record.id)
		print(record.seq.reverse_complement())
def translate(faa_filename):
	for record in SeqIO.parse(faa_filename, 'fasta'):
		print('>'+record.id)
		print(record.seq.translate())

def get_fasta_by_id(faa_filename, ids_filename):
	# All ids of sequence to be extracted
	ids = []
	for line in open(ids_filename):
		ids.append(line.strip())

	# Get all fastas whose name are in the id list
	for record in SeqIO.parse(faa_filename, 'fasta'):
		if record.id in ids:
			SeqIO.write(record, sys.stdout, 'fasta') 

def stats(faa_filename):
	for record in SeqIO.parse(faa_filename, 'fasta'):
		print('%s\t%s'%(record.id, len(record)))

def main():
	if len(sys.argv) < 3:
		sys.stderr.write("Usage: fasta-reverse-and-complement.py <sub_command> <in.fasta>\n")
		sys.exit()
	
	sub_command = sys.argv[1]
	faa_filename = sys.argv[2]
	if sub_command == 'reversecomplement':
		reverse_complement(faa_filename)
	elif sub_command == 'translate':
		translate(faa_filename)
	elif sub_command == 'getfastabyid':
		if len(sys.argv) < 4:
			sys.stderr.write("Usage: fasta-reverse-and-complement.py <sub_command> <faa_filename> <ids_filename>\n")
			sys.exit()
		get_fasta_by_id(faa_filename, sys.argv[3])
	elif sub_command == 'stats':
		stats(faa_filename)
	else:
		sys.stderr.write("unknown sub_command\n")

if __name__ == '__main__':
	main()