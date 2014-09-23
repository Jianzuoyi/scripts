# find overlap regions of elements in chromosome

import sys

if len(sys.argv) < 3:
	print("Usage: python %s positions positions2 [-d=show_detail]"%sys.argv[0])
	sys.exit()

fin_positions = sys.argv[1]
fin_positions2 = sys.argv[2]
show_detail = ''
if len(sys.argv) > 3:
	show_detail = sys.argv[3]

# position1 
position1_number = 0
position2_number = 0
positions = []
for line in open(fin_positions):
	cols = line.strip().split()
	if not cols: continue
	start = int(cols[1])
	end = int(cols[2])
	positions.append((start, end))
#print(positions)
position1_number = len(positions)
# position 2 
overlaps = 0
overlap_hits = 0
left_overlap = 0
include = 0
included = 0
right_overlap = 0
for line in open(fin_positions2): 
	cols = line.strip().split()
	if not cols: continue
	start2 = int(cols[1])
	end2 = int(cols[2])
	position2_number += 1
	for start, end in positions:
		# find overlap 
		overlap = ''
		overlap_type = ''
		if end >= start2 and start <= end2:	# has overlap; no overlap: end < start2 or start > end2
			#print('has overlap')
			overlap_hits += 1
			if start < start2 and end <= end2:		# left overlap
				#print('left overlap')	
				overlap = (end - start2 + 1)
				overlap_type = 'left'
				left_overlap += 1
			elif start < start2 and end > end2:		# include
				#print('include')
				overlap = (end2 - start2 + 1)
				overlap_type = 'include'
				include += 1
			elif start >= start2 and end <= end2:	# be included
				#print('be included')
				overlap = (end - start + 1)
				overlap_type = 'beincluded'
				included += 1
			elif start >= start2 and end > end2:	# right overlap
				#print('right overlap')
				overlap = (end2 - start + 1)
				overlap_type = 'right'
				right_overlap += 1
			overlaps += overlap
			# show detail: print overlap
			if show_detail == '-d':
				seq_positions = ''
				seq_positions2 = ''
				if overlap_type == 'left':
					seq_positions = '%s%s%s%s' % (start, '+' * 20, '*'*20,end)
					seq_positions2 = '%s%s%s%s%s%s%s' % (' '*20, start2, '*'*10, overlap, '*'*10, '-'*20, end2)
				elif overlap_type == 'include':
					seq_positions = '%s%s%s%s%s' % (start, '+'*20, '+'*20, '+'*20, end)
					seq_positions2 = '%s%s%s%s%s%s' % (' '*20, start2, '*' * 10, overlap, '*'*10,end2)
				elif overlap_type == 'beincluded':
					seq_positions2 = '%s%s%s%s%s' % (start2, '-'*20, '-'*20, '-'*20, end2)
					seq_positions = '%s%s%s%s%s%s' % (' '*20, start, '*' * 10, overlap, '*'*10,end)
				elif overlap_type == 'right':
					seq_positions2 = '%s%s%s%s' % (start2, '-' * 20, '*'*20,end2)
					seq_positions = '%s%s%s%s%s%s%s' % (' '*20, start, '*'*10, overlap, '*'*10, '+'*20, end)
				print(seq_positions)
				print(seq_positions2)
				'''
				indent = start - start2
				seq_region1 = '%s%s%s' % (start, '-' * abs(indent)*2, end)
				seq_region2	= '%s%s%s' % (start2, '+' * abs(indent)*2, end2)
				
				if indent > 0:
					seq_region1 = ' ' * abs(indent) + seq_region1
				else:
					seq_region2 = ' ' * abs(indent) + seq_region2
				print(seq_region1)
				print(seq_region2) 
				'''

print('overlaps[TP]\t%s'%overlaps)
print('overlap hits\t%s'%overlap_hits)
print('position1\t%s'%position1_number)
print('positions2\t%s'%position2_number)
print('left overlap\t%s'%left_overlap)
print('include\t%s'%include)
print('included\t%s'%included)
print('right overlap\t%s'%right_overlap)


