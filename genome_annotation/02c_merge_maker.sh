module load maker

$BASE = "Citrus_chr_polished_round2"

#generate summary annotation files from maker run
gff3_merge -g -n -d ${BASE}_master_datastore_index.log
fasta_merge -d ${BASE}_master_datastore_index.log

#isolate AED scores from maker annotation
grep -oP '_AED=(\S){4}' ${BASE}.all.gff | \
awk -F "=" '{print $2}' > AED_scores.txt

#isolate eAED scores
grep -oP '_eAED=(\S){4}' ${BASE}.all.gff | \
awk -F "=" '{print $2}' > eAED_scores.txt

#generate feature counts
awk '{if (!($1 ~ "#")){print $3}}' Citrus_chr_polished_round2.all.gff | sort | uniq -c > feature_count.txt

#make png images of cumulative frequency plots of AED/eAED scores
Rscript generateAEDplots.r

#make png image of bar plot for feature counts
Rscript generateFeatureCounts.r
