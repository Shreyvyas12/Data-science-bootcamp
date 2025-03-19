# 1.⁠ ⁠Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.
# import pandas as pd
# import matplotlib.pyplot as plt
# # Read the dataset
# url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
# df = pd.read_csv(url)
print()
print("Q1")
import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
# print(df.head())

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
# print(df.head())

weekday_data = df[df['hour_beginning'].dt.weekday < 5]
weekday_counts = weekday_data.groupby(df['hour_beginning'].dt.day_name())['Pedestrians'].sum()
weekday_counts = weekday_counts.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print(weekday_counts)

plt.figure(figsize=(8, 5))
weekday_counts.plot(kind='line', marker='o', color='blue')
plt.title('Pedestrian Counts for Weekdays (Monday to Friday)')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrians')
plt.grid(True)
plt.show()

# 2. ⁠Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity in that year. 
# Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix) between weather patterns and pedestrian counts for the selected year.
# -This question requires you to show the relationship between a numerical feature(Pedestrians) and a non-numerical feature(Weather Summary). 
# In such instances we use Encoding. Each weather condition can be encoded as numbers( 0,1,2..). This technique is called One-hot encoding.
# -Correlation matrices may not always be the most suitable visualization method for relationships involving categorical data points, 
# nonetheless this was given as a question to help you understand the concept better.
print()
print("Q2")
brooklyn_2019 = df[(df['location'] == 'Brooklyn Bridge') & (df['hour_beginning'].dt.year == 2019)]
brooklyn_2019['weather_summary'].fillna('unknown', inplace=True)
weather_encoded = pd.get_dummies(brooklyn_2019['weather_summary'])
brooklyn_2019 = pd.concat([brooklyn_2019, weather_encoded], axis=1)
correlation_matrix = brooklyn_2019[['Pedestrians'] + list(weather_encoded.columns)].corr()

print("Correlation Matrix between Weather and Pedestrian Counts:\n", correlation_matrix)
plt.figure(figsize=(8, 5))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.title('Correlation Matrix: Weather vs Pedestrian Counts (2019)')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.show()

# 3.⁠ ⁠Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. 
# Use this new column to analyze pedestrian activity patterns throughout the day.
# -Students can also show plots analyzing activity.
print()
print("Q3")
def categorize_time(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['Time of Day'] = df['hour_beginning'].dt.hour.apply(categorize_time)
time_of_day_counts = df.groupby('Time of Day')['Pedestrians'].sum().reindex(['Morning', 'Afternoon', 'Evening', 'Night'])
print(time_of_day_counts)

plt.figure(figsize=(8, 5))
time_of_day_counts.plot(kind='bar', color='skyblue')
plt.title('Pedestrian Activity by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrians')
plt.xticks(rotation=45)
plt.show()