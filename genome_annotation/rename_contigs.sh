perl -i -p -e 's/>NODE_(\d+)_length_/>ctg_$1 /' *.fasta
