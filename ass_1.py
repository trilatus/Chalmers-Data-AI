import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("swedish_population_by_year_and_sex_1860-2022.csv")
    #Start with filtering out data that is not intresting when it comes to the task at hand
    df = df.drop("sex", axis=1) #Sex is not intresting in this scenario
    df = df.drop("age", axis=1) #Age is intresting but due to the slicing operations later its not needed.
    child = df.iloc[0:30]
    child = pd.DataFrame(child[:].sum(), columns=["sum"]) #wildcard select all col then sum
    labor = df.iloc[30:130]
    labor = pd.DataFrame(labor[:].sum(), columns=["sum"])
    elder = df.iloc[130:]
    elder = pd.DataFrame(elder[:].sum(), columns=["sum"])

    tot = elder["sum"] + labor["sum"] + child["sum"]
    index = elder.index #index range of 1860 - 2022

    tmp = pd.DataFrame(100 * ((elder["sum"] + child["sum"]) / labor["sum"]))
    plt.plot(index, elder/tmp)
    plt.plot(index, child/tmp)
    plt.plot(index, labor/tmp)
    #elder.index
    #Think this is task 1 done?
    #plt.plot(index, (100 * ((elder["sum"] + child["sum"]) / labor["sum"]))) #Formula used in task 1
    plt.xlabel("Year")
    plt.ylabel("Dependency ratio")
    
    plt.show()

    #Task 1 works but mby not super optimal