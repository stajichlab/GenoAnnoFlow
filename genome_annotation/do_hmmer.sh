#PBS -j oe -q js -l walltime=3:00:00 -N feuw.Pfam -l nodes=1:ppn=8

module load hmmer/3.1b1

if [ ! $PBS_NP ]; then
 PBS_NP=1
fi

hmmscan --cpu $PBS_NP --cut_ga --domtbl F_euwallaceae.all.maker.proteins.PfamA.domtbl /srv/projects/db/pfam/current/HMMER3.1b1/Pfam-A.hmm F_euwallaceae.all.maker.proteins.functional.fasta > F_euwallaceae.all.maker.proteins.PfamA.hmmscan

