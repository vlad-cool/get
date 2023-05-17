#!/usr/bin/python3
import matplotlib.pyplot as plt

data = []
time = []

time_step = 0
adc_step = 0

charge_time = 0
discharge_time = 0

with open("settings.txt", "r") as f:
    time_step = float(f.readline())
    adc_step = float(f.readline())

with open("data.txt", "r") as dat:
    i = 0
    d = dat.readline()
    while d:
        data.append(int(dat.readline()) * 3.3 / 256)
        time.append(time_step * i)
        d = dat.readline()
        i += 1

charge_time = data.index(max(data)) * time_step
discharge_time = len(data) * time_step - charge_time

plt.plot(time, data, color="red", marker="o", markevery=10, markersize=2, linewidth=0.5, label="Зависимость напряжения\nот времени")
plt.title("Процесс заряда и разряда конденсатора в RC-цепочке")
plt.legend(frameon=False, loc=1)
plt.xlabel("Время эксперимента, с")
plt.ylabel("Напряжение на конденсаторе, В")
plt.grid(color="lightgray", which="major")
plt.grid(color="lightgray", linestyle="--", which="minor")
plt.minorticks_on()
plt.annotate(f"Время заряда: {round(charge_time, 2)}с\nВремя разряда: {round(discharge_time, 2)}с", (1, 0))
#plt.show()
plt.savefig("plot.svg", format="svg")