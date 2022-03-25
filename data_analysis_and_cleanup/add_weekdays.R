library(lubridate)
library(dplyr)

is_weekend = function(timestamp){
  lubridate::wday(timestamp, week_start = 1) >= 6
}

data <- read.csv("matrix.csv")
data$date <- as.Date(data$date)

holidays <- read.csv("schulferien.csv", sep=";")
holidays$Spring.holidays <- as.Date(holidays$Spring.holidays, "%m/%d/%y")
holidays$X <- as.Date(holidays$X, "%m/%d/%y")
holidays$Summer.holidays <- as.Date(holidays$Summer.holidays, "%m/%d/%y")
holidays$X.1 <- as.Date(holidays$X.1, "%m/%d/%y")
holidays$Fall.holidays <- as.Date(holidays$Fall.holidays, "%m/%d/%y")
holidays$X.2 <- as.Date(holidays$X.2, "%m/%d/%y")

is_between_holidays = function(timestamp) {
  nrow(holidays %>% filter(Spring.holidays <= timestamp && X >= timestamp))
}

is_between_holidays("2021-04-03")

data$day_off <- is_weekend(data$date)
