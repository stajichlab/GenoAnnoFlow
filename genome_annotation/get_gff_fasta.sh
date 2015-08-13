#PBS -l nodes=1:ppn=1 -j oe -l walltime=4:00:00

module load perl
module load stajichlab
module load maker/2.31.8
D=`dirname \`pwd\``
SPECIES=`basename $D`

fasta_merge -d $SPECIES.maker.output/$SPECIES"_master_datastore_index.log"
gff3_merge -d $SPECIES.maker.output/$SPECIES"_master_datastore_index.log"
