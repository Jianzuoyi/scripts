import sys
from Bio import SeqIO
'''
def read_fasta(fp):
	name,seq='',''
	for line in fp:
		#print(line)
		line=line.strip()
		if line.startswith('>'):
			if name!='':yield(name,seq)
			name,seq=line,''
		else:
			seq+=line
	if name!='':yield(name,seq)
'''

if __name__=='__main__':
	if len(sys.argv)<3:
		print("subseq.py [input file] [chrom_id:start-end]")
		raise

	fin=sys.argv[1]
	chrom=sys.argv[2].split(':')[0]
	start=int(sys.argv[2].split(':')[1].split('-')[0])
	end=int(sys.argv[2].split(':')[1].split('-')[1])
	#print(fin,chrom,start,end)
	for record in SeqIO.parse(sys.argv[1], "fasta"):
		if record.id==chrom:
			#print('seqlen%s'%len(seq))
			if start <= end:
				print(record.seq[start-1:end])
			else:
				print(record.seq[start-1:end-2:-1].complement())
			break
		