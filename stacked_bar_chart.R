library(ggplot2)
library(tidyr)

pdf("exit.pdf")

data <- data.frame(read.csv('steamPlayLog.csv', header = TRUE))
data <- transform(data, Launch=as.Date(Launch, format="%Y-%m-%d"))
data %>% complete(Launch = seq(min(Launch), max(Launch), by="day"))

d <-ggplot(data, aes(fill=Game, y=Minutes, x=Launch)) + geom_bar(position='stack', stat='identity') + scale_x_date(date_labels=" %Y-%m-%d") 
d + theme(axis.text.x = element_text(angle = 50, vjust = 1, hjust=1))
