# Tabelas-de-UCs-Unifesp
Modern approach of the display and automatization of the subjects from the Federal University of São Paulo 

This script reads the file Materias-Unifesp-1.pdf which is an table with all the subjects from 
the Science and Technology Bachelor degree and convert into a .csv format using 
[tabula-py](https://github.com/chezou/tabula-py)
library. Then it manipulates this .csv file in a dataframe with 
[pandas](https://github.com/pandas-dev/pandas) to modify the generated table. 

After that, there's
a comparison between the elements from the dataframe with a file that contains the classes that 
will take place in the follow semester, file  and adds to our table if it's available in the 
correspondent semester with the usage of [openpyxl](https://openpyxl.readthedocs.io/en/stable/)


## Installation:

## This script only needs python libraries, listed inside *requirements.txt*
## Required libraries:
All required libraries can be installed using pip, through the following command:
 
    pip install -r requirements.txt

**It's highly recommended to use Python Virtual Environments.**




