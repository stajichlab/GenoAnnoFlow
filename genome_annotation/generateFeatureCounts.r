library("ggplot2")

input <- read.table("feature_counts.txt")
feature_counts <- input$V1
names(feature_counts) <- input$V2

png("feature_counts.png")
par(las=2, mar=c(9,5,3,1))
barplot(feature_counts, main="Feature Counts", names.arg=names(feature_counts))

