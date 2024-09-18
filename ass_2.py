import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://en.wikipedia.org/wiki/Five-number_summary
def FiveNumSum(data):
    return np.percentile(data, [0, 25, 50, 75, 100], method="midpoint")

df = pd.read_csv("out.csv")
df = df.drop("Unnamed: 0", axis=1)  #Remove dublicate id
df["Date of sale"] = df["Date of sale"].str.slice(start=1)  #Remove added blank space from the data
df = df[df["Date of sale"].str.contains("2022")]
df["Price"] = pd.to_numeric(df["Price"].str.replace("kr", "")) #Remove kr and change the data to numeric
print("Here is the five-number summary ", FiveNumSum(df["Price"]))

#Calculating bin size with the help of "Freedman–Diaconis rule"
#https://how2matplotlib.com/bin-size-in-matplotlib-histogram.html
iqr = np.subtract(*np.percentile(df["Price"], [75, 25]))
bin_width = 2 * iqr * len(df["Price"])**(-1/3)
num_bins = int((max(df["Price"]) - min(df["Price"])) / bin_width)

#Plotting Histogram
#plt.hist(df["Price"], bins=num_bins, color="yellow", edgecolor = "black")
plt.title("Closing Price Histogram")
plt.ylabel("Frequency")
plt.xlabel("Price")
#plt.show()

df['Living area'] = pd.to_numeric(df['Living area'].str.extract(r"\('(\d+)'")[0]) #Filter so only boarea is included
plt.scatter(df["Price"], df["Living area"])
plt.title("Scatter plot relation price, boarea")
plt.xlabel("Price")
plt.ylabel("Boarea")
#plt.show()

print(df)
df["No. rooms"] = pd.to_numeric(df["No. rooms"].str.replace("rum", "")) #Remove kr and change the data to numeric
#z = [x for x in range(190)] # för färg skit
plt.scatter(df["Price"], df["Living area"], c=df["No. rooms"], cmap="cividis")
plt.colorbar().set_label("No. rooms")
plt.show()