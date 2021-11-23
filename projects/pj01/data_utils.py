"""data_utils to be used for Project 01."""

__author__ = "730397680"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open ahandle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_based: dict[str, list[str]], amount: int) -> dict[str, list[str]]:
    """A function where a column_based data table is sent in with the amount of rows you want displayed from the table."""
    table: dict[str, list[str]] = {}
    for rows in column_based:
        i: int = 0
        n_values: list[str] = []
        if amount >= len(column_based[rows]):
            return column_based
        while i < amount:
            n_values.append(column_based[rows][i])
            i += 1
        
        table[rows] = n_values
    return table


def select(non_mutated_column: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """A function where only the a sepcific subset of the original columns will be produced in a new column-based table."""
    new_table: dict[str, list[str]] = {}
    for column in column_names:
        new_table[column] = non_mutated_column[column]

    return new_table


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """A function where a new column_based table will be produced with the combination of two_column based tables."""
    new_table: dict[str, list[str]] = {}
    for column in first_table:
        new_table[column] = first_table[column]
    for column in second_table:
        if column in new_table:
            new_table[column] += second_table[column]
        else:
            new_table[column] = second_table[column]
    
    return new_table


def count(frequencies: list[str]) -> dict[str, int]:
    """A function where the amount of times a value appears in the input list."""
    new_table: dict[str, int] = {}
    for item in frequencies:
        if item in new_table:
            new_table[item] += 1
        else:
            new_table[item] = 1
    
    return new_table