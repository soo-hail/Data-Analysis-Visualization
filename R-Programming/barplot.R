# Bar-plot(Bar-Graph)

setwd('C:/Users/Sohail Mohammed/OneDrive/Desktop/Data Analysis & Data Visualization')
data <- read.csv('monthlysales.csv')

# Understand data
View(data)

# Create Bar-Graph(Barplot)
barplot(data$Profit, names.arg = data$Month, xlab = 'Months', ylab = 'Profit', main = 'Monthly Sales', col='blue', border
        ='black')

#NOTE: 
# names.arg: Lables each bar. 