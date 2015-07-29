# ------------------------------------------------------------------------------
#  BCH_WHO.R
#  Mortality data from World Health Organization 
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Program written by:  Espen Henriken, October 2012, later adapted by Dave  
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear memory, set directory for output 
rm(list=ls())
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/JIE_2013"
setwd(dir)
# subdir for backups 
backup <- "backups"

# load packages
library("gdata")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Demographic data 
years <- c("1990","2000","2011")

# Loads, formats and saves WHO life tables

for(y in 1:length(years)){
  prefix <- c("http://apps.who.int/whosis/database/life_tables/download/life_")
  suffix <- c(".csv")
  
  namesabb <- data.frame(read.csv("countrycodes.csv", na.strings="", skip = 0))
  
  for(i in 1:nrow(namesabb)){
    filename <- paste(prefix,namesabb[i,1],"_",years[y],suffix,sep="") 
    assign(paste("lt_",namesabb[i,2],years[y],sep=""), data.frame(read.csv(filename, na.strings="", skip = 2)))
  }
  
  rm("filename","i","namesabb","prefix","suffix")
  
  save(list = ls(all=TRUE), file = paste("whodata",years[y],".RData",sep=""))
}



# OLD STUFF 
# 4. Plot capital-output ratios 
# ------------------------------------------------------------------------------
# reload data (you can start program here)
rm(list=ls())
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/JIE_2013"
setwd(dir)
load("PWT.RData")

# temp calc
#xx <- pwt[pwt$isocode == "USA" & pwt$year > 1989,]
#mean(xx$ki)

# select countries 
list.countries <- c("CHN", "DEU", "JPN", "USA")
pwt$isocode <- gsub("GER", "DEU", pwt$isocode) 

pwt_sub <- pwt[pwt$isocode %in% list.countries,]
ky <- pwt_sub$KY
ky <- matrix(ky, ncol=4)
colnames(ky) <- list.countries
ky_ts = ts(ky, start=1950, frequency=1)
ky_ts <- window(ky_ts, start=1980)

# plot all countries together 
plot.name <- "figs/BCH_ky.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,3,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
plot(ky_ts,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Capital-Output Ratio", main="",
)
mtext("Source: Penn World Table and authors calculations", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=list.countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
