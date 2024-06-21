import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "c"]
    values = [20, 34, 120] 

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()

generate_pie_chart()