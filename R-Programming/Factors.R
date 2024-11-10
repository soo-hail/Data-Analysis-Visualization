# Factors: are used to store categorical data.

gender <- c('Male', 'Female', 'Male', 'Female', 'Male', 'Female')

gender_fac <- factor(gender, levels = c('Female', 'Male'))
print(gender_fac)