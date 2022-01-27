
def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        value = row[col_index]
        if value != "NA":
            col.append(value)
    return col 

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]

    msrps = get_column(msrp_table, header, "MSRP")
    print("msrps:", msrps)

    # more on attributes
    # 1. what is the type?
    # e.g. how is it stored?
    # int, float, str, list...
    # 2. what is the semantic type of the attribute (and its values)?
    # e.g. what does the attribute represent?
    # domain knowledge!!
    # 3. what is the attribute's measurement scale?
    # categorical vs continuous
    # nominal: categorical w/no inherent ordering
    # ordinal: categorical w/an inherent ordering
    # TODO: start with categorical examples then move on to continous

if __name__ == "__main__":
    main()