import plotnine as p9



def plot_distributions_bar_plot_grid(dataframe, figure_size=(14, 4)):
    """
    We create a function to plot the bar plot.
    """

    return (
        # Define the plot.
        p9.ggplot(dataframe, p9.aes(x='threshold', fill='value'))
        # Add the bars.
        + p9.geom_bar(position='dodge')
        + p9.geom_text(p9.aes(label='stat(count)'), stat='count', position=p9.position_dodge(0.9), size=7, va='bottom')
        # Rename the x axis.
        + p9.scale_x_discrete(name='Threshold')
        # Rename the y axis, give some space on top and bottom (mul_bottom, add_bottom, mul_top, add_top).
        + p9.scale_y_continuous(name='Count', expand=(0, 0, 0, 500))
        # Replace the names in the legend and set the colors of the bars.
        + p9.scale_fill_manual(values={0: '#009e73', 1: '#d55e00'}, labels=lambda l: [{0: 'Stable', 1: 'Unstable'}[x] for x in l])
        # Place the plots in a grid, renaming the labels.
        + p9.facet_grid('. ~ iterations', labeller=p9.labeller(cols=lambda x: f'iters = {x}'))
        # Define the theme for the plot.
        + p9.theme(
            # Remove the y axis name.
            axis_title_y=p9.element_blank(),
            # Set the size of x and y tick labels font.
            axis_text_x=p9.element_text(size=7),
            axis_text_y=p9.element_text(size=7),
            # Place the legend on top, without title, and reduce the margin.
            legend_title=p9.element_blank(),
            legend_position='top',
            legend_box_margin=2,
            # Set the size for the figure.
            figure_size=figure_size,
        )
    )


def plot_metrics_comparison_lineplot_grid(dataframe, models_labels, metrics_labels, figure_size=(14, 4)):
    """
    We define a function to plot the grid.
    """

    return (
        # Define the plot.
        p9.ggplot(dataframe, p9.aes(x='threshold', y='value', group='variable', color='variable', shape='variable'))
        # Add the points and lines.
        + p9.geom_point()
        + p9.geom_line()
        # Rename the x axis and give some space to left and right.
        + p9.scale_x_discrete(name='Threshold', expand=(0, 0.2))
        # Rename the y axis, give some space on top and bottom, and print the tick labels with 2 decimal digits.
        + p9.scale_y_continuous(name='Value', expand=(0, 0.05), labels=lambda l: ['{:.2f}'.format(x) for x in l])
        # Replace the names in the legend.
        + p9.scale_shape_discrete(name='Metric', labels=lambda l: [metrics_labels[x] for x in l])
        # Define the colors for the metrics for color-blind people.
        + p9.scale_color_brewer(name='Metric', labels=lambda l: [metrics_labels[x] for x in l], type='qual', palette='Set2')
        # Place the plots in a grid, renaming the labels for rows and columns.
        + p9.facet_grid('iterations ~ model', labeller=p9.labeller(rows=lambda x: f'iters = {x}', cols=lambda x: f'{models_labels[x]}'))
        # Define the theme for the plot.
        + p9.theme(
            # Remove the y axis name.
            axis_title_y=p9.element_blank(),
            # Set the size of x and y tick labels font.
            axis_text_x=p9.element_text(size=7),
            axis_text_y=p9.element_text(size=7),
            # Place the legend on top, without title, and reduce the margin.
            legend_title=p9.element_blank(),
            legend_position='top',
            legend_box_margin=2,
            # Set the size for the figure.
            figure_size=figure_size,
        )
    )


def plot_preprocessing_boxplot_overall(dataframe, metrics_labels, groups_labels, figure_size=(14, 4)):
    """
    We define a function to plot the boxplot.
    """

    return (
        # Define the plot.
        p9.ggplot(dataframe, p9.aes(x='group', y='value', fill='group'))
        # Add the boxplots.
        + p9.geom_boxplot(position='dodge')
        # Rename the x axis.
        + p9.scale_x_discrete(name='Group', labels=lambda l: [groups_labels[x] for x in l])
        # Rename the y axis.
        + p9.scale_y_continuous(name='Value', labels=lambda l: ['{:.2f}'.format(x) for x in l])
        # Define the colors for the groups for color-blind people.
        + p9.scale_fill_brewer(name='Group', labels=lambda l: [groups_labels[x] for x in l], type='qual', palette='Set2')
        # Place the plots in a grid, renaming the labels.
        + p9.facet_grid('variable ~ .', scales='free_y', labeller=p9.labeller(rows=lambda x: f'{metrics_labels[x]}'))
        # Define the theme for the plot.
        + p9.theme(
            # Remove the x and y axis names.
            axis_title_x=p9.element_blank(),
            axis_title_y=p9.element_blank(),
            # Set the size of x and y tick labels font.
            axis_text_x=p9.element_text(size=7),
            axis_text_y=p9.element_text(size=7),
            # Place the legend on top, without title, and reduce the margin.
            legend_title=p9.element_blank(),
            legend_position='top',
            legend_box_margin=2,
            # Set the size for the figure.
            figure_size=figure_size,
        )
    )


def plot_preprocessing_boxplot_bymodel(dataframe, models_labels, metrics_labels, groups_labels, figure_size=(14, 4)):
    """
    We define a function to plot the grid.
    """

    return (
        # Define the plot.
        p9.ggplot(dataframe, p9.aes(x='variable', y='value', fill='group'))
        # Add the boxplots.
        + p9.geom_boxplot(position='dodge')
        # Rename the x axis.
        + p9.scale_x_discrete(name='Metric', labels=lambda l: [metrics_labels[x] for x in l])
        # Rename the y axis.
        + p9.scale_y_continuous(name='Value', expand=(0, 0.05), 
        # breaks=[-0.25, 0, 0.25, 0.5, 0.75, 1], limits=[-0.25, 1],
        labels=lambda l: ['{:.2f}'.format(x) for x in l])
        # Define the colors for the metrics for color-blind people.
        + p9.scale_fill_brewer(name='Group', labels=lambda l: [groups_labels[x] for x in l], type='qual', palette='Set2')
        # Place the plots in a grid, renaming the labels.
        + p9.facet_grid('model ~ .', scales='free_y', labeller=p9.labeller(rows=lambda x: f'{models_labels[x]}'))
        # Define the theme for the plot.
        + p9.theme(
            # Remove the x and y axis names.
            axis_title_x=p9.element_blank(),
            axis_title_y=p9.element_blank(),
            # Set the size of x and y tick labels font.
            axis_text_x=p9.element_text(size=7),
            axis_text_y=p9.element_text(size=7),
            # Place the legend on top, without title, and reduce the margin.
            legend_title=p9.element_blank(),
            legend_position='top',
            legend_box_margin=2,
            # Set the size for the figure.
            figure_size=figure_size,
        )
    )
