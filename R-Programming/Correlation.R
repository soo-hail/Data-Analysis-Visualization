# Co-relation
study_hours <- c(5, 7, 3, 8, 6, 9)
exam_scores <- c(80, 85, 60, 90, 75, 95)

c <- round(cor(study_hours, exam_scores), 2)

# Create Plot
plot(study_hours, exam_scores, main = 'Study-hours v/s Exam-scores')
abline(lm(exam_scores ~ study_hours), col='red')
text(4, 90, paste('Correlation: ', c))
