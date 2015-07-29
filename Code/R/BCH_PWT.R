# ------------------------------------------------------------------------------
#  BCH_PWT.R
#  Capital-output ratios computed from Penn World Tables.  
#  Backus, Cooley, and Henriksen, "Demography and low-frequency capital flows" 
#  Reads in Penn World Table, computes capital stocks, etc 
#  If you'd like the version that merges Barro-Lee education data, let us know 
#  PWT data:  http://pwt.econ.upenn.edu/php_site/pwt_index.php
#  List of variables:  http://pwt.econ.upenn.edu/php_site/pwt71/pwt71_form.php
#  Program written by:  Paul Backus, October 2012, later adapted by Dave  
# ------------------------------------------------------------------------------
# clear memory, set directory for output 
rm(list=ls())
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)

# 1. Functions 
# ------------------------------------------------------------------------------

# Download zipped data file and unzip it in given subdir  
download_pwt_data <- function(directory) {
	zip_url = "http://pwt.econ.upenn.edu/Downloads/pwt71/pwt71_07262012version.zip"
	download.file(zip_url, basename(zip_url), method="auto")
	unzip(basename(zip_url), exdir=directory)
}

# ------------------------------------------------------------------------------
# Import complete PWT:  read csv data file into a data frame
import_pwt_data <- function(directory) {
	read.csv(paste(directory, "pwt71_w_country_names.csv", sep="/"))
}

# ------------------------------------------------------------------------------
# Create a table of countries and their iso codes from the first two columns
# col 1 = country name, col 2 = country code (3-letter abbrev)
country_index <- function(dataset) {
	unique(cbind(as.character(dataset$country), as.character(dataset$isocode)))
}

# ------------------------------------------------------------------------------
# From here you can use 'subset' to get specifc countries and variables.
# This code gives the same subset used in Espen's code (pwt_ky_ratios_db.R)
#subset(pwt_dataframe,
#	isocode %in% c("CHN", "JPN", "IND", "USA"), # countries (rows)
#	select=c("country", "isocode", "year", "rdpl", "ki") # variables (columns)
#)

# ------------------------------------------------------------------------------
# Compute capital for one or more countries
# Algorithm adapted from Clementi's Stata code, itself based on Hall-Jones 
# depreciation is 0.06, but if you use a number in the function call it'll use that instead 
capital <- function(cdata, depreciation=0.06) {
  # remove rows with missing observations
  cdata <- cdata[!is.na(cdata$rgdpch) & !is.na(cdata$POP) & !is.na(cdata$ki),]
  
  # compute investment
  investment <- cdata$rgdpch*(cdata$ki/100)*(cdata$POP*1000)  
  
  # compute growth rates
  growth_y <- with(cdata, (log(rgdpch[10]) - log(rgdpch[1]))/10)
  growth_pop <- with(cdata, (log(POP[10]) - log(POP[1]))/10)
  
  # compute initial capital (k0)
  # Similar to Hall and Jones (QJE, 1999, fn 5) 
  # http://www.stanford.edu/~chadj/HallJonesQJE.pdf		
  # NB:  HJ use growth rate of investment, we use growth of GDP  
  ki_bar <- mean(cdata$ki[1:10])
  init_inv <- cdata$rgdpch[1]*(ki_bar/100)*(cdata$POP[1]*1000)
  init_capital <- init_inv/(exp(growth_y + growth_pop) - 1 + depreciation)
  
  # compute capital series according to the recurrence relation
  capital <- Reduce(
    function(k,t) {
      c(k, (1-depreciation)*k[t-1] + investment[t-1])
    },
    2:length(investment),
    init_capital
  )
  
  # add some metadata to allow for easy merging
  series <- cbind(capital, cdata$year)
  colnames(series) <- c("capital","year")
  
  return(series)
}

# ------------------------------------------------------------------------------
# Add capital column to pwt dataframe 
# Much faster version based on merging country blocks 
add_capital_column <- function(dataset) {
  do.call(
    rbind,
    lapply(
      split(dataset, dataset$isocode),
      function(cdata) {
        merge(cdata, capital(cdata), by = "year", all.x=TRUE)
      }
    )
  )
}

# ------------------------------------------------------------------------------
# Barro-Lee functions:  read data, interpolate, and merge with PWT 
# Two files for education of different age groups 

# ------------------------------------------------------------------------------
# Download BL data 
download_bl_data <- function(directory) {
  csv_urls = c(
    "http://www.barrolee.com/data/BL_v1.2/BL(2010)_MF2599_v1.2.csv",
    "http://www.barrolee.com/data/BL_v1.2/BL(2010)_MF1599_v1.2.csv"
  )
  for (url in csv_urls) {
    download.file(url, paste(directory, basename(url), sep="/"), method="auto")
  }
}

# ------------------------------------------------------------------------------
# Read it -- times two 
import_bl15_data <- function(directory) {
  read.csv(paste(directory, "BL(2010)_MF1599_v1.2.csv", sep="/"))
}

import_bl25_data <- function(directory) {
  read.csv(paste(directory, "BL(2010)_MF2599_v1.2.csv", sep="/"))
}

# ------------------------------------------------------------------------------
# Fill in missing values by linear interpolation
# helper function for following 
interp_nas <- function(x) {
  pos=which(!is.na(x))
  if (length(pos) < 2) {
    warning("Not enough data to interpolate.")
    return(x)
  }
  for (i in 1:(length(pos) - 1)) {
    x[pos[i]:pos[i+1]] <- approx(
      c(x[pos[i]], x[pos[i+1]]),
      n=(pos[i+1] - pos[i] + 1)
    )$y
  }
  return(x)
}

# ------------------------------------------------------------------------------
# Adds the column labeled "yr_sch" to pwtdata and fills in missing values by
# linear interpolation 
add_education_column <- function(pwtdata, edudata, colname="yr_sch") {
  # subset to year, country code, and the column we want to merge
  edudata <- subset(edudata, select = c("year", colname, "WBcode"))
  
  # merge data frames
  combined <- merge(
    pwtdata,
    edudata,
    by.x = c("year", "isocode"),
    by.y = c("year", "WBcode"),
    all.x = TRUE # include all years in the result
  )
  
  # interpolate missing values
  combined <- do.call(
    rbind,
    lapply(
      split(combined, combined$isocode),
      function(cdata) {
        #print(cdata$yr_sch)
        cdata$yr_sch <- interp_nas(cdata$yr_sch)
        cdata
      }
    )
  )
  return(combined)
}

# 2. Generate and organize data 
# ------------------------------------------------------------------------------

# get PWT data 
noquote("Downloading PWT data...")
data_dir = "backups"
download_pwt_data(data_dir)
pwt <- import_pwt_data(data_dir)

# compute capital stocks and insert into dataframe 
noquote("Computing capital stocks...")
pwt <- add_capital_column(pwt)


# 3. Create variables and csv file for class    
# ------------------------------------------------------------------------------
# drop the peripheral stuff
#col.names(pwt)
variables <- c("country", "isocode", "year", "POP", "rgdpch", "rgdpwok", "ki", "capital")
pwt <- pwt[variables]

# create variables of interest with understandable labels 
pwt$YPOP <- pwt$rgdpch
pwt$Y    <- pwt$YPOP*(pwt$POP*1000)
pwt$YL   <- pwt$rgdpwok 
pwt$LPOP <- pwt$YPOP/pwt$YL 
pwt$KY   <- pwt$capital/pwt$Y 
pwt$KL   <- pwt$KY*pwt$YL 
pwt$TFP  <- pwt$YL/pwt$KL^(1/3)
pwt$I <- pwt$rgdpch*(pwt$ki/100)*(pwt$POP*1000)

# save as rdata file for easy access later
save(pwt, file="PWT.RData")

# 4. Plot capital-output ratios 
# ------------------------------------------------------------------------------
# reload data (you can start program here)
rm(list=ls())
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
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
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,2,0.1), cex=1.25)
colseq = c("red", "black", "green3", "blue")
plot(ky_ts,
     plot.type='single',
     lty=1, 
     lwd=3, 
     col=colseq, 
     xlab="", ylab="Capital-Output Ratio", main="",
     ylim=c(0,4.5)
)
mtext("Source: Penn World Table and authors calculations", side=1, line=2.5, cex=1.0, adj=0)
legend("topleft", legend=list.countries, cex=1.0, lwd=3, col=colseq, 
       y.intersp=1, x.intersp=0.5, ncol=2, bty="n"
)
dev.off()
