"""
Convert to Python 
http://www.r-bloggers.com/led-is-my-new-hello-world-r-time/

R code 
line<-c(1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3)
index<-c(0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9)
map<-c("  _ ","| | ","|_| ","  ","| ","| ","  _ "," _| ","|_  ",
       " _","_| ","_| ","    ","|_| ","  | ","  _ ","|_  "," _| ",
       "  _ ","|_  ","|_| "," _  "," |  "," |  ","  _ ","|_| ","|_| ",
       "  _ ","|_| "," _| ")

Lines<-cbind(line,index,map)
DF_Lines<-data.frame(Lines,stringsAsFactors=F)

line1<-""
line2<-""
line3<-""

p_number<-readline("Enter a number?: ")
l_number<-strsplit(p_number,"")
for(i in 1:nchar(p_number)){
  num_map<-DF_Lines[DF_Lines$index == as.numeric(l_number[[1]][i]),]
  line1<-paste(line1,num_map$map[1])
  line2<-paste(line2,num_map$map[2])
  line3<-paste(line3,num_map$map[3])
}
lines = paste(line1,"n",line2,"n",line3,"n")
cat(lines)
"""

