import matplotlib.pyplot as plt

labels = ['Только 5', '4 и 5', 'С тройками', 'С пересдачами', 'Не сдали']
sizes = [10, 13, 8, 4, 2]
colors = ['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightgray']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.savefig('chart.png')
plt.show()