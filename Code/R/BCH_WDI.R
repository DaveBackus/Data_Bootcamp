# ------------------------------------------------------------------------------
#  BCH_WDI.R  
#  WDI data plots for demography paper 
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Grabs World Bank's WDI ("World Dev Indicators") and GDF ("Global Dev Fin") 
#  Data locations:  
#    Overview:  http://data.worldbank.org/
#    WDI:  http://data.worldbank.org/data-catalog/world-development-indicators
#    Zipped csv:  http://databank.worldbank.org/data/download/WDI_csv.zip
#  Data is large flat file, one (variable,country) per row, ordered by
#  variable (first) and country (second)
#  Each row looks like this:  
#    Column A:  Country.Name 
#    Column B:  Country.Code
#    Column C:  Indicator.Name  
#    Column D:  Indicator.Code 
#    Columns E-whatever:  Year starting 1960  
#  Variables of interest 
#    BN.CAB.XOKA.GD.ZS  current account (% of GDP) 
#    NE.GDI.FTOT.ZS     gross domestic investment (% of GDP) 
#    NY.GDS.TOTL.ZS     gross domestic saving (% of GDP) 
#  FAIL!!!  Current account data start in 2005! 
#  Adapted by Dave Backus from code written by Espen and Paul 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/JIE_2013"
setwd(dir)

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# 1. Get data 
# no one-step method so far --- can't stick the url in the unzip function 

# get zip file and save it 
zip.url <- "http://databank.worldbank.org/data/download/WDI_csv.zip"
zip.name = paste("WDI_",Sys.Date(),".zip",sep="")  
download.file(url=zip.url, destfile=zip.name, method="auto")

# now read it 
wdi <- read.csv(unzip(zipfile=zip.name, files="WDI_Data.csv", list=FALSE), header=TRUE, sep=",")

# check contents 
names(wdi)
#head(wdi) 
frameClasses(wdi) 

# save for faster access (ie, start below in future)  
save(list=ls(all=TRUE), file="WDI.RData")

# 2. Data selection and plot 
# ** start here  
noquote("Clear workspace and load data...")
rm(list=ls())
load("WDI.RData")
setwd(dir)

# select countries and variables 
list.countries <- c("CHN", "DEU", "JPN", "USA")
list.variables <- c("BN.CAB.XOKA.GD.ZS") #, "NE.GDI.FTOT.ZS", "NY.GDS.TOTL.ZS")

wdi_sub <- wdi[wdi$Indicator.Code %in% list.variables,]
wdi_sub <- wdi[wdi$Country.Code %in% list.countries & wdi$Indicator.Code %in% list.variables,]

# convert to ts 
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,5:ncol(dataset)-1]),  # transpose: ts expects data in columns
    # note that it treats the row names as a column here
    start=1960, 
    frequency=1
  )
  # label with country names 
  colnames(ts_data) <- as.character(dataset$Country.Code)
  return(ts_data)
}

ts <- convert_to_ts(wdi_sub)
ts <- window(ts, start=1970,end=2012)

df <- data.frame(ts) 

head(wdi_ts)

# plot all countries together 
par(fin=c(8,6))
colseq = c("red", "black", "green3", "blue")
plot(wdi_ts,
     plot.type='single',
     mgp=c(2.75,1,0),
     mai=c(1,1,1,1),
     lwd=4, 
     xlab="", ylab="Current Account (percent of GDP)", main="",
     col=colseq, 
)
abline(a=0, b=0)  
mtext("Source: World Bank, World Development Indicators, May 2013", side=1, line=2.5, cex=.6, adj=0)
legend("topleft", legend=colnames(weo_ts), cex=0.90, lwd=4, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.print(device=pdf, file="BCH_CA_WDI.pdf", width=8, height=6)

