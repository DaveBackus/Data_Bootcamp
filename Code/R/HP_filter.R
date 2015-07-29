#  HP_filter.R 
#  Draws NX/Y and HP-filtered version for slides 
#  Data from FRED, input with functions written by Paul Backus 
#  Written by:  Dave Backus 
# ------------------------------------------------------------------------------
# 0. Preliminaries 

# clear workspace  
rm(list=ls()) 

# set working directory for output 
dir = "C:/Users/dbackus/Documents/Papers/BCH/data/ISOM_2013"
setwd(dir)

library("XML")    # for FRED input 
library("xts")    # time series package (also used for FRED)

# 1. FRED functions from Paul 
# ------------------------------------------------------------------------------

# FRED functions from Paul 
callFredAPI <- function(call_string, params) {
  api_key <- "055ba538c874e5974ee22d786f27fdda"  
  url <- paste(
    "http://api.stlouisfed.org/fred/", # base url
    call_string, # subdirectory--documented on fred website
    "?", # separator between web address and parameter list
    paste(
      paste("api_key=", api_key, sep=""),
      paste(
        sapply(
          names(params),
          function(pname) {
            paste(pname, "=", params[[pname]], sep="")
          }
        ),
        collapse="&" # use collapse instead of sep to flatten list
      ),
      sep="&"
    ),
    sep=""
  )
  return(xmlTreeParse(url, useInternal=TRUE))
}

# Helper function to extract specific attributes from FRED's XML
collectAttrs <- function(doc, tag, attr) {
  sapply(
    getNodeSet(doc, paste("//", tag)),
    function(el) { xmlGetAttr(el, attr) }
  )
}

# Downloads the specified series and returns it as a vector, with the dates
# of each observation stored in the vector's names attribute
getFredData <- function(series_id) {
  doc <- callFredAPI("series/observations", list(series_id=series_id))
  dataseries <- as.numeric(collectAttrs(doc, "observation", "value"))
  names(dataseries) <- collectAttrs(doc, "observation", "date")
  return(dataseries)
}

# Downloads the metadata of a FRED series and returns a particular attribute
# A list of available attributes can be found at
#   http://api.stlouisfed.org/docs/fred/series.html
getFredMetadata <- function(series_id, attribute) {
  doc <- callFredAPI("series", list(series_id=series_id))
  attrs <- collectAttrs(doc, "series", attribute)
  return(attrs)
}

# Returns a multivariate time series of the variables specified in series_ids
getFredTable <- function(series_ids) {
  data <- do.call(
    merge,
    lapply(
      series_ids, 
      function(series) { as.xts(getFredData(series)) }
    )
  )
  colnames(data) <- series_ids
  return(data)
}

#  2. Data input 
# ------------------------------------------------------------------------------
# qrtly data:  net exports 
fred.sym <- c("NETEXP", "GDP") #, "EXPGS", "EXPGSC1", "IMPGS", "IMPGSC1")
fred <- getFredTable(fred.sym)

# kill off some obs
fred <- fred["1960-01-01/"]  # slash means go to end: "n1/n2", "/n2", "n1/"
fred$nxy <- fred$NETEXP/fred$GDP

#test <- data.frame(fred.q)

#  3. Filtering  
# ------------------------------------------------------------------------------
# From Farnsworth, "Econometrics in R," page 25
# http://cran.r-project.org/doc/contrib/Farnsworth-EconometricsInR.pdf
hpfilter <- function(x,lambda=1600){
  eye <- diag(length(x))
  result <- solve(eye+lambda*crossprod(diff(eye,lag=1,d=2)),x)
  return(result)
}

# quarterly data:  net exports 
fred$nxy.hp  <- hpfilter(fred$nxy) 
fred$nxy.dev <- fred$nxy - fred$nxy.hp 

plot.name <- "figs/BCH_hp_nxy.pdf"
pdf(file=plot.name, width=8, height=6)
par(fin=c(8,6), mgp=c(2.25,1,0), mar=c(4,3.6,3,0.5), cex=1.25)

plot(fred$nxy,
     auto.grid="FALSE", minor.ticks="FALSE", major.format="%Y", 
     main="", ylab="Ratio of Net Exports to GDP", 
     mar=c(2,3,2,2), mgp=c(2.5,1,0), col="blue") # can't make lwd=2??
lines(fred$nxy, col="blue", lwd=2)
lines(fred$nxy.hp, col="magenta", lwd=2)
abline(h=0, lwd=0.25)
dev.off()

#dev.copy2eps(device=postscript, file="NXY.eps", width=8, height=6)



