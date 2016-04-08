admissions <- read.csv(file="C:\\GitProjects\\CSCI2963\\Lab8\\binary.csv",head=TRUE,sep=",")
col_names <- names(admissions)
admissions[,col_names] <- lapply(admissions[,col_names] , factor)
library(arules)
rules <- apriori(admissions,parameter = list(minlen=2,supp=0.005,conf=0.8),appearance=list(rhs=c("admit=1"),lhs=c("rank=1","rank=2","rank=3","rank=4"),default="lhs"))
quality(rules)<-round(quality(rules),digits=3)
rules.sorted <- sort(rules,by="lift")
inspect(rules.sorted)
 
subset.matrix <- is.subset(rules.sorted, rules.sorted)
subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
redundant <- colSums(subset.matrix, na.rm=T) >= 1
which(redundant)
rules.pruned <- rules.sorted[!redundant]
inspect(rules.pruned)

library(arulesViz)
plot(rules,method = "graph", control=list(type="items"))
