import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)  
days = 30
temperature = np.random.uniform(low=20.0,high=45.0,size=days).round(1)
print("🌡️ daily temprature are \n",temperature)

#these  fucnction show's all days which have max temprature or min temprature
max_temp  = np.max(temperature)
min_temp  = np.min(temperature)
max_day = np.argmax(temperature)+1
min_day = np.argmin(temperature) + 1
avg_temp = np.mean(temperature)

#identify hot days 

hot_days = temperature[temperature  > 35]
cold_days = temperature[temperature < 25]
# print(hot_days)

adjust_temp = temperature.copy()
adjust_temp[adjust_temp>40] += 2


#display all summary
print("\nSummary:")

print(f"Highest Temperature: {max_temp}°C")
print(f"Lowest Temperature: {min_temp}°C")
print(f"average temperature: {avg_temp}")
print("\nHot Days (>35°C):", hot_days)
print("Cold Days (<25°C):", cold_days)

print("\nAdjusted Temperatures (after heat wave simulation):")
print(adjust_temp)

plt.figure(figsize=(10,6))


#it shows the temperature of month
plt.plot(temperature, label='Temperature', color='blue', marker='o')
plt.title("TEMPERATURE FOR 30 DAYS")
plt.legend()


plt.figure(figsize=(10, 6))
plt.hist(temperature,color='orange',bins=10,edgecolor = 'black')
plt.title("TEMPERATURE DISTRIBUATION")


hot_cold_count = [len(hot_days),len(cold_days)]
labels = ['Hot Days (>35°C)', 'Cold Days (<25°C)']
plt.figure(figsize=(8,5))
plt.bar(labels, hot_cold_count, color=['red', 'blue'])
plt.title("NO OF HOT AND COLD DAYS")
plt.show()