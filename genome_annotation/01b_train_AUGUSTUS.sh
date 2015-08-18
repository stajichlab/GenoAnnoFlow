#!/bin/bash
#PBS -l nodes=1:ppn=1,mem=16gb,walltime=24:00:00 -j oe -N augTrain

SPECIES="Fairchild"
OLDPATH=$PATH

export PATH="/bigdata/wesslerlab/shared/Citrus/augustus/3.1/bin:/bigdata/wesslerlab/shared/Citrus/augustus/3.1/scripts:$PATH"
export AUGUSTUS_CONFIG_PATH="/bigdata/wesslerlab/shared/Citrus/augustus/3.1/config"

perl /rhome/twrightsman/git/GenoAnnoFlow/scripts/zff2augustus_gbk.pl ../snap/export.ann ../snap/export.dna > $SPECIES.train.gbk
autoAugTrain.pl --CRF --trainingset=$SPECIES.train.gbk --species=$SPECIES --optrounds=2

export PATH=$OLDPATH
