#!/bin/bash
#PBS -l nodes=1:ppn=8,walltime=200:00:00,mem=32gb
#PBS -N MAKER.Cr -j oe -o Maker.Cr.log

#qsub -d `pwd` -t 1-8 maker_job.sh
module load perl
module load maker
module load augustus/3.0.3
which augustus

maker 
