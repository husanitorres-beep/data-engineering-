import pandas as pd
import numpy as np
from data import people

# --- SETUP ---
df = pd.DataFrame(people)

# set_index makes email the row label instead of 0, 1, 2
# useful when email is a unique identifier (like a primary key in SQL)
df.set_index("email", inplace=True)

# --- SLICING ---
# iloc = position based (first 2 rows)
print(df.iloc[0:2])

# loc = label based (only works after set_index)
print(df.loc["mike@email.com"])

# --- FILTERING ---
# OR filter — SQL equivalent: WHERE country = 'USA' OR country = 'Canada'
usa_or_canada = (df["country"] == "USA") | (df["country"] == "Canada")
print(df.loc[usa_or_canada])

# AND filter — SQL equivalent: WHERE country = 'USA' AND salary > 90000
usa_high_salary = (df["country"] == "USA") & (df["salary"] > 90000)
print(df.loc[usa_high_salary, ["first", "salary"]])

# filter by salary threshold
high_salary = df["salary"] > 80000
print(df.loc[high_salary, ["first", "salary"]])

# USA earners above 70000 — show name, country, salary
usa_70k = (df["country"] == "USA") & (df["salary"] > 70000)
print(df.loc[usa_70k, ["first", "country", "salary"]])

# --- SORTING ---
# sort by salary descending
desc_salary = df.sort_values("salary", ascending=False)
print(desc_salary)

# sort by country A-Z, then salary high to low within each country
sort_country_salary = df.sort_values(
    by=["country", "salary"],
    ascending=[True, False]
)
print(sort_country_salary)

# -- UPDATING ROWS ---
# update a specific row — SQL equivalent: UPDATE table SET salary = 95000 WHERE email = 'mike@email.com'
df.loc["mike@email.com", "salary"] = 95000

# -- ADDING COLUMNS ---
# combine first and last into full name
df["full_name"] = df["first"] + " " + df["last"]
print(df["full_name"])

# --- GROUPING & AGGREGATING ---
# average salary per country — SQL equivalent: SELECT country, AVG(salary) FROM df GROUP BY country
avg_salary = df.groupby("country")["salary"].mean()
print(avg_salary)

# median salary per country sorted highest to lowest
median_salary = df.groupby("country")["salary"].median().sort_values(ascending=False)
print(median_salary)

# count of rows — SQL equivalent: SELECT COUNT(*) FROM df
print(df["salary"].count())

# distribution of a categorical column — good for yes/no columns
# print(df["hobbyist"].value_counts())

# --- CONCAT (adding rows) ---
# SQL equivalent: UNION ALL
new_people = {
    "first": ["lara", "johnny"],
    "last": ["Smith", "marks"],
    "email": ["lara@email.com", "johnny@email.com"],
    "salary": [8000000, 80000],
    "country": ["USA", "Europe"]
}
df2 = pd.DataFrame(new_people).set_index("email")
combined = pd.concat([df, df2])
print(combined)

# --- STRING FILTERING ----
# str.contains = SQL equivalent of LIKE '%value%'
# percentage of people per country who use Python
# True = 1, False = 0, so .mean() gives a proportion, * 100 gives percentage
percentage_python = (
    df.groupby("country")["languagesworkedwith"]
    .apply(lambda x: x.str.contains("Python", na=False).mean() * 100)
)
print(percentage_python)

# percentage of people per country who use JavaScript
percentage_javascript = (
    df.groupby("country")["languagesworkedwith"]
    .apply(lambda x: x.str.contains("JavaScript", na=False).mean() * 100)
)
print(percentage_javascript)
filter = (df["country"] == "Canada") | (df["salary"] > 90000)
print(df.loc[filter , ["first", "salary" , "country"]])

df.groupby["salary_level] df.count()