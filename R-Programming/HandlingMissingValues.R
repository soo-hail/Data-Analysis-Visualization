# Handling Missing Values.

vec <- c(51, 24, 53, 60, NA, 23)
# Create Data-frame.
df <- as.data.frame(matrix(vec, ncol = 2))

# Handle Missing Values.
is.na(df)

new_df <- na.omit(df) # Removes row that contains 'NA'
print(new_df)

# Replace Missing Values with Mean/Median.
