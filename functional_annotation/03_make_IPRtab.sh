for file in *.d
do
 b=`basename $file .d`
 cat $file/*.tsv > $b.IPROUT.tab
done
