'''
works on the fasta file to performe the CDS check
Output the summary table of all transcript, CDS-failed summary table and failed ID

Xin Apr 1, 2013

'''

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

fasta=open(sys.argv[1],'r')

main_output=open(sys.argv[1][:-3] + '_CDS_check_table.txt','w') # contain all the information of all the transcripts
main_output.write('transcript\tCDS_check_code(no_start,no_end,premature_stop,not_3m)(0=OK,1=Fail)\n')

CDS_fail_output = open(sys.argv[1][:-3] + '_CDS_fail_table.txt', 'w') # write only failed transcripts and reasons
CDS_fail_output.write('failed_transcript\tCDS_check_code(no_start,no_end,premature_stop,not_3m)(0=OK,1=Fail)\n')
failedID = open(sys.argv[1][:-3] + '_failed_transcriptIDs.txt', 'w') # only write transcript IDs

def generate_codon_list(codon):
	'''
	generate codons use ? to replace base in different positon
	@para codon str
	@return list
	'''
	codon_list = []
	for i in (codon[0], 'N'):
		for j in (codon[1], 'N'):
			for k in (codon[2], 'N'):
				codon_list.append(''.join((i, j, k)))
	return codon_list

# create the start and stop codon list since there maybe 'N'
initiators = generate_codon_list('ATG')

terminators = []
	
for codon in ('TAA', 'TGA', 'TAG'):
	terminators.extend(generate_codon_list(codon))

terminators = list(set(terminators)) #remove the repeat codon by set operation

print initiators
print terminators
##########################################
print "read the fastq into dict"
all_record=SeqIO.parse(fasta,'fasta')
seq_dict={}

for record in all_record:
	transcript=record.id	
	seq=str(record.seq)
	seq_dict[transcript] = seq

##########################################

###################################################
print "start to check the CDS of each sequence"

bad_list = []

for transcript in seq_dict:
	
	seq = seq_dict[transcript]
	
	seq_length=len(seq)
	
	CDS_fail_reason = [0,0,0,0] # order: start, stop, premature stop, length is 3 multiple 
	
	### check the CDS ###	
	if seq[:3].upper() not in initiators:
		CDS_fail_reason[0] += 1
	
	if seq[-3:].upper() not in terminators:
		CDS_fail_reason[1] += 1

	if '*' in Seq(seq).translate()[:-1]:
		CDS_fail_reason[2] += 1
		
	if len(seq) % 3 != 0:
		CDS_fail_reason[3] += 1

	### write the CDS check result of one sequence into a string as code ###
	CDS_check_string = ''
	for reason in CDS_fail_reason:
		CDS_check_string += str(reason)+','



	### write the results into different output ###	
	main_output.write(('%s\t%s\n') % (str(transcript),CDS_check_string[:-1]))
	
	if '1' in CDS_check_string:
		CDS_fail_output.write(('%s\t%s\n') % (str(transcript),CDS_check_string[:-1]))
		
		bad_ID = str(transcript)
		if bad_ID not in bad_list:
			bad_list.append(bad_ID)


print "write CDS failed transcript IDs to output"
for i in bad_list:
	failedID.write(('%s\n') % (str(i))) # contain the CDS failed transcript IDs, even only one wolf failed


main_output.close()
CDS_fail_output.close()
failedID.close()

