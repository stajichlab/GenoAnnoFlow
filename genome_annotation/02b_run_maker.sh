#!/bin/bash
#PBS -l noes=1:ppn=8,walltime=200:00:00,mem=32gb
#PBS -N MAKER -j oe -o MAKER.log

#(!!) This script can be run as an array job: (!!)
#qsub -d `pwd` -t 1-8 02b_run_maker.sh

module load perl
module load maker

OLDPATH=$PATH
export PATH="/bigdata/wesslerlab/shared/Citrus/augustus/3.1/bin:/bigdata/wesslerlab/shared/Citrus/augustus/3.1/scripts:$PATH"

maker

export PATH=$OLDPATH
