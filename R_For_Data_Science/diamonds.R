library(tidyverse)

ggplot(diamonds, aes(carat, price)) + 
  geom_hex()
ggsave("R_For_Data_Science/diamonds.pdf")

write_csv(diamonds, "R_For_Data_Science/diamonds.csv")

# source('E:/03-Download/Github/xiangxing98.github.io/R_For_Data_Science/diamonds.R')