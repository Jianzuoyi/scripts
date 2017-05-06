# Here specify the directory where the sequences deposit,
# the dir only must only include the sequences data
DATA=/its1/GB_BT2/jianzuoyi/SRA/xinandaxue_F14FTSCCKW0174-F14FTSCCKF0205/data/F14FTSCCKF0205_PRUtcyE/fq

# Upload data by ascp
ASCP=/opt/bio/aspera_connect/bin/ascp
ASCPKEY=/its1/GB_BT2/jianzuoyi/biosoft/ascp/aspera.openssh
$ASCP -i $ASCPKEY -QT -l100m -k1 -d $DATA  subasp@upload.ncbi.nlm.nih.gov:uploads/jianzuoyi@qq.com_1xRqFBNk
