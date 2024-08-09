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
             x_tick_distance=None, y_tick_distance=None):
    """
    Customizes the appearance and behavior of tick marks on a Matplotlib plot.
    
    Parameters:
    - ax: Matplotlib axes object.
    - x, y: Data for plotting on the additional axes (right and top) to synchronize.
    - scale: Scale type for the plot, either 'linear' or 'log' (default is 'linear').
    - x_tick_format: Number of decimal places for X-axis tick labels (optional, default is None).
    - y_tick_format: Number of decimal places for Y-axis tick labels (optional, default is None).
    - x_tick_distance: Custom interval between major ticks on the X-axis (optional).
    - y_tick_distance: Custom interval between major ticks on the Y-axis (optional).
    
    Returns:
    - ax: The original axes.
    - ax2: The twin axes on the right (Y-axis).
    - ax3: The twin axes on the top (X-axis).
    """
    
    # Set the direction and size of tick marks on the left and bottom axes
    ax.tick_params(axis='both', which='major', length=8, width=2)
    ax.tick_params(axis='both', which='minor', length=4, width=2)

    # Create twin axes on the right (ax2) and top (ax3)
    ax2 = ax.twinx()  # Right Y-axis
    ax3 = ax.twiny()  # Top X-axis

    # Customize the right Y-axis ticks: point inward, hide labels
    ax2.yaxis.set_ticks_position('right')
    ax2.plot(x, y, alpha=0.0)  # Invisible plot to synchronize axes
    ax2.set_yscale(scale)  # Set the scale (linear or logarithmic)
    ax2.tick_params(axis='y', which="both", direction='in', labelleft=False, labelright=False)
    ax2.tick_params(axis='both', which='major', length=8, width=2)
    ax2.tick_params(axis='both', which='minor', length=4, width=2)

    # Customize the top X-axis ticks: point inward, hide labels
    ax3.xaxis.set_ticks_position('top')
    ax3.plot(x, y, alpha=0.0)  # Invisible plot to synchronize axes
    ax3.tick_params(axis='x', which="both", direction='in', labeltop=False, labelbottom=False)
    ax3.set_yscale(scale)  # Set the scale (linear or logarithmic)
    ax3.tick_params(axis='both', which='major', length=8, width=2)
    ax3.tick_params(axis='both', which='minor', length=4, width=2)

    # Hide grid lines and labels on the right and top spines
    ax2.spines['right'].set_color('none')  # Hide the right spine
    ax3.spines['top'].set_color('none')    # Hide the top spine

    # Format tick labels to display a specific number of decimal places if specified
    if x_tick_format is not None:
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{x_tick_format}f"))
        ax3.xaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{x_tick_format}f"))

    if y_tick_format is not None:
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{y_tick_format}f"))
        ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter(f"%.{y_tick_format}f"))

    # Set custom tick intervals if specified
    if x_tick_distance is not None:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_distance))
        ax2.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_distance))

    if y_tick_distance is not None:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_distance))
        ax3.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_distance))

    # Return the main and twin axes
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
set_ticks_directions(ax1, x_fit, y_fit)

plt.tight_layout()
position = path_fig + '_1.jpg'
fig.savefig(position, bbox_inches='tight', pad_inches=0.27, dpi=300, format='jpg')
plt.show()
