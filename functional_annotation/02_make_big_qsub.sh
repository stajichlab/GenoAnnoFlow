for file in `cat folders`; do 
 cd $file; 
 n=`wc -l peplist | awk '{print $1}'`; 
 nm=`echo $file | perl -p -e '($_)= split(/\./,$_); $_ .= "\n"'`;
 echo "qsub -q batch -l nodes=1:ppn=1,mem=16gb -d `pwd` -t 1-$n -N $nm run_interpro.sh"; 
 cd ..; 
done
