import sys

if len(sys.argv) < 2:
	print("Usage: python %s <sequence>"%(sys.argv[0]))
	sys.exit()

fin_sequence = sys.argv[1]

def count(seq):
	# nucleotides count
	A = 0
	T = 0
	C = 0
	G = 0
	AT = 0
	CG = 0

	begin = 0
	end = len(seq) - 1
	for i in xrange(0, end + 1):
		if seq[i] == 'A' or seq[i] == 'a':
			A += 1
		elif seq[i] == 'T' or seq[i] == 't':
			T += 1
		elif seq[i] == 'C' or seq[i] == 'c':
			C += 1
		elif seq[i] == 'G' or seq[i] == 'g':
			G += 1
		if i < end:
			if (seq[i] == 'C' or seq[i] == 'c') and (seq[i+1] == 'G' or seq[i+1] == 'g'):
				CG += 1
		if i < end:
			if (seq[i] == 'A' or seq[i] == 'a') and (seq[i+1] == 'T' or seq[i+1] == 't'):
				AT += 1
	seq_len = len(seq)
	print('A\t%s\tT\t%s'%(A*1.0 / seq_len, T*1.0 / seq_len))
	print('C\t%s\tG\t%s'%(C*1.0 / seq_len, G*1.0 / seq_len))
	print('CG\t%s'%(CG*1.0 / seq_len))
	print('AT\t%s'%(AT*1.0 / seq_len))

def for_each_sequence():
	chrom = ''
	seq = ''
	for line in open(fin_sequence):
		if line[0] == '>':
			if len(seq) != 0:
				count(seq)
			chrom = line.strip()
			seq = ''
		else:
			seq += line.strip()
	if len(seq) != 0:
		count(seq)

if __name__ == '__main__':
	for_each_sequence()