# Import your libraries
import pandas as pd

# Start writing code
submissions['total']=submissions.groupby('rate_type')['balance'].transform('sum')

submissions['p'] = submissions['balance']/submissions['total']

submissions
