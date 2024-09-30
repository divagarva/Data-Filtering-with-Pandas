# Import necessary libraries
import pandas as pd

# Sample data (You can replace this with your dataset)
data = {
    'Name': ['John Doe', 'Anna Smith', 'Peter Parker', 'Sam Taylor', 'Lisa Ray'],
    'Age': [28, 22, 35, 45, 30],
    'Country': ['USA', 'Canada', 'USA', 'UK', 'Canada'],
    'Salary': [50000, 40000, 60000, 55000, 45000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 1: Filter based on a single condition (e.g., Age > 30)
age_filter = df[df['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(age_filter)

# Step 2: Filter based on multiple conditions (e.g., Age > 30 and Country is 'USA')
age_country_filter = df[(df['Age'] > 30) & (df['Country'] == 'USA')]
print("\nFiltered Data (Age > 30 and Country is USA):")
print(age_country_filter)

# Step 3: Filter using a list of values (e.g., filtering for specific countries)
countries_filter = df[df['Country'].isin(['USA', 'Canada'])]
print("\nFiltered Data (Country is USA or Canada):")
print(countries_filter)

# Step 4: Filter by string condition (e.g., Name starts with 'A')
name_filter = df[df['Name'].str.startswith('A')]
print("\nFiltered Data (Name starts with 'A'):")
print(name_filter)

# Step 5: Filtering based on Salary (e.g., Salary greater than or equal to 45000)
salary_filter = df[df['Salary'] >= 45000]
print("\nFiltered Data (Salary >= 45000):")
print(salary_filter)
