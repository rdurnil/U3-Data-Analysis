
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
    # 1. what is the type of the attribute?
    # e.g. how is it stored?
    # int, float, str, list, ...
    # 2. what is the attribute's semantic type?
    # e.g. what does the attribute (and its values) represent?
    # domain knowledge!!
    # 3. what is the attribute's measurement scale?
    # categorical vs continuous scales
    # nominal: categories without an inherent ordering
    # ordinal: categories with an inherent ordering

if __name__ == "__main__":
    main()