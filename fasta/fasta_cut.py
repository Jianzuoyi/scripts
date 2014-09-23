import sys

def read_fasta(fp):
	name, seq = '', ''
	for line in fp:
		#print(line)
		line = line.strip()
		if line.startswith('>'):
			if name != '': yield(name, seq)
			name, seq = line, ''
		else:
			seq += line
	if name != '': yield(name, seq)


def cut(fp):
	for name, seq in read_fasta(fp):
		if len(seq) > 10000:
			seq = seq[0:10000]
		print(name)
		print(seq)

if __name__ == '__main__':
	'''
	if len(sys.argv) < 2:
		print("Usage: fasta_cut <fastafile>")
	'''
	#fin_fasta = sys.argv[1]
	with open ('genome.fa') as fp:
		#cut(fp)
		for name, seq in read_fasta(fp):
			print(name, len(seq))
			#print(seq)
	
	