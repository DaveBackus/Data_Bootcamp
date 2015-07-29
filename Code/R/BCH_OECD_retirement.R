# ------------------------------------------------------------------------------
#  BCH_OECD_retirement.R  
#  Effective retirement ages from OECD for 
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Source:  OECD, Statistics on average effective age of retirement
#  http://www.oecd.org/els/public-pensions/ageingandemploymentpolicies-statisticsonaverageeffectiveageofretirement.htm
#  Adapted by Dave Backus from code written by Espen and Paul 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)

# load packages
library("gdata")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Read data 

file <- "OECD_retirement_age_timeseries_May_13.xlsx"
data <- read.xls(file, sheet="BCH", header=TRUE) 


# ------------------------------------------------------------------------------
# 2. Data manipulation and plot 

# convert to ts 
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,2:ncol(dataset)]), 
    # note column one is the row names 
    start=1970, 
    frequency=1
  )
  # label with country names 
  colnames(ts_data) <- as.character(data$Country)
  return(ts_data)
}

data_ts <- convert_to_ts(data)
data_ts <- window(data_ts, start=1980, end=2011)

# plot all countries together 
plot.name <- "figs/BCH_retirement.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
plot(data_ts,
     plot.type='single',
     lty=1,  
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Effective Retirement Age", main="",
)
mtext("Source: OECD, Average Effective Age of Retirement", side=1, line=2.5, cex=1, adj=0)
legend("bottomleft", legend=colnames(data_ts), cex=1, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
#dev.print(device=pdf, file=plot.name, width=8, height=6)

