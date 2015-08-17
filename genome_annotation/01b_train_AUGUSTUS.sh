#!/bin/bash
#PBS -l nodes=1:ppn=1,mem=16gb,walltime=48:00:00 -j oe -n augTrain

SPECIES="Fairchild"

export PATH="/bigdata/wesslerlab/shared/Citrus/augustus/3.1/bin:/bigdata/wesslerlab/shared/Citrus/augustus/3.1/scripts:$PATH"
CONFIG="/bigdata/wesslerlab/shared/Citrus/augustus/3.1/config"

new_species.pl --species=$SPECIES --AUGUSTUS_CONFIG_PATH=$CONFIG --ignore

perl /rhome/twrightsman/git/GenoAnnoFlow/scripts/zff2augustus_gbk.pl ../snap/export.ann ../snap/export.dna > $SPECIES.train.gbk
autoAugTrain.pl --CRF --trainingset=$SPECIES.train.gbk --species=$SPECIES --optrounds=2

