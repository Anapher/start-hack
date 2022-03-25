folder = "./datas/1"

install.packages("rjson")

library(lubridate)
library(rjson)
library(purrr)

data <- read.csv(paste(folder, "train_congestion.csv", sep="/"))
stopsData <- fromJSON(file = paste(folder, "map.json", sep="/"))

stops <- map_chr(stopsData, function(x) {x[2]})

is_weekday = function(timestamp){
  lubridate::wday(timestamp, week_start = 1) < 6
}

fix_decimals = function(s) {
  as.numeric(gsub(",", ".", s))
}

data$weekend <- is_weekday(data$date)

weather <- read.csv("weather.csv", sep=";")
weather$leisure_biking.idx <- fix_decimals(weather$leisure_biking.idx)
weather$t_2m.C <- fix_decimals(weather$t_2m.C)
weather$snow_depth.cm <- fix_decimals(weather$snow_depth.cm)
weather$precip_24h.mm <- fix_decimals(weather$precip_24h.mm)
weather$date <- gsub("T.*$", "", weather$validdate)

summary(weather)

merged <- merge(x = data, y = weather, by = "date")

for(i in 1:length(stops)) {
  fm <- as.formula(paste(stops[i], "~", "weekend + leisure_biking.idx"))
  model <- lm(fm, data = merged)
  
  model
}

