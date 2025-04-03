import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker

font = {'family': 'Arial', 'weight': 'normal', 'size': 30}
label_font = {'family': 'Arial', 'weight': 'normal', 'size': 40}
axes = {'linewidth': 2}
lines = {'linewidth': 2}

matplotlib.rc('font', **font)           # set font
matplotlib.rc('axes', **axes)           # set axes
matplotlib.rc('lines', **lines)         # set lines

def pyOrigin(ax, x, y, x_scale="linear", y_scale="linear", x_tick_format=None, y_tick_format=None,
                         x_tick_distance=None, y_tick_distance=None, x_sci_format=False,
                         y_sci_format=False, x_lim=None, y_lim=None):
    """
    Configures tick marks and axes to create an Origin-like plot style using Matplotlib.

    Parameters:
    ax (matplotlib.axes.Axes): The primary axes on which the plot is drawn.
    x (array-like): Data for the x-axis (used for synchronizing twin axes).
    y (array-like): Data for the y-axis (used for synchronizing twin axes).
    x_scale (str): Scale for the x-axis ('linear' or 'log'). Default is 'linear'.
    y_scale (str): Scale for the y-axis ('linear' or 'log'). Default is 'linear'.
    x_tick_format (int, optional): Number of decimal places for x-axis tick labels. Default is None.
    y_tick_format (int, optional): Number of decimal places for y-axis tick labels. Default is None.
    x_tick_distance (float, optional): Distance between major ticks on the x-axis. Default is None.
    y_tick_distance (float, optional): Distance between major ticks on the y-axis. Default is None.
    x_sci_format (bool): Use scientific notation for x-axis. Default is False.
    y_sci_format (bool): Use scientific notation for y-axis. Default is False.
    x_lim (tuple, optional): Limits for the x-axis in the form (min, max). Default is None.
    y_lim (tuple, optional): Limits for the y-axis in the form (min, max). Default is None.

    Returns:
    tuple: The primary axes and the two twin axes (ax, ax2, ax3) for further customization.
    """

    # Set the scale and tick parameters for the primary axes
    ax.set_xscale(x_scale)
    ax.set_yscale(y_scale)
    ax.tick_params(axis='both', which='major', length=8, width=2)
    ax.tick_params(axis='both', which='minor', length=4, width=2)

    # Create twin axes on the right (ax2) for the y-axis and top (ax3) for the x-axis
    ax2 = ax.twinx()  # Right Y-axis
    ax3 = ax.twiny()  # Top X-axis

    # Customize ax2 (right y-axis)
    ax2.set_yscale(y_scale)  # Match the y-scale with the main axis
    ax2.plot(x, y, alpha=0.0)  # Invisible plot to synchronize axes
    ax2.yaxis.set_ticks_position('right')
    ax2.tick_params(axis='y', direction='in', labelleft=False, labelright=False, length=8, width=2)

    # Customize ax3 (top x-axis)
    ax3.set_xscale(x_scale)  # Match the x-scale with the main axis
    ax3.plot(x, y, alpha=0.0)  # Invisible plot to synchronize axes
    ax3.xaxis.set_ticks_position('top')
    ax3.tick_params(axis='x', direction='in', labeltop=False, labelbottom=False, length=8, width=2)

    # Hide the spines on the right and top
    ax2.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')

    # Apply custom formatting to tick labels if specified
    if x_tick_format is not None:
        formatter = ticker.FormatStrFormatter(f"%.{x_tick_format}f")
        ax.xaxis.set_major_formatter(formatter)
        ax3.xaxis.set_major_formatter(formatter)

    if y_tick_format is not None:
        formatter = ticker.FormatStrFormatter(f"%.{y_tick_format}f")
        ax.yaxis.set_major_formatter(formatter)
        ax2.yaxis.set_major_formatter(formatter)

    # Set custom tick intervals if specified
    if x_tick_distance is not None:
        locator = ticker.MultipleLocator(x_tick_distance)
        ax.xaxis.set_major_locator(locator)
        ax3.xaxis.set_major_locator(locator)

    if y_tick_distance is not None:
        locator = ticker.MultipleLocator(y_tick_distance)
        ax.yaxis.set_major_locator(locator)
        ax2.yaxis.set_major_locator(locator)

    # Use scientific notation if specified
    if x_sci_format:
        ax.xaxis.set_major_formatter(ticker.LogFormatterMathtext())
        ax3.xaxis.set_major_formatter(ticker.LogFormatterMathtext())

    if y_sci_format:
        ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext())
        ax2.yaxis.set_major_formatter(ticker.LogFormatterMathtext())

    # Apply axis limits if specified
    if x_lim is not None:
        ax.set_xlim(x_lim)
        ax3.set_xlim(x_lim)

    if y_lim is not None:
        ax.set_ylim(y_lim)
        ax2.set_ylim(y_lim)


colors = [
    "#515151", "#F14040", "#1A6FDF", "#37AD6B", "#B177DE", "#CC9900",
    "#00CBCC", "#7D4E4E", "#8E8E00", "#FB6501", "#6699CC", "#6FB802"
] # Color4line in Origin

fig = plt.figure(num=1, figsize=(13, 9))
ax1 = fig.add_subplot(111)
ax1.plot(x, y, color = colors[1], linewidth = 8, alpha=0.8, label = "Any")
ax1.set_ylabel('Voltage (V)', fontdict=label_font)
ax1.set_xlabel('Time (ns)', fontdict=label_font)
ax1.legend(frameon = False)
pyOrigin(ax1, x, y, x_tick_format=1, y_tick_format=1, y_tick_distance=0.1)

plt.tight_layout()
position = path_fig + '_1.jpg'
fig.savefig(position, bbox_inches='tight', pad_inches=0.27, dpi=300, format='jpg')
plt.show()
