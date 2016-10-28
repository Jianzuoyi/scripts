#!/bin/bash
#	Install blast+ software

wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.5.0+-x64-linux.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.5.0+-x64-linux.tar.gz.md5
md5sum -c --status ncbi-blast-2.5.0+-x64-linux.tar.gz.md5
if [[ $? != 0 ]]; then
	echo "Failed to download blast+" > blast+.error
	exit 1
fi

tar xvf ncbi-blast-2.5.0+-x64-linux.tar.gz
# Use blast+
"""

"""