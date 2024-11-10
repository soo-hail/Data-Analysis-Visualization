# Correlation

data <- data.frame(
  StudyHours = c(2, 3, 5, 4, 8, 7, 9, 6, 10, 5, 3, 4, 7, 8, 6),
  TestScore = c(55, 60, 65, 63, 85, 78, 90, 76, 92, 67, 59, 64, 80, 88, 74)
)

# Understand data
View(data)

# Calculate Correlation
c <- cor(data$StudyHours, data$TestScore)
#print(c)

# Visualize
plot(data$StudyHours, data$TestScore)
abline(lm(data$TestScore ~ data$StudyHours), col = 'red')