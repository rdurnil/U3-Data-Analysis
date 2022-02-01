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
    col.sort() # inplace 
    # parallel lists
    values = []
    counts = []
    for value in col:
        if value in values: # seen it before
            counts[-1] += 1 # okay because sorted
        else: # haven't seen it before
            values.append(value)
            counts.append(1)

    return values, counts # we can return multiple values in python
    # they are packaged into a tuple

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]

    msrps = get_column(msrp_table, header, "MSRP")
    print("msrps:", msrps)
    # TASK: define/call another get_frequencies_categorical() 
    # that returns a dictionary of value: count mappings for categorical attributes

    # warmup
    msrp_values, msrp_counts = get_frequencies(msrp_table, header, "ModelYear")
    print(msrp_values, msrp_counts)

    # more on attributes
    # 1. what is the type?
    # e.g. how is it stored?
    # int, float, str, list...
    # 2. what is the semantic type of the attribute (and its values)?
    # e.g. what does the attribute represent?
    # domain knowledge!!
    # 3. what is the attribute's measurement scale?
    # categorical vs continuous (numeric)
    # nominal: categorical w/no inherent ordering
    # ex: eye color, names, zip codes, etc.
    # ordinal: categorical w/an inherent ordering
    # ex: T-shirt sizes (XS, S, M, L, ...) and letter grades (A, A-, B+, ...)
    # ratio-scaled: continuous with a 0 value that means absence
    # ex: 0lbs is an absence of weight
    # ex: 0 degrees K is an absence of temperature
    # interval: continuous without an inherent absence value
    # ex: 0 degrees F does not mean absence of temperature

    # noisy vs invalid values
    # noisy means valid on the scale but recorded incorrectly
    # ex: 18 year old records 81 as their age
    # invalid: not valid on the scale
    # ex: someone enters "bob" for their age

    # missing values
    # 2 main ways to deal with them
    # 1. discard them
    # really only do this when the dataset is large and the number of missing values
    # are small
    # we never want to throw away data
    # 2. fill them
    # 2.A. categorical attribute: majority voting system (e.g. most frequent value)
    # 2.B. continuous attribute: central tendency measure (e.g. mean, median, mode)
    # later... 2.A and 2.B can be more "intelligent": use similar subgroups 
    # (or the kNN algorithm), etc.

    # summary stats
    # min, max
    # mid-value (AKA mid-range)
    msrp_mid_value = (min(msrps) + max(msrps)) / 2
    print("mid value:", msrp_mid_value)
    # arithmetic mean 
    msrp_mean = sum(msrps) / len(msrps)
    print("mean:", msrp_mean)
    # note: mean is subject by outliers
    # sometimes we prefer the median (middle number in a sorted list)
    # mode: most frequently occuring value(s) in the list

    # data dispersion
    # variance: measures the spread of data
    # low variance: data is close to the mean
    # standard deviation: square root of variance
    # variance: average of the squared mean deviations
    squared_mean_deviations = [(x - msrp_mean) ** 2 for x in msrps] # list comprehension
    msrp_variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    msrp_stdev = np.sqrt(msrp_variance)
    print("stdev:", msrp_stdev)
    # compare our stdev calculation with numpy
    # assert msrp_stdev == np.std(msrps)
    # when comparing floating point numbers use np.isclose()
    # and np.allclose() 
    # the latter is for a list of floating point numbers
    assert np.isclose(msrp_stdev, np.std(msrps))
    # more on standard deviation
    # empirical rule for normal distributions (bell shaped curves)
    # 68% of data is within +/- 1 stdev of the mean
    # 95% of data is within +/- 2 stdev of the mean
    # 99.7% of data is within +/- 3 stdev of the mean
    
    # quantiles
    # are used to partition (sorted) data into roughly equal sized groups
    # 2 quantiles: 2 groups, 1 cut-off point (median)
    # quartiles: 4 groups, 3 cut-off points
    # percentiles: 100 groups, 99 cut-off points
    # more on percentiles later...


if __name__ == "__main__":
    main()