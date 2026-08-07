# Company Complaint Analysis

Research Question:
Which companies received the most credit card complaints from Virginia consumers?

Method:
The complaint dataset was loaded into a Pandas DataFrame, and complaint counts were calculated using the Company field.

Python Code:

complaints = xl("A1:P1124", headers=True)

complaints["Company"].value_counts().head(10)
