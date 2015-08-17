#!/bin/bash
#PBS -l nodes=1:ppn=4,mem=32gb,walltime=72:00:00

module load augustus/3.0.3

GENE_FILE=$1
SPECIES=citrus_reticulata
TEST_GENES=200

AUGUSTUS_CONFIG_PATH=/opt/linux/centos/7.x/x86_64/pkgs/augustus/3.0.3/config

#Split gene structure set into training and test set
randomSplit.pl $GENE_FILE $TEST_GENES

#Create a meta parameters file
new_species.pl --species=$SPECIES --ignore --AUGUSTUS_CONFIG_PATH=$AUGUSTUS_CONFIG_PATH

#Make an initial training
etraining --species=$SPECIES $1.train
augustus --species=$SPECIES $1.test > firsttest.out

#Run optimize_augustus.pl
optimize_augustus.pl --species=$SPECIES $1.train

etraining --species=$SPECIES $1.train

augustus --species=$SPECIES $1.test | tee secondtest.out

