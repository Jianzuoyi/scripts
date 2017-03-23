import sys
from Bio import SeqIO

for record in SeqIO.parse(sys.argv[1], 'genbank'):
	 
	for feature in record.features:
		if feature.type == 'source':
			organism = feature.qualifiers['organism'][0]
			plasmid = False
			if 'plasmid' in feature.qualifiers.keys():
				plasmid = True 
		if 'translation' in feature.qualifiers.keys():
			locus_tag = feature.qualifiers['locus_tag'][0]
			product = feature.qualifiers['product'][0]
			if plasmid:
				header = '>gnl|'+record.dbxrefs[0].split(':')[1] + "|" + locus_tag + " " + product + " " + "(plasmid) " + "[" + organism + "]"
			else:
				header = '>gnl|'+ record.dbxrefs[0].split(':')[1] + "|" + locus_tag + " " + product + " " + "[" + organism + "]"
			print("%s \n%60s\n" % (header, feature.qualifiers['translation'][0]))
