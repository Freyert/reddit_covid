import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import importlib.resources as pkg_resources
import io
import math


# data collection didn't start until a few weeks before this.
firstCleanPeriod = '2020-04-27'


def graph(df):
    with pkg_resources.path(__package__, "graphing") as path:
        plt.style.use(path / "style.mplstyle")

    fig = plt.figure()

    ax = fig.add_subplot()

    posIncrease = df.resample(
        'W-MON', on='date').sum().sort_values(by='date')
    # get left and bottom spines to cross
    ax.spines['left'].set_position(('axes', 0.04))
    ax.spines['bottom'].set_position(('axes', 0.03))

    day_fmt = mdates.DateFormatter('%b %d')
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(day_fmt)

    print(posIncrease['positiveIncrease'].pct_change())
    posIncrease['positiveIncrease'].pct_change(
    )[firstCleanPeriod:].plot(kind="line", ax=ax)

    f = io.BytesIO()
    plt.show()
    exit(0)
    fig.savefig(f, bbox_inches='tight')
    return f.getvalue()
