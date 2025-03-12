import numpy as np
import pandas as pd

# Part 1 - Numpy
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
# print(iris_2d)

# 1.⁠ ⁠Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
print()
print("Part 1 Q1")
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print("Vertical Stack:\n", vertical_stack)
print("Horizontal Stack:\n", horizontal_stack)

# 2.⁠ ⁠Find common elements between A and B. [Hint : Intersection of two sets]
print()
print("Part 1 Q2")
common_elements = np.intersect1d(A, B)
print("Common Elements:", common_elements)

# 3.⁠ ⁠Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
print()
print("Part 1 Q3")
A = np.array([2, 4, 6, 8, 10, 12])
filtered_A = A[np.where((A >= 5) & (A <= 10))]
print("Filtered A:", filtered_A)

# 4.⁠ ⁠Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
print()
print("Part 1 Q4")
filtered_iris = iris_2d[np.where((iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0))]
print("Filtered Iris rows:\n", filtered_iris)

# # Part 2 - Pandas
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# print(df)

# 1.⁠ ⁠From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print()
print("Part 2 Q1")
filtered_df = df.loc[0::20, ['Manufacturer', 'Model', 'Type']]
print("Every 20th row):\n", filtered_df)

# 2.⁠ ⁠Replace missing values in Min.Price and Max.Price columns with their respective mean.
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print()
print("Part 2 Q2")
print("Missing values before filling:")
print(df[['Min.Price', 'Max.Price']][df[['Min.Price', 'Max.Price']].isna().any(axis=1)])
df.fillna({'Min.Price': df['Min.Price'].mean()}, inplace=True)
df.fillna({'Max.Price': df['Max.Price'].mean()}, inplace=True)
print("Missing values after filling:")
print(df[['Min.Price', 'Max.Price']][df[['Min.Price', 'Max.Price']].isna().any(axis=1)])

# # 3.⁠ ⁠How to get the rows of a dataframe with row sum > 100?
# # df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print()
print("Part 2 Q3")
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df_random)
filtered_rows = df_random[df_random.sum(axis=1) > 100]
print("Rows with sum > 100:\n", filtered_rows)