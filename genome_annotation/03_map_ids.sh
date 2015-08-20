module load maker

BASE="Citrus_chr_polished_round2"
SPECIES="Fairchild"

maker_map_ids --prefix $SPECIES --iterate 0 --justify 5 $BASE.all.gff > $BASE.id.map

map_fasta_ids $BASE.id.map $BASE.all.maker.proteins.fasta
map_fasta_ids $BASE.id.map $BASE.all.maker.transcripts.fasta
map_gff_ids $BASE.id.map $BASE.all.gff
