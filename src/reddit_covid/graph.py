import matplotlib.pyplot as plt
import importlib.resources as pkg_resources
import io


def graph(df):
    with pkg_resources.path(__package__, "graphing") as path:
        plt.style.use(path / "style.mplstyle")

    posIncrease = df['positiveIncrease']
    yticks = [
        posIncrease.min(),
        posIncrease.median(),
        posIncrease.max()
    ]

    reversed = df[::-1]
    plt.stackplot(reversed['date'],
                  reversed['positiveIncrease'], color='#d38fc5')
    plt.gcf().set_size_inches(4, 3)

    f = io.BytesIO()
    plt.show()
    exit(0)
    plt.savefig(f, bbox_inches='tight')
    return f.getvalue()
