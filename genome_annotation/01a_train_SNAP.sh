#!/bin/bash
#PBS -l nodes=1:ppn=1,mem=8gb,walltime=4:00:00

module load snap/0.15.4
module load maker/2.31.8

SPECIES="Fairchild"
AED_CUTOFF="0.08"

maker2zff -x $AED_CUTOFF -d ../../Annotation/MAKER_v1/Citrus_chr_polished_round2.maker.output/Citrus_chr_polished_round2_master_datastore_index.log
fathom genome.ann genome.dna -categorize 1000
fathom uni.ann uni.dna -export 1000 -plus

mkdir hmm
cd hmm
forge ../export.ann ../export.dna
cd ..

hmm-assembler.pl -x $SPECIES hmm > $SPECIES.snap_intronlen.hmm
hmm-assembler.pl $SPECIES hmm > $SPECIES.snap.hmm
