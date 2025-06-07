import seaborn as sns
import matplotlib.pyplot as plt

# Wbudowany zestaw danych
data = sns.load_dataset("iris")

# Wykres rozrzutu
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.title("Seaborn - Iris Dataset")
plt.show()
