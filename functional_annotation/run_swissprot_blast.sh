#PBS -l nodes=1:ppn=12 -q js -N spblast -j oe
module load ncbi-blast
D=`dirname \`pwd\``
SPECIES=`basename $D`
blastp -query $SPECIES.all.maker.proteins.fasta -db /bigdata/stajichlab/shared/db/uniprot/uniprot_sprot.fasta -use_sw_tback \
-num_threads $PBS_NP -outfmt 6 -evalue 1e-3 -out $SPECIES.all.maker.swissprot.BLASTP -max_target_seqs 5
