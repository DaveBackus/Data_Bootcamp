# ------------------------------------------------------------------------------
#  BCH_WHO.R
#  Data from World Heatlh Organization, Global Health Observatory 
#    http://www.who.int/gho/en/
#  Specific links below in the code
#  Guide to new version of data 
#  Data files 
#    LIFE_0000000029 : nMx - age-specific death rate between ages x and x+n
#    LIFE_0000000030 : nqx - probability of dying between ages x and x+n
#    LIFE_0000000031 : lx - number of people left alive at age x
#    LIFE_0000000032 : ndx - number of people dying between ages x and x+n
#    LIFE_0000000033 : nLx - person-years lived between ages x and x+n
#    LIFE_0000000034 : Tx - person-years lived above age x
#    LIFE_0000000035 : ex - expectation of life at age x
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Program written by:  Espen Henriken, October 2012, later adapted by Dave  
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear memory, set directory for output 
rm(list=ls())
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/JIE_2013"
setwd(dir)

# load packages
#library("gdata")
library("RCurl")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Life Table data, new API as of 2013  

#url <- "http://apps.who.int/gho/athena/data/data-text.csv?target=GHO/LIFE_0000000029,LIFE_0000000030,LIFE_0000000031,LIFE_0000000032,LIFE_0000000033,LIFE_0000000034,LIFE_0000000035&profile=text&filter=COUNTRY:USA"
prefix <- "http://apps.who.int/gho/athena/data/data-text.csv?target=GHO/"
nmx <- "LIFE_0000000029"
nqx <- "LIFE_0000000030"
lx  <- "LIFE_0000000031" 
suffix <- "&profile=text&filter=COUNTRY:"

# test 
#gho <- read.csv(paste(prefix, "LIFE_00000000031", suffix, "CHN", sep=""))

# read in mortality data for a list of countries
# read does one at a time, then stacks them up 
noquote("Read GHO data one country at a time...")
countries <- c("CHN", "DEU", "JPN", "USA")

gho <- do.call(rbind,
  lapply(countries, 
    function(country) {
      print(country)
      url <- paste(prefix, nmx, suffix, country, sep="")
#      download.file(url, paste("backups/GHO_",country,"_",Sys.Date(),".csv",sep=""),  
#                    method="auto", quiet=FALSE) 
      data <- read.csv(url)
      return(data)
    }
  )
)

save(list=ls(all=TRUE), file="WHO.RData")

# ------------------------------------------------------------------------------
# 2. Data selection and plot 
# ** start here after setting directory 
noquote("Clear workspace and load data...")
rm(list=ls())
load("WHO.RData")

# for later use 
dates = c("1990", "2000", "2011")

# convert age to factor, set levels so that we can sort later 
# https://stat.ethz.ch/pipermail/r-help/2011-October/292738.html
ages = c("<1", "1-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", 
         "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", 
         "80-84", "85-89", "90-94", "95-99", "100+")
gho$Age.Group <- factor(gho$Age.Group, levels=ages)

# sort 
# http://stackoverflow.com/questions/1296646/how-to-sort-a-dataframe-by-columns-in-r
gho <- gho[with(gho, order(Year, Sex, Indicator, Country, Age.Group)),]

# all countries for 2011 
sub <- subset(gho, Sex=="Both sexes" & Year=="2011", select=c(Indicator, Year, Country, Age.Group, Numeric))
all.countries <- data.frame(matrix(sub$Numeric, ncol=4))
rownames(all.countries) <- ages 
colnames(all.countries) <- countries 

# US data for three dates 
sub <- subset(gho, Sex=="Both sexes" & Country=="United States of America", select=c(Indicator, Year, Country, Age.Group, Numeric))
#sub <- subset(gho, Sex=="Both sexes" & Country=="China", select=c(Indicator, Year, Country, Age.Group, Numeric))
all.dates <- data.frame(matrix(sub$Numeric, ncol=3))
rownames(all.dates) <- ages 
colnames(all.dates) <- dates 

# plot all countries together 
plot.name <- "figs/BCH_asmr_all.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
matplot(log(all.countries),
  bty="o", 
  type="l", 
  lty=c(1), 
  lwd=c(3), 
  col=colseq, 
  xlabels=ages,
  xlab="", ylab="Log of Mortality by Age", main="",
  xaxt="n",         
)
axis(1, at=c(1:length(ages)), labels=ages, tick=TRUE, hadj=0.5) 
mtext("Source: WHO, Global Health Observatory", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()

# plot all US data for three dates 
plot.name <- "figs/BCH_asmr_USA.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "magenta", "blue")
matplot(log(all.dates),
        type="l", 
        lty=c(1), 
        lwd=c(3), 
        col=colseq, 
        xlab="", ylab="Log of Mortality by Age", main="",
        xaxt="n", 
)
axis(1, at=c(1:length(ages)), labels=ages, tick=TRUE, hadj=0.5) 
mtext("Source: WHO, Global Health Observatory", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=dates, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=1, bty="n"
)
dev.off()

# OLD VERSION OF GHO DATA 
# ------------------------------------------------------------------------------
# 1. Life Table data 
# Old version of data, 1990 and 2000 only 

years <- c("1990", "2000", "2011")
#  Espen's complete countrycodes.csv is abbreviations.csv  
namesabb <- data.frame(read.csv("countrycodes.csv", na.strings="", skip = 0))
prefix <- c("http://apps.who.int/whosis/database/life_tables/download/life_")
suffix <- c(".csv")

for(y in 1:length(years)){
  print(years[y])
  
  for(i in 1:nrow(namesabb)){
    filename <- paste(prefix,namesabb[i,1],"_",years[y],suffix,sep="") 
    if(url.exists(filename)) {
      print(matrix(namesabb[i,2]))
      assign(paste("lt_",namesabb[i,2],years[y],sep=""), data.frame(read.csv(filename, na.strings="", skip = 2)))
    }
  }
  
  rm("filename","i")
  
  save(list = ls(all=TRUE), file = paste("whodata",years[y],".RData",sep=""))
}
