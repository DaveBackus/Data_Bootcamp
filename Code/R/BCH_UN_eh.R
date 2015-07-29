# ------------------------------------------------------------------------------
#  BCH_UN_eh.R  
#  UN demographic data of various sorts:  population, fertility, dependency...   
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Source:  UN population projections, http://esa.un.org/unpd/wpp/index.htm
#  Specific url's below.  
#  Adapted by Dave Backus from code written by Espen and Paul 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir <- "C:/Users/dbackus/Documents/Papers/BCH/data/test"
dir <- ""
setwd(dir)
# subdir for backups 
backup <- "backups"

# load packages
library("gdata")

print("test")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Demographic data 

# gdata version, read straight from url, save copy for future reference 
# old = data through 2010, new = projections through 2100 

# (a) Population 

url_old <- "http://esa.un.org/unpd/wpp/Excel-Data/DB04_Population_ByAgeSex_Annual/WPP2010_DB4_F1A_POPULATION_BY_AGE_BOTH_SEXES_ANNUAL_1950-2010.XLS"
pop_old <- read.xls(url_old, sheet=1, verbose=T, skip=10, header=T, na.strings=c("\u2026"), encoding="Latin1")
url_new <- "http://esa.un.org/unpd/wpp/Excel-Data/DB04_Population_ByAgeSex_Annual/WPP2010_DB4_F1B_POPULATION_BY_AGE_BOTH_SEXES_ANNUAL_2011-2100.XLS"
pop_new <- read.xls(url_new, sheet=1, verbose=T, skip=10, header=T, na.strings=c("\u2026"), encoding="Latin1")

# several formatting problems on mac/unix:
#   both space as thousand separator and the "levels" problem.
#   the following function in combination with sapply provides a solution
tmpfn <- function(x) {as.numeric(gsub(" ","",as.character(x)))}

# check platform -- if sysname is "Darwin", platform is mac
tmp <- Sys.info()["sysname"]
if(tmp[[1]]=="Darwin"){
  pop <- {rbind(cbind(pop_old[1:nrow(pop_old),1:6],sapply(pop_old[1:nrow(pop_old),7:ncol(pop_old)],tmpfn)),
                cbind(pop_new[1:nrow(pop_new),1:6],sapply(pop_new[1:nrow(pop_new),7:ncol(pop_new)],tmpfn)))}
} else {
  pop <- rbind(pop_old, pop_new)
}
frameClasses(pop)
rm(pop_old, pop_new,tmp)


# save copies
download.file(url_old, paste(backup,paste("UN_pop_old_",Sys.Date(),".xls",sep=""),sep="/"),method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb")
download.file(url_new, paste(backup,paste("UN_pop_new_",Sys.Date(),".xls",sep=""),sep="/"),method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb")
rm(tmp)

# (b) Old-age dependency:  65+ over 20-64 
# sheet 1 = past, sheet 2 = projections (medium)

url_oad <- "http://esa.un.org/unpd/wpp/Excel-Data/DB02_Stock_Indicators/WPP2010_DB2_F05_3B_OLD_AGE_DEPENDENCY_RATIO_2064.XLS"
oad_old <- read.xls(url_oad, sheet=1, skip=10, header=TRUE)  
oad_new <- read.xls(url_oad, sheet=2, skip=10, header=TRUE)  

# save copy 
download.file(url_oad, paste(backup,paste("UN_oad_",Sys.Date(),".xls",sep=""),sep="/"), 
              method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb") 

# drop extra columns 
oad_old <- oad_old[-c(1,4)]
oad_new <- oad_new[-c(1,2,3,4)]

oad <- merge(oad_old, oad_new, by="Country.code")
frameClasses(oad)
rm(oad_old, oad_new)

# (c) Age=specific fertility rates 
# sheet 1 = past, sheet 2 = projections (medium)

url_asfr <- "http://esa.un.org/unpd/wpp/Excel-Data/DB06_Fertility_IndicatorsByAge/WPP2010_DB6_F2_AGE_SPECIFIC_FERTILITY.XLS"
asfr_old <- read.xls(url_asfr, sheet=1, skip=10, header=TRUE)  
asfr_new <- read.xls(url_asfr, sheet=2, skip=10, header=TRUE)  

# save copy 
download.file(url_asfr, paste(backup,paste("UN_asfr_",Sys.Date(),".xls",sep=""),sep="/"), 
              method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb") 

asfr <- rbind(asfr_old, asfr_new)  
frameClasses(asfr) 
rm(asfr_old, asfr_new)  

# (d) Life expectancy  
# sheet 1 = past, sheet 2 = projections (medium)

url_le <- "http://esa.un.org/unpd/wpp/Excel-Data/DB01_Period_Indicators/WPP2010_DB1_F05_1_LIFE_EXPECTANCY_0_BOTH_SEXES.XLS"
le_old <- read.xls(url_le, sheet=1, skip=10, header=TRUE)  
le_new <- read.xls(url_le, sheet=2, skip=10, header=TRUE)  

# save copy 
download.file(url_le, paste(backup,paste("UN_le_",Sys.Date(),".xls",sep=""),sep="/"), 
              method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb") 

# drop extra columns 
le_old <- le_old[-c(1,4)]
le_new <- le_new[-c(1,2,3,4)]

le <- merge(le_old, le_new, by="Country.code")
frameClasses(le) 
rm(le_old, le_new)  

# (e) Age=specific mortality rates 
# ?? note sure what this spreadsheet contains...  

url_asmr <- "http://esa.un.org/unpd/wpp/Model-Life-Tables/data/MLT_UN2010-130_1y.xls"

# (f) Save in RData file for faster access (ie, start below in future)  

save(list=ls(all=TRUE), file="UN.RData")

# ------------------------------------------------------------------------------
# 2. Data selection and plot 

# ** start here  
noquote("Clear workspace and load data...")
rm(list=ls())
load("UN.RData")
setwd(dir)

# country codes 
# CHN = 156, DEU = 276, JPN = 392, USA = 840, Western Europe = 926 
# http://cran.r-project.org/web/packages/countrycode/countrycode.pdf

# select countries 
list.countries <- c("CHN", "DEU", "JPN", "USA")
list.uncodes   <- c("156", "276", "392", "840")

# (a) Life expectancy 

# this orders the countries by code 
le_sub <- le[le$Country.code %in% list.uncodes,]

# convert to ts 
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,4:ncol(dataset)]), 
    # note column one is the row names 
    start=1952.5, 
    frequency=0.2
  )
  # label with country names 
  colnames(ts_data) <- list.countries
  return(ts_data)
}

le_ts <- convert_to_ts(le_sub)

# plot all countries together 
colseq = c("red", "black", "green3", "blue")
par(fin=c(8,6), mgp=c(2.75,1,0), mar=c(4,4,3,0)) 
plot(le_ts,
     plot.type='single',
     lty=1, #c(1,1,1,5),  
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Life Expectancy at Birth", main="",
     xlim=c(1950,2100),
)
abline(v=2010) 
text(1990, 47, "Estimates")
text(2030, 47, "Projections")
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=.6, adj=0)
legend("topleft", legend=colnames(le_ts), cex=0.90, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.print(device=pdf, file="BCH_le.pdf", width=8, height=6)

# (b) Old-age dependency 

oad_sub <- oad[oad$Country.code %in% list.uncodes,]

# convert to ts 
rm("convert_to_ts")
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,4:ncol(dataset)]),  
    start=1950, 
    frequency=0.2
  )
  # label with country names 
  colnames(ts_data) <- list.countries
  return(ts_data)
}

oad_ts <- convert_to_ts(oad_sub)

# plot all countries together 
colseq = c("red", "black", "green3", "blue")
par(fin=c(8,6), mgp=c(2.75,1,0), mar=c(4,4,3,0)) 
plot(oad_ts,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Old-Age Dependency (65+ over 20-64)", main="",
     xlim=c(1950,2100),
)
abline(v=2010) 
#text(1995, 47, "Estimates")
#text(2030, 47, "Projections")
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=.6, adj=0)
legend("topleft", legend=colnames(le_ts), cex=0.90, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.print(device=pdf, file="BCH_oad.pdf", width=8, height=6)

# (c) fertility by age  

asfr_sub <- asfr[asfr$Country.code %in% list.uncodes,] # & asfr$Period == "2005-2010",]
asfr_sub <- asfr_sub[order(asfr_sub$Country.code),]

# convert to ts 
rm("convert_to_ts")
convert_to_ts <- function(dataset) {
  ts_data <- ts(
    t(dataset[,7:ncol(dataset)]),  
    start=17.5, 
    frequency=0.2
  )
  # label with country names 
  colnames(ts_data) <- list.countries
  return(ts_data)
}

asfr_ts <- convert_to_ts(asfr_sub)

# plot all countries together 
colseq = c("red", "black", "green3", "blue")
par(fin=c(8,6), mgp=c(2.75,1,0), mar=c(4,4,3,0)) 
plot(asfr_ts,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Fertility by Age", main="",
)
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=.6, adj=0)
legend("topright", legend=colnames(le_ts), cex=0.90, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.print(device=pdf, file="BCH_asfr.pdf", width=8, height=6)
