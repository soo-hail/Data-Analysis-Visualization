data1 <- c(1, 2, 3, 4, 5, 6 ,7, 8, 9)
data2 <- c(10, 11, 12, 13, 14, 15, 16, 17, 18)

mat1 <- matrix(data1, nrow = 3, ncol = 3, byrow = TRUE)
mat2 <- matrix(data2, nrow = 3, ncol = 3, byrow = TRUE)

# Addition
print("Addition: ")
print(mat1 + mat2)

# Subtraction
print("Subtraction ")
print(mat2 - mat1)

# Multiplication
print("Multiplication: ")
r <- mat1 %*% mat2
print(r)

# Division
print('Division')
r2 <- mat2 / mat1
print(r2)