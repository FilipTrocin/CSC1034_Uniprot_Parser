import matplotlib.pyplot as plt

def plot_bar_show(d):
    """Printing a bar chart"""

    r = range(0, len(d))
    plt.figure()
    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.tight_layout()
    plt.show()

def plot_pie_show(d):

    labels = d.keys()
    sizes = d.values()
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
