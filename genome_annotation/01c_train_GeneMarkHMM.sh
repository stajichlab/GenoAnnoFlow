#PBS -l nodes=1:ppn=4,walltime=72:00:00,mem=16gb -j oe

module load genemarkHMM/4.21

SEQ_PATH=../../Annotation/MAKER_v1/Citrus_chr_polished_round2.fasta

perl gmes_petap.pl --cores $PBS_NP --pbs --ES --max_intergenic 50000 --test_set ../snap/export.dna --sequence $SEQ_PATH
