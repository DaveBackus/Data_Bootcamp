# ------------------------------------------------------------------------------
#  BCH_WEO.R  
#  WEO data plots for demography paper 
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Data from IMF's WEO database 
#  Data is large flat file, one (variable,country) per row 
#  Each row looks like this:  
#    Column A:  WEO Country Code (3 digit number) 
#    Column B:  ISO (3 letter country abbrev)
#    Column C:  WEO Subject Code (variable code) 
#    Column D:  Country (full name) 
#    Column E:  Subject descriptor (variable description) 
#    Columns AN-whatever:  data by year, starting 1980 (current version to 2018)   
#  Variables of interest 
#    BCA_NGDPD: CA as ratio to GDP
#  Additional information:  
#    http://www.imf.org/external/data.htm#data 
#    http://www.imf.org/external/ns/cs.aspx?id=28
#  Adapted by Dave Backus from code written by Espen and Paul 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)
backup <- "backups"

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# 1. Get data 

# one-step version 
# Comment:  file has xls suffix, but is tab delimited 
url = "http://www.imf.org/external/pubs/ft/weo/2013/01/weodata/WEOApr2013all.xls" 
weo <- read.delim(url, header=TRUE, fill=TRUE)

# Alt version:  download, then read 
file.name = paste("WEO_",Sys.Date(),".xls",sep="")
download.file(url, paste(backup,file.name,sep="/"), mode="wb")
#weo <- read.delim(file.name, header=TRUE, fill=TRUE)

# check contents 
names(weo)
#head(weo) 
frameClasses(weo) 

# save for faster access (ie, start below in future)  
save(list=ls(all=TRUE), file="WEOApr13.RData")

# 2. Data selection and plot 
# ** start here  
noquote("Clear workspace and load data...")
rm(list=ls())
load("WEOApr13.RData")
#setwd(dir)

# select countries and variables 
list.countries <- c("CHN", "DEU", "JPN", "USA")
list.variables <- c("BCA_NGDPD")

weo_sub <- weo[weo$ISO %in% list.countries & weo$WEO.Subject.Code %in% list.variables,]

# convert to ts 
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,11:ncol(dataset)-1]),  # transpose: ts expects data in columns
    # note clumn one is the row names 
    start=1980, 
    frequency=1
  )
  # label with country names 
  colnames(ts_data) <- as.character(dataset$ISO)
  return(ts_data)
}

weo_ts <- convert_to_ts(weo_sub)
weo_ts <- window(weo_ts, start=1980, end=2013)

# plot all countries together 
plot.name <- "figs/BCH_ca.pdf"
pdf(file=plot.name, width=8, height=6)
colseq = c("red", "black", "green3", "blue")
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
plot(weo_ts,
     plot.type='single',
#     new=TRUE, 
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Current Account (Percent of GDP)", main="",
)
abline(a=0, b=0)  
mtext("Source: IMF, World Economic Outlook, April 2013", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=list.countries, cex=1, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
#dev.print(device=pdf, file="BCH_CA.pdf", width=8, height=6)

