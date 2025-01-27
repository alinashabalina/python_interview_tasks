import re

import numpy as np
import pandas as pd

# the file is added to .gitignore
file_raw = 'test.xlsx'
df = pd.read_excel(file_raw)

# delete the emails that are not unique
unique_email = np.unique(df['email1'].to_numpy())

# clean the data appending only valid emails (according to the regex)
regex = (r"^((([!#$%&'*+\-/=?^_`{|}~\w])|([!#$%&'*+\-/=?^_`{|}~\w][!#$%&'*+\-/=?^_`{|}~\.\w]{0,}[!#$%&'*+\-/=?^_`{"
         r"|}~\w]))[@]\w+([-.]\w+)*\.\w+([-.]\w+)*)$")

clean_data = []
for email in unique_email:
    if re.search(regex, email):
        clean_data.append(email)
