# ------------------------------------------------------------------------------
#  BCH_LMF.R  
#  NFA data plots for demography paper 
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Grabs Lane and Milesi-Ferretti database on net foreign assets, described in 
#  "The External Wealth of Nations," JIE, 2007 
#  See paper at:  http://www.imf.org/external/pubs/cat/longres.aspx?sk=18942.0
#  Data is large flat file, countries stacked up, 1970-2007 or subset 
#  Written by Espen Henriksen, September 2010 
#  Adapted by Dave Backus 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)
# subdir for backups 
backup <- "backups"

# load packages
library("gdata")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Download data

# download data and save in "fname" (dated to avoid overwriting old data)
# url = internet source of data, destfile = filename for local version 
fname = paste("LMF99_",Sys.Date(), ".zip" ,sep="")    
flocation <- paste("backups/", fname, sep="")
url <- "http://www.imf.org/external/pubs/ft/wp/2006/data/update/wp0669.zip"
download.file(url=url, destfile=flocation, method="auto")

# input data sheet (first one reads data, second one reads headers for variable names) 
lmf.data     <- read.xls(unzip(zipfile=flocation,files="EWN II update for web (August 2009).xls",list=FALSE),header=TRUE,skip=1,sheet=4)
series.names <- read.xls(unzip(zipfile=flocation,files="EWN II update for web (August 2009).xls",list=FALSE),header=FALSE,skip=0,sheet=4,nrows=1)

series.names.old <- series.names
print(t(series.names.old))

# why?  seems redundant 
series.names[1] <- "Country"
series.names[2] <- "IFS.code"
series.names[3] <- "Year"
series.names[4] <- "Portfolio equity assets"
series.names[5] <- "Portfolio equity liabilities"
series.names[6] <- "FDI assets"
series.names[7] <- "FDI liabilities"
series.names[8] <- "Debt assets (portfolio debt plus other investment)"
series.names[9] <- "Debt liabilities (portfolio debt plus other investment)"
series.names[10] <- "Financial derivatives assets"
series.names[11] <- "Financial derivatives liabilities"
series.names[12] <- "FX Reserves minus gold"
series.names[13] <- "Total assets"
series.names[14] <- "Total liabilities"
series.names[15] <- "NFA"
series.names[16] <- "Net IIP as officially reported"
series.names[17] <- "NFA (alternative FDI valuation)"
series.names[18] <- "GDP"
series.names[19] <- "Portfolio debt assets"
series.names[20] <- "Portfolio debt liabilities"
series.names[21] <- "Other investment assets"
series.names[22] <- "Other investment liabilities"
series.names[23] <- "FDI assets (other valuation)"
series.names[24] <- "FDI liabilities (other valuation)"
series.names[25] <- "Exchange rate vis-a-vis US dollar (period avg)"
series.names[26] <- "Exchange rate vis-a-vis US dollar (end of period)"

# assign var names to data, [[2]] means names apply to columns (see also colnames)
dimnames(lmf.data)[[2]] <- series.names  

# save for faster access (ie, start with load)  
save(lmf.data,file="LMF.Rdata")

rm(list=ls())
load("LMF.Rdata")

# ------------------------------------------------------------------------------
# 2. Extract subset 

# ?? could probably streamline this 
# extract a subset of columns (variables) 
lmf.subset <- data.frame(Country = lmf.data$Country,
                          IFS     = lmf.data$IFS.code,
                          Year    = lmf.data$Year,
                          NFA     = as.numeric(gsub(",","",lmf.data$NFA)),
                          GDP     = as.numeric(gsub(",","",lmf.data$GDP)),
                          NFAGDP  = as.numeric(gsub(",","",lmf.data$NFA))
              )

lmf.subset$NFAGDP <- lmf.subset$NFA/lmf.subset$GDP

# extract a subsect of countries (rows) 
countries <- c("China,P.R.: Mainland", "Germany", "Japan", "United States")
#c("Australia","Canada","China,P.R.: Mainland", #"Germany","France","Italy","Japan","Norway","United Kingdom","United States")

lmf.oecd<- NULL
for(i in 1:length(countries)){
  lmf.oecd <- cbind(lmf.oecd,lmf.subset[lmf.subset$Country == countries[i],]$NFAGDP)
}

countries <- c("CHN", "DEU", "JPN", "USA")

dimnames(lmf.oecd)[[2]] <- countries
lmf.oecd <- ts(lmf.oecd,start=1970,frequency=1)
lmf.oecd <- window(lmf.oecd, start=1980)

# ------------------------------------------------------------------------------
# 3. Plot NFA/GDP for selected countries 

plot.name <- "figs/BCH_nfa.pdf"
pdf(file=plot.name, width=8, height=6)
colseq = c("red", "black", "green3", "blue")
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)

plot(lmf.oecd,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Net Foreign Assets (Ratio to GDP)", main="",
)  
abline(h=0, lty=1)  
legend("topleft", legend=countries, cex=1, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
mtext("Source:  Lane and Milesi-Ferretti", side=1, line=2.5, cex=1, adj=0)
dev.off()

