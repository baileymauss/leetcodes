# DataFrame report
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | product     | object |
# | quarter_1   | int    |
# | quarter_2   | int    |
# | quarter_3   | int    |
# | quarter_4   | int    |
# +-------------+--------+
# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
     var_name="quarter", value_name='sales')