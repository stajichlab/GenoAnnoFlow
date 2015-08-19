score_table = read.table("AED_scores.txt")
score_vector = score_table$V1
png("AEDplot.png")
plot(ecdf(score_vector), ylab="Frequency", xlab="AED scores", main="Cumulative frequency plot of AED scores")
