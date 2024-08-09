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

def pyOrigin(ax, x, y, scale="linear", x_tick_format=None, y_tick_format=None,
                         x_tick_distance=None, y_tick_distance=None, x_sci_format=False,
                         y_sci_format=False, x_lim=None, y_lim=None):
    """
    Configures the appearance of tick marks on a Matplotlib plot, including creating twin axes for additional customization.

    Parameters:
    ax (matplotlib.axes.Axes): The primary axes on which the plot is drawn.
    x (array-like): Data for the x-axis (used for synchronizing twin axes).
    y (array-like): Data for the y-axis (used for synchronizing twin axes).
    scale (str): The scale of the axes, either "linear" or "log" (default is "linear").
    x_tick_format (int, optional): Number of decimal places for x-axis tick labels. Default is None.
    y_tick_format (int, optional): Number of decimal places for y-axis tick labels. Default is None.
    x_tick_distance (float, optional): Distance between major ticks on the x-axis. Default is None.
    y_tick_distance (float, optional): Distance between major ticks on the y-axis. Default is None.
    x_sci_format (bool): Whether to use scientific notation for x-axis. Default is False.
    y_sci_format (bool): Whether to use scientific notation for y-axis. Default is False.
    x_lim (tuple, optional): Limits for the x-axis in the form (min, max). Default is None.
    y_lim (tuple, optional): Limits for the y-axis in the form (min, max). Default is None.

    Returns:
    tuple: The primary axes and the two twin axes (ax, ax2, ax3) for further customization.
    """

    # Set the tick direction and size for both major and minor ticks on the primary axes.
    ax.tick_params(axis='both', which='major', length=8, width=2)
    ax.tick_params(axis='both', which='minor', length=4, width=2)

    # Create twin axes: ax2 on the right for the y-axis, and ax3 on the top for the x-axis.
    ax2 = ax.twinx()  # Twin y-axis on the right side.
    ax3 = ax.twiny()  # Twin x-axis on the top side.

    # Customize ax2 (right y-axis): Set ticks to point inward and hide the tick labels.
    ax2.yaxis.set_ticks_position('right')
    ax2.plot(x, y, alpha=0.0)  # Synchronize with main axes using an invisible plot.
    ax2.set_yscale(scale)  # Apply the same scale as the primary y-axis.
    ax2.tick_params(axis='y', which="both", direction='in', labelleft=False, labelright=False)
    ax2.tick_params(axis='both', which='major', length=8, width=2)
    ax2.tick_params(axis='both', which='minor', length=4, width=2)

    # Customize ax3 (top x-axis): Set ticks to point inward and hide the tick labels.
    ax3.xaxis.set_ticks_position('top')
    ax3.plot(x, y, alpha=0.0)  # Synchronize with main axes using an invisible plot.
    ax3.tick_params(axis='x', which="both", direction='in', labeltop=False, labelbottom=False)
    ax3.tick_params(axis='both', which='major', length=8, width=2)
    ax3.tick_params(axis='both', which='minor', length=4, width=2)

    # Hide the spines (axis lines) on the right and top to keep the plot clean.
    ax2.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')

    # Apply custom formatting to x-axis ticks if specified.
    if x_tick_format is not None:
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{x_tick_format}f"))
        ax3.xaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{x_tick_format}f"))

    # Apply custom formatting to y-axis ticks if specified.
    if y_tick_format is not None:
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{y_tick_format}f"))
        ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{y_tick_format}f"))

    # Set custom major tick intervals for the x-axis if specified.
    if x_tick_distance is not None:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_distance))
        ax3.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_distance))

    # Set custom major tick intervals for the y-axis if specified.
    if y_tick_distance is not None:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_distance))
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_distance))

    # Use scientific notation for the x-axis if specified.
    if x_sci_format:
        ax.xaxis.set_major_formatter(ticker.LogFormatterMathtext())
        ax3.xaxis.set_major_formatter(ticker.LogFormatterMathtext())

    # Use scientific notation for the y-axis if specified.
    if y_sci_format:
        ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext())
        ax2.yaxis.set_major_formatter(ticker.LogFormatterMathtext())

    # Apply limits to the x-axis if specified.
    if x_lim is not None:
        ax.set_xlim(x_lim)
        ax3.set_xlim(x_lim)

    # Apply limits to the y-axis if specified.
    if y_lim is not None:
        ax.set_ylim(y_lim)
        ax2.set_ylim(y_lim)

    # Return the main axes and the two twin axes for further customization.
    return ax, ax2, ax3


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
pyOrigin(ax1, x, y)

plt.tight_layout()
position = path_fig + '_1.jpg'
fig.savefig(position, bbox_inches='tight', pad_inches=0.27, dpi=300, format='jpg')
plt.show()
