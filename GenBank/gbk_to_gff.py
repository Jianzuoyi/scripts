import sys
from Bio import SeqIO

for record in SeqIO.parse(sys.argv[1], 'genbank'):
	cols = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
	fields = {}
	for col in cols:
		fields[col] = ''
	fields['seqname'] = record.id
	fields['source'] = "GenBank"
	for feature in record.features:
		fields['feature'] = feature.type
		fields['start'] = str(int(feature.location.parts[0].start + 1))
		fields['end'] = str(int(feature.location.parts[-1].end))
		if feature.location.strand == 1:
			fields['strand'] = '+'
		else:
			fields['strand'] = '-'
		fields['score'] = '.'
		fields['frame'] = '.'
		# Attribute
		attribute = []
		for key, value in feature.qualifiers.items():
			#print(key + "=" + value[0])
			attribute.append(key + "=" + value[0])
		fields['attribute'] = ';'.join(attribute)
		# Print to stdout
		line = []
		for col in cols:
			line.append(fields[col])
		#line = fields.values()
		print('\t'.join(line))