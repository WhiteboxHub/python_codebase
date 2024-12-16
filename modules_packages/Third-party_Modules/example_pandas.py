import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
# Output:
#       Name  Age         City
# 0    Alice   24     New York
# 1      Bob   27  Los Angeles
# 2  Charlie   22      Chicago

# Filter data
young_people = df[df["Age"] < 25]
print(young_people)
# Output:
#       Name  Age     City
# 0    Alice   24  New York
# 2  Charlie   22   Chicago
