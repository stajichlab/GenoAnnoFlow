module load maker

BASE="Citrus_chr_polished_round2"

maker_map_ids --prefix $BASE --iterate 0 --justify 5 $BASE.all.gff > $BASE.id.map
