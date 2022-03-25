install.packages("dplyr")
library(dplyr)

data <- read.csv("reservation_data_2019-2021_incl_capacity.csv")

data$line <- as.factor(data$line)

d <- data[ ,!names(data) %in% c("res_delta_ist","res_delta_soll", "res_delta_valid")]

summary(d)
head(data, 3)

train_capacity_avg <- data %>%
  group_by(line) %>%
  summarise(capacity = mean(capacity, na.rm=T))

summary(train_capacity_avg)

grouped <- data %>% 
  group_by(train_nr, date) %>% 
  summarise(reserved = sum(reserved), capacity = mean(capacity))

test <- data %>%
  group_by(bp_from, bp_to) %>%
  summarise(reserved = )

summary(grouped)


wrong <- grouped[[grouped$reserved > grouped$capacity]]




weather <- read.csv("weather.csv", sep=";")
summary(weather)

weather$leisure_biking.idx <- as.numeric(gsub(",", ".", weather$leisure_biking.idx))

summary(weather)


weather_grouped <- weather %>%
  group_by(station_id) %>%
  summarise(m = mean(leisure_biking.idx, na.rm=T))



summary(weather_grouped)
