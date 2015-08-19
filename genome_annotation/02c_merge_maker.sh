module load maker

$BASE = "Citrus_chr_polished_round2"

gff3_merge -g -n -d ${BASE}_master_datastore_index.log
fasta_merge -d ${BASE}_master_datastore_index.log

grep -oP '_AED=(\S){4}' ${BASE}.all.gff | \
awk -F "=" '{print $2}' > AED_scores.txt

Rscript generateAEDplot.r
