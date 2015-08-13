#PBS -l nodes=1:ppn=2 -q js -N spblast -j oe
SIZE=500
module load ncbi-blast
D=`dirname \`pwd\``
SPECIES=`basename $D`
PREFIX=$SPECIES
CPU=1
if [ $PBS_NP ]; then
 CPU=$PBS_NP
fi

if [ $PBS_ARRAYID ]; then
 N=$PBS_ARRAYID
fi

if [ ! $N ]; then 
 N=$1
fi

if [ ! $N ]; then
 echo "No ID num provided";
 exit;
fi

if [ ! -d $PREFIX.BLAST ]; then
 mkdir $PREFIX.BLAST
 bp_dbsplit --size 500 --prefix $PREFIX.BLAST/db $SPECIES.all.maker.proteins.fasta
fi

if [ ! -f $PREFIX.BLAST/$PREFIX.$N.BLASTP ]; then
blastp -query $PREFIX.BLAST/db.$N -db /bidgata/stajichlab/shared/db/uniprot/uniprot_sprot.fasta -use_sw_tback \
-num_threads $CPU -outfmt 6 -evalue 1e-3 -out $PREFIX.BLAST/$PREFIX.$N.BLASTP -max_target_seqs 5
fi
