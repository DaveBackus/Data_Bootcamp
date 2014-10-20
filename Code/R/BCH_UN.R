# ------------------------------------------------------------------------------
#  BCH_UN.R  
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
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)
# subdir for backups 
backup <- "backups"

# load packages
library("gdata")

# cool function from Espen to check column classes (watch for dreaded factors)
frameClasses <- function(x) {unlist(lapply(unclass(x),class))}

# ------------------------------------------------------------------------------
# 1. Demographic data 

# gdata version, read straight from url, save copy for future reference 
# old = data through 2010, new = projections through 2100 

# (a) Population 

url_old <- "http://esa.un.org/unpd/wpp/Excel-Data/DB04_Population_ByAgeSex_Annual/WPP2010_DB4_F1A_POPULATION_BY_AGE_BOTH_SEXES_ANNUAL_1950-2010.XLS"
pop_old <- read.xls(url_old, sheet=1, skip=10, header=TRUE)  # 10 works, not sure why 

url_new <- "http://esa.un.org/unpd/wpp/Excel-Data/DB04_Population_ByAgeSex_Annual/WPP2010_DB4_F1B_POPULATION_BY_AGE_BOTH_SEXES_ANNUAL_2011-2100.XLS"
pop_new <- read.xls(url_new, sheet=1, skip=10, header=TRUE) 

pop <- rbind(pop_old, pop_new)
frameClasses(pop)
rm(pop_old, pop_new)

# save copies 
download.file(url_old, paste(backup,paste("UN_pop_old_",Sys.Date(),".xls",sep=""),sep="/"), 
              method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb") 
download.file(url_new, paste(backup,paste("UN_pop_new_",Sys.Date(),".xls",sep=""),sep="/"), 
              method="auto", quiet=FALSE, cacheOK=FALSE, mode="wb") 

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

# ** start here after setting directory 
noquote("Clear workspace and load data...")
rm(list=ls())
load("UN.RData")

# country codes 
# CHN = 156, DEU = 276, JPN = 392, USA = 840, Western Europe = 926 
# http://cran.r-project.org/web/packages/countrycode/countrycode.pdf

# select countries 
#list.countries <- c("CHN", "DEU", "JPN", "USA")
list.uncodes   <- c("156", "276", "392", "840")
library("countrycode")
list.countries <- countrycode(list.uncodes, "un", "iso3c", warn=TRUE)

# set graphics parameters 
#par.old  <- par()
#par.mine <- par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,4.2,3,0.2), cex=1) 

# ------------------------------------------------------------------------------
# (a) Life expectancy 

# order the countries by code 
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
plot.name <- "figs/BCH_le.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
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
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=list.countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
#dev.print(device=pdf, file=plot.name, width=8, height=6)

# ------------------------------------------------------------------------------
(b) Old-age dependency 

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
plot.name <- "figs/BCH_oad.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25) 
colseq = c("red", "black", "green3", "blue")
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
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=list.countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
#dev.print(device=pdf, file=plot.name, width=8, height=6)

# ------------------------------------------------------------------------------
(c) age-specific fertility   

asfr_sub <- asfr[asfr$Country.code %in% list.uncodes& asfr$Period == "2005-2010",]
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

# compute totals 
asfr_total <- colSums(asfr_ts)
noquote("Total fertility by country")
print(asfr_total)

# plot all countries together 
plot.name <- "figs/BCH_asfr.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
plot(asfr_ts,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Births per Thousand Women", main="",
)
mtext("Source: UN, World Population Prospects, 2010 revision", side=1, line=2.5, cex=1.0, adj=0)
legend("topright", legend=list.countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
#dev.print(device=pdf, file=plot.name, width=8, height=6)


# ------------------------------------------------------------------------------
(d) age distribution 

frameClasses(pop)
list.years <- c(1980, 2010, 2040)

pop_sub <- pop[pop$Country.code == 156 & pop$Reference %in% list.years,]

# plot 
TAB <- cohorts.country
mp <- barplot(as.matrix(TAB),beside=TRUE,col=rainbow(nyears),axisnames=FALSE, args.legend=list(x="topright"))
legend("topright", legend=c("1950","1980","2010","2040"), fill=rainbow(nyears), bty="n")

# country heading 
mtext(ccode[j,2], side=3, adj=0, line=0.5, cex=1.25) 

# age labels 
colMeansmp <- colMeans(mp)
for(i in 1 : 11){
  mtext(1, at=colMeansmp[(i-1)*2+1], text=x[(i-1)*2+1], line=0.20, cex=0.8)
}
for(i in 1 : 10){
  mtext(1, at=colMeansmp[i*2], text=x[i*2], line=1.00, cex=0.8)
}
mtext("Source:  United Nations, Population Estimates and Projections", side=1, line=2.5, cex=.6, adj=0)
