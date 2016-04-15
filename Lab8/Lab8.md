###Sam Deslandes - Lab 8   

#####Working with R
Although this lab was mostly straight forward, it was quite frustrating to get started. One of the largest challenges faced in this lab was 
getting more than one rule when using apriori. In order to get more rules I had to lower the support and confidence parameters.  

At first I looked at the ranks of the individuals who were admitted. 
```
admissions <- read.csv(file="C:\\GitProjects\\CSCI2963\\Lab8\\binary.csv",head=TRUE,sep=",")
col_names <- names(admissions)
admissions[,col_names] <- lapply(admissions[,col_names] , factor)
library(arules)
rules <- apriori(admissions,parameter = list(minlen=2,supp=0.002,conf=0.2),
				 appearance=list(rhs=c("admit=1"),lhs=c("rank=1","rank=2","rank=3","rank=4"),
				 default="none"))
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
```
The resulting rules were:  
![rules1](http://puu.sh/oaRPH/da565142ef.png)

In order to garner more rules I changed the lhs of teh apriori algorithm to default. The new rule is as follows:
```
rules <- apriori(admissions,parameter = list(minlen=2,supp=0.005,conf=0.8),
				 appearance=list(rhs=c("admit=1"),default="lhs"))
``` 

The results:  
![rules2](http://puu.sh/oaSb5/57da5696bb.png)
![graph](http://puu.sh/oaSe3/1e8b1b370c.png)

#####Project progress
This was a busy week which left me with no time to work on my project.
