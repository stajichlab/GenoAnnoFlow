#PBS -j oe
module load stajichlab
module load stajichlab-perl
module load perl
module load maker/2.31.8

D=`dirname \`pwd\``
SPECIES=`basename $D`
PREF=`echo $SPECIES | perl -p -e 'my @n = split('_',$_); $_ = uc substr($n[0],0,1) . substr($n[1],0,3). "_"'`

echo $PREF
maker_map_ids  --prefix $PREF --iterate 0 --justify 5 $SPECIES.all.gff > $SPECIES.mapids
