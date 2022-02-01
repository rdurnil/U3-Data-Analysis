import numpy as np 

def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        value = row[col_index]
        if value != "NA":
            col.append(value)
    return col 

def get_frequencies(table, header, col_name):
    col = get_column(table, header, col_name)
    col.sort() # inplace sort
    values = []
    counts = []
    for value in col:
        if value in values:
            counts[-1] += 1 # okay because col is sorted
        else: # haven't seen this value before
            values.append(value)
            counts.append(1)
    return values, counts # we can return multiple items
    # packaged into a tuple

# TASK: define/call get_frequencies_categorical() 
# which works for nominal attributes (that have no order)
# return a dictionary of category: count

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]
    msrps = get_column(msrp_table, header, "MSRP")
    print("msrps:", msrps)
    # warmup
    msrp_values, msrp_counts = get_frequencies(msrp_table, header, "ModelYear")
    # tuple unpacking
    print(msrp_values, msrp_counts)

    # more on attributes
    # 1. what is the type of the attribute?
    # e.g. how is it stored?
    # int, float, str, list, ...
    # 2. what is the attribute's semantic type?
    # e.g. what does the attribute (and its values) represent?
    # domain knowledge!!
    # 3. what is the attribute's measurement scale?
    # categorical vs continuous (numeric) scales
    # nominal: categories without an inherent ordering
    # ex: eye color, names, zip codes
    # ordinal: categories with an inherent ordering
    # ex: T-shirt sizes (S, M, L, etc.), letter grades (A, A-, B+,...)
    # ratio-scaled: continuous where 0 means absence
    # ex: 0lbs in weight means an absence of weight
    # ex: 0 degrees K means an absence of temperature
    # interval: continuous without an inherence absence value
    # ex: 0 degrees F does not mean an absence of temperature

    # noisy vs invalid values
    # noisy: valid on the scale, but recorded incorrectly
    # ex: an 18-year old enters 81 as their age
    # invalid: not valid no the scale
    # ex: someone enters "bob" as their age

    # missing values
    # 2 main ways to deal
    # 1. discard them
    # you only want to consider discarding missing values when
    # your dataset is large and the missing values quantity is small
    # we never want to throw away data
    # 2. fill them
    # 2.A. categorical attribute: use a majority vote system 
    # (e.g. the most frequent value)
    # 2.B. continuous attribute: use central tendency measure 
    # (e.g. mean, median, mode, etc.)
    # note: (later) do it more "intelligently" such as using subgroups or kNN algorithm

    # summary stats
    # min, max
    # mid-range (AKA mid-value)
    msrp_midrange = (min(msrps) + max(msrps)) / 2
    print("midrange:", msrp_midrange)
    # arithmetic mean
    msrp_mean = sum(msrps) / len(msrps)
    print("mean:", msrp_mean)
    # the mean is subject to outliers
    # sometimes we prefer to use the median
    # median: the middle value in a sorted list of numbers
    # mode: the most frequently occuring value(s)
    # data dispersion
    # how spread out is the data
    # variance: average of the squared mean deviations
    # low variance: data is clustered around the mean
    squared_mean_deviations = [(x - msrp_mean) ** 2 for x in msrps] # list comprehension
    msrp_variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    # standard deviation is the square root of the variance
    msrp_stdev = np.sqrt(msrp_variance)
    print("stdev:", msrp_stdev)
    # check our work with numpy
    # assert msrp_stdev == np.std(msrps)
    # use np.isclose() to compare two floating point numbers
    # use np.allclose() to compare two lists of floating point numbers
    assert np.isclose(msrp_stdev, np.std(msrps))
    # empirical rule for normal distributions (bell-shaped curves)
    # 68% data is within mean +/- 1 stdev
    # 95% data is within mean +/- 2 stdevs
    # 99.7% data is within mean +/- 3 stdevs
    # quantiles
    # used to partition (sorted) data into roughly equal sized groups
    # 2-quantiles: 2 groups, 1 cut-off point (median)
    # quartiles: 4 groups, 3 cut-off points
    # percentiles: 100 groups, 99 cut-off points
    # more on percentiles later...

if __name__ == "__main__":
    main()