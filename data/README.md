TASK 1 : parse_csv.py (contains the raw code)
mynewfile.csv (is the output of parse_csv.py)
Instructions:
Soul Foods has provided you with three CSV files, all of which are in the data folder of the starter repo you cloned in the last task. These CSV files contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. Take a moment to acquaint yourself with the data contained in each one of these files.

Next, we’ll go field by field and think about how we can use each one:
The first field, “product”, contains many different types of morsels. Soul Foods is only interested in Pink Morsels, so we can remove any row which contains another type of product.
Next come “quantity” and “price”. Since we’re interested in the total sales for a given day, these can be combined into a single field, “sales,” by multiplying them together.
The date field is useful as is and can remain untouched.
It would be nice to filter by region in the final visualisation, so we’ll also leave the region field untouched.

Your task is to use the above instructions to convert the three CSV files into a single formatted output file. Your output file should contain three fields:
Sales
Date
Region