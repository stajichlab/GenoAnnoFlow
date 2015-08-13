#PBS -j oe
module load stajichlab
module load stajichlab-perl
module load perl
module load maker/2.31.6

D=`dirname \`pwd\``
SPECIES=`basename $D`

map_fasta_ids $SPECIES.mapids $SPECIES.all.maker.proteins.fasta
map_fasta_ids $SPECIES.mapids $SPECIES.all.maker.transcripts.fasta
map_gff_ids $SPECIES.mapids $SPECIES.all.gff 
