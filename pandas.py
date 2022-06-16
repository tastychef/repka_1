import pandas as pd
import matplotlib.pyplot as plt

week = pd.Serius({"ПН": 90, "ВТ": 90, "СР": 90, "ЧТ": 90, "ПТ": 90,})
plt.title("График")
plt.plot(week)
plt.show()
