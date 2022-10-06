import openpyxl
import matplotlib.pyplot as plt
wk = openpyxl.load_workbook('d:/炼狱.xlsx')
sheet = wk['Sheet1']
colors = []
sizes = []
for i in range(1, 21):
    colors.append(sheet['A'+str(i)].value)
    sizes.append(sheet['B'+str(i)].value)

color_class = set(colors)
count = len(colors)
color_percent = []
for clr in color_class:
    color_percent.append(colors.count(clr)/count)

plt.pie(x=color_percent, labels=color_class, autopct='%1.0f')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.legend()
plt.savefig('d:/炼狱.png')