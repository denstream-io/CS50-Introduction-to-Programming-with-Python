last, first, house = [row.strip("r\"").strip(" ") for row in row]
, quoting=csv.QUOTE_NONE



name, house = row
last, first = name.strip("\"\"").strip(" ").split(",")