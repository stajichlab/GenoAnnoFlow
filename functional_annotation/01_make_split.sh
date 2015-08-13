module load perl
for file in `ls *.fasta`
do
 base=`basename $file .fasta`
 mkdir $base.d
 cd $base.d
 bp_dbsplit.pl -s 50 -p split-$base ../$file
 ls split-$base.* > peplist
 ln -s ../run_interpro.sh
 cd ..
done
