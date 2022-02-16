 import pandas as pd
 
 def return_column_headers(data_sheet, print_columns=False):
 """
    Reads the data of an excel sheet and returns the names of each column. 
    Optionally prints all names in the console in new lines.
    
    Args:
        data_sheet : Excel sheet data
        print_columns (optional): should names be printed in the console
    Returns:
        returns the names of each column as a list
 """
    b = pd.read_excel(data_sheet)
    column_headers = list(b.columns.values)
    if print_columns:
        print("\n".join(column_headers))
    return column_headers