# Virginia Consumer Credit Card Complaints Analysis

## Overview

This analysis examines 1,000+ credit card-related complaints submitted by Virginia consumers to the Consumer Financial Protection Bureau (CFPB) between August 2025 and August 2026. The goal is to identify trends and patterns in consumer complaints to better understand the issues Virginia consumers experience with credit card products and services and the companies most frequently associated with those concerns.

## Objectives

The objectives of this analysis are to:

- Identify the companies most frequently associated with credit card-related complaints from Virginia consumers.
- Determine the most common complaint issues and categories reported to the CFPB.
- Analyze how complaint volume changed over the study period.
- Examine complaint narratives to identify recurring themes and consumer concerns.

## Dataset

Source: Consumer Financial Protection Bureau (CFPB) Consumer Complaint Database

Filters applied:
- Product: Credit Card
- State: Virginia (VA)
- Date Received: August 2, 2025 - August 2, 2026
- Complaints with consumer narratives only

Total records: 1,123

## Research Questions

1. Which companies were most frequently associated with credit card-related complaints from Virginia consumers?
2. What complaint issues occurred most frequently among Virginia consumers?
3. How did complaint volume change over the study period?
4. What themes appeared most frequently in consumer complaint narratives?

## Results

## Research Question 1

### Which companies received the most credit card complaints from Virginia consumers?

<img width="976" height="485" alt="top_companies" src="https://github.com/user-attachments/assets/b48844fd-b961-4cbb-a0c3-620a007d04f6" />

### Key Findings

CITIBANK, N.A. received the highest number of credit card-related complaints from Virginia consumers, with approximately 130 complaints during the time period. EQUIFAX, INC., Experian Information Solutions Inc., and Capital One Financial Corporation each received more than 100 complaints. Complaint totals dropped noticeably after these top four companies, with most of the remaining organizations receiving fewer than 80 complaints. This suggests that consumer complaints were concentrated among a relatively small group of companies.

## Research Question 2

### What complaint issues occurred most frequently among Virginia consumers?

<img width="1202" height="591" alt="top_issues" src="https://github.com/user-attachments/assets/ef3af21a-19e9-40d7-8ae0-ea3013c24ba2" />

### Key Findings

Complaints related to purchases shown on consumer statements were the most frequently reported issue, with 299 complaints. Incorrect information on credit reports followed closely behind with 264 complaints. These two categories accounted for a large share of all complaints submitted during the study period. Concerns involving account features, fees or interest charges, and credit card applications were also reported but at much lower rates.

## Research Question 3

### How did complaint volume change over the study period?

<img width="1189" height="590" alt="monthly_complaints" src="https://github.com/user-attachments/assets/170c01bd-27de-419b-97f8-5c56bbea486b" />

Virginia consumers submitted the most complaints in September 2025 (194 complaints) and October 2025 (189 complaints). After that, complaint volume generally decreased, although there was a small increase during the spring of 2026. By the end of the study period, monthly complaint totals had dropped to 32 complaints in June and 9 complaints in July. Overall, complaints were more common during the beginning of the study period than at the end.

## Research Question 4

### What themes appeared most frequently in consumer complaint narratives?

<img width="1190" height="590" alt="common_themes" src="https://github.com/user-attachments/assets/2cb6e833-0ac1-40d5-adfd-075c5faaf135" />

Payment issues were the most common topic discussed in consumer complaints, with 1,741 mentions. Consumers also frequently mentioned disputes (1,071), credit cards (850), fraud (598), and charges (503). These results show that many complaints involved payment problems, billing disputes, and concerns about fraudulent activity. The themes found in the complaint narratives were similar to the issues identified in the earlier parts of the analysis.

## Methods

- Data filtering and preparation
- SQL-based data exploration
- Statistical analysis using Python
- Data visualization and reporting

## Tools and Technologies

- SQL
- Python
- Pandas
- Matplotlib
- Microsoft Excel
- Microsoft Access
- Github

## SQL Analysis

The SQL queries included in this project can be used to analyze the CFPB complaint dataset in Microsoft Access. These queries support the same research questions explored in the Python analysis, including identifying the companies and complaint issues most frequently reported by Virginia consumers and tracking complaint volume over time. For the complaint narrative analysis, SQL was used to retrieve complaint narratives, while Python was used to identify recurring themes within the text.

## Conclusion

This analysis examined 1,000+ credit card-related complaints submitted by Virginia consumers to the CFPB between August 2025 and August 2026. The results showed that complaints were concentrated among a small group of companies and were most often related to purchase disputes, credit reporting issues, and payment problems. Common themes found in complaint narratives included disputes, fraud, charges, and account management concerns. Overall, the project provides a clearer picture of the issues Virginia consumers reported most often during the study period.

## How to Use This Project

1. Review the `Consumer Complaints.xlsx` dataset located in the `data` folder. This is the dataset used throughout the analysis.
   > **Note:** Alternative datasets can be obtained from the CFPB Consumer Complaint Database using different filters. Results may vary depending on the selected data. To run the SQL queries exactly as written, import the dataset into Microsoft Access and create a table named `ConsumerComplaints`.
2. Run the SQL queries in the `sql` folder to explore complaint trends and patterns.
3. Execute the Python analysis in the `python` folder to generate summary statistics, visualizations, and narrative theme analysis.
4. Review the generated charts, tables, and findings to identify common complaint issues, company trends, complaint volume patterns, and recurring narrative themes.
