# import the required modules
import tabula
from openpyxl import load_workbook
import pandas as pd
from pandas.api.types import is_string_dtype

# read a pdf file
df = tabula.read_pdf('historic_unifesp_sis.pdf', pages="all", encoding='utf-8', lattice=True)[0]
print(df.to_string())

#convert PDF into CSV format
#tabula.convert_into('historic_unifesp.pdf', 'requriments_subject-page-1.csv', output_format='csv', pages='all')