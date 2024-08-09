def pyOrigin(ax, x, y, scale="linear"):
    """
    Adjusts the direction of tick marks on the left, bottom, right, and top axes, 
    and hides the tick labels and gridlines on the right and top axes.

    Parameters:
    ax (matplotlib.axes.Axes): The primary axis on which to set the tick directions.
    x (array-like): Data for the x-axis.
    y (array-like): Data for the y-axis.
    scale (str, optional): The scale for the y-axis, either 'linear' or 'log'. Defaults to 'linear'.

    Returns:
    tuple: The original axis (ax), the twin y-axis (ax2), and the twin x-axis (ax3).
    """
    
    # Set the direction of tick marks on the left and bottom axes to point inward
    ax.tick_params(axis='both', which='major', length=8, width=2)
    ax.tick_params(axis='both', which='minor', length=4, width=2)

    # Create twin axes for the right y-axis and top x-axis
    ax2 = ax.twinx()
    ax3 = ax.twiny()

    # Set the tick marks on the right y-axis to point inward and hide labels
    ax2.yaxis.set_ticks_position('right')
    ax2.plot(x, y, alpha=0.0)  # Plot an invisible line to synchronize the scale
    ax2.set_yscale(scale)
    ax2.tick_params(axis='y', which="both", direction='in', labelleft=False, labelright=False)
    ax2.tick_params(axis='both', which='major', length=8, width=2)
    ax2.tick_params(axis='both', which='minor', length=4, width=2)

    # Set the tick marks on the top x-axis to point inward and hide labels
    ax3.xaxis.set_ticks_position('top')
    ax3.plot(x, y, alpha=0.0)  # Plot an invisible line to synchronize the scale
    ax3.tick_params(axis='x', which="both", direction='in', labeltop=False, labelbottom=False)
    ax3.set_yscale(scale)
    ax3.tick_params(axis='both', which='major', length=8, width=2)
    ax3.tick_params(axis='both', which='minor', length=4, width=2)

    # Hide the gridlines and spines (borders) on the right and top axes
    ax2.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')

    return ax, ax2, ax3
