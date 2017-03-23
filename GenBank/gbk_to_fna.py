import sys
from Bio import SeqIO

# SeqIO.convert(gb_file, 'genbank', 'CP019114-5.fna', 'fasta')
			
# For comparison, construct the FASTA file "by hand" giving full control:
for record in SeqIO.parse(sys.argv[1], 'genbank'):
	# Source nucleotides
	print(">%s %s\n%s\n " % (record.id, record.description, record.seq))

	# Features nucleotides
	"""
	for feature in record.features:
		locus_tag = ""
		product = ""
		if 'product' in feature.qualifiers.keys():
			product = feature.qualifiers['product'][0]
		if 'locus_tag' in feature.qualifiers.keys():
			locus_tag = feature.qualifiers['locus_tag'][0]
			location = str(int(feature.location.start)) + ":" + str(int(feature.location.end)) + "(" + str(feature.location.strand) + ")"
			print(">%s %s\n%s\n" % (locus_tag, location + " " + feature.type + " " + product, str(feature.extract(record.seq))))
"""
