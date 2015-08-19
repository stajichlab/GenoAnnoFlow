AED_table <- read.table("AED_scores.txt")
AED_vector <- AED_table$V1
eAED_table <- read.table("eAED_scores.txt")
eAED_vector <- eAED_table$V1
png("AEDplot.png")
plot(ecdf(AED_vector), ylab="Frequency", xlab="AED scores", main="Cumulative frequency plot of AED scores")
dev.off()

png("eAEDplot.png")
plot(ecdf(eAED_vector), ylab="Frequency", xlab="eAED scores", main="Cumulative frequency plot of eAED scores")
