import numpy as np
import pandas as pd



def pivot_table_grouping(dataframe, index, columns, metrics, index_sort, columns_sort, aggfunc):
    """
    We define a function to produce a pivot table that group by model, iterations, and threshold, applying an aggregation function.
    """

    # Group into a pivot table.
    result_df = dataframe.pivot_table(index=index, columns=columns, values=metrics, aggfunc=aggfunc)

    # Sort the index.
    if index_sort:
        if len(index_sort) == 1:
            result_df = result_df.reindex(index_sort[0])
        elif len(index_sort) > 1:
            for i, sorting in enumerate(index_sort):
                result_df = result_df.reindex(sorting, level=i)

    # Sort the columns.
    if columns_sort:
        if len(columns_sort) == 1:
            result_df = result_df.reindex(columns_sort[0], axis=1)
        if len(columns_sort) > 1:
            for i, sorting in enumerate(columns_sort):
                result_df = result_df.reindex(sorting, level=i, axis=1)

    return result_df


def median_long_dataframe(dataframe, models, metrics):
    """
    We define a utility function to prepare the data.
    """

    # Compute the medians for each of the groups.
    median_df = dataframe[dataframe['model'].isin(models)].groupby(['model', 'iterations', 'threshold', 'selector', 'sampler'], observed=True).median().drop(columns=['fold'])

    # Transform the data from wide to long.
    long_median_df = pd.melt(median_df.reset_index(), id_vars=['model', 'iterations', 'threshold', 'selector', 'sampler'], value_vars=metrics)

    # Transform the "variable" label into categorical.
    long_median_df['variable'] = pd.Categorical(long_median_df['variable'], categories=metrics)

    # Return the dataframe.
    return long_median_df
