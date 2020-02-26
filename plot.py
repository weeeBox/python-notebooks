import matplotlib.pyplot as plt


def to_plot_points(points):
    if isinstance(points, str):
        values = points.split()
        x = [int(values[i]) for i in range(len(values)) if i % 2 == 0]
        y = [int(values[i]) for i in range(len(values)) if i % 2 == 1]
    else:
        x = [p[0] for p in points]
        y = [p[1] for p in points]

    return x, y


def figure():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot()
    return ax


def plot_points(ax, points, color='b'):
    x, y = to_plot_points(points)
    ax.scatter(x, y, color=color)


def plot_line(ax, points, color='b'):
    x, y = to_plot_points(points)
    ax.scatter(x, y, color=color)
    ax.plot(x, y, color=color)


def plot_polygon(ax, points, color='r'):
    x, y = to_plot_points(points)
    ax.scatter(x, y, color=color)
    x.append(x[0])
    y.append(y[0])
    ax.plot(x, y, color=color)
