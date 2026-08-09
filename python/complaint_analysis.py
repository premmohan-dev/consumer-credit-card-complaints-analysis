# Virginia Credit Card Complaints Analysis

# Author: Premsai Mohan
# August 2026

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
complaints = xl("A1:P1124", headers=True)

# =====================================================
# Research Question 1
# Which companies were most frequently associated
# with credit card-related complaints?
# =====================================================

top_companies = complaints["Company"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(12,6))
top_companies.plot(kind="bar", ax=ax)

plt.title("Top 10 Companies by Number of Complaints")
plt.xlabel("Company")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.show()


# =====================================================
# Research Question 2
# What complaint issues occurred most frequently
# among Virginia consumers?
# =====================================================

top_issues = complaints["Issue"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(12,6))
top_issues.plot(kind="bar", ax=ax)

plt.title("Most Common Credit Card Complaint Issues Among Virginia Consumers")
plt.xlabel("Issue")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.show()


# =====================================================
# Research Question 3
# How did complaint volume change over the study period?
# =====================================================

complaints["Date received"] = pd.to_datetime(
    complaints["Date received"]
)

monthly_counts = complaints.groupby(
    complaints["Date received"].dt.to_period("M")
).size()

monthly_counts.index = monthly_counts.index.astype(str)

print(monthly_counts.to_string())

fig, ax = plt.subplots(figsize=(12,6))

monthly_counts.plot(
    kind="line",
    marker="o",
    ax=ax
)

plt.title("Monthly Credit Card-Related Complaints in Virginia")
plt.xlabel("Month")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.show()


# =====================================================
# Research Question 4
# What themes appeared most frequently
# in consumer complaint narratives?
# =====================================================

text = " ".join(
    complaints["Consumer complaint narrative"]
    .fillna("")
    .astype(str)
).lower()

themes = [
    "credit report",
    "credit card",
    "late payment",
    "payment",
    "interest",
    "fees",
    "fraud",
    "identity theft",
    "unauthorized",
    "charges",
    "customer service",
    "credit limit",
    "account closed",
    "billing dispute",
    "dispute"
]

theme_counts = []

for theme in themes:
    theme_counts.append({
        "Theme": theme.title(),
        "Count": text.count(theme)
    })

results = pd.DataFrame(theme_counts)

results = results.sort_values(
    by="Count",
    ascending=False
)

print(results)

fig, ax = plt.subplots(figsize=(12,6))

results.plot(
    x="Theme",
    y="Count",
    kind="bar",
    ax=ax
)

plt.title("Most Common Themes in Consumer Complaint Narratives")
plt.xlabel("Theme")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
