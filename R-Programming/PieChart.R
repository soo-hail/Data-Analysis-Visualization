# Pie-chart
setwd('C:/Users/Sohail Mohammed/OneDrive/Desktop/Data Analysis & Data Visualization')
data <- read.csv('sales.csv')

# Understand Data
View(data)

# Pie-Chart
pie(data$Sales, labels = data$Product)

perc <- round((data$Sales/sum(data$Sales)) * 100)
# print(perc)

pie(data$Sales, labels = perc)