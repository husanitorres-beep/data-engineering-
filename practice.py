

#i learnt slicing ex. -> df.loc[0:2, "hobbyist": "employment"]
#i learnt df.set_inde("email", inplace = True) idk what it does 
# this seems to work for real work scenearios -> high_salary = print(df ["salary"] > 70000)
#^ print(df.loc["high_salary", ["country", "prgramworkedwith", "salary"]])  --> try to recall what would be shown and what it will do 
#filter is very immportant 
#updating rows 
#adding and removing colmns, Ex. ->  df["first"] + ' ' + df["last"]
#adding and removing rows, Ex. ->
#sort by 
#grouping and aggreagting 


import pandas as pd 
from data import people 

df = pd.DataFrame(people)
#df.set_index("email", inplace=True)

print(df)
# print(df["email"])     
print(df.iloc[0:2])          

filter = (df["country"] == "USA") | (df["country"] == "Canada")
print(df.loc[filter])



filter = df["salary"] > 80000
print(df.loc[filter, ["first", "salary"]])

#print(df.loc["mike@email.com"]) 
 
filter = (df["country"] == "USA") &  (df["salary"] > 90000)
print(df.loc[filter , ["first" , "salary"]])

desc_salary = df.sort_values("salary" , ascending = False) 
print(desc_salary)
 
df.loc[0, "salary"] = 95000 
print(df)

average_salary = df.groupby("country")["salary"].mean()
print(average_salary)

first_last = df["first"]+" " + df["last"]
print(first_last)

people = {
    "first": ["lara", "jhonny"],
    "last": ["Smith", "marks"],
    "email": ["lara@email" , "jhonny@email"],
    "salary" : [8000000 , 80000 ],
    "country" : ["USA" , "Europe"]
}
df2 = pd.DataFrame(people)
print(df2)
combined = pd.concat([df, df2], ignore_index=True)
print(combined)
sort = df2.sort_values(by = "last")
print(sort)

#sort
sort_country_salary = df.sort_values(
    by=["country", "salary"],
    ascending=[True, False]
)
print(sort_country_salary)

#grouping and aggreagting, value_count important


print(df2["salary"].count())


#this is something i cant do beacuse i dont have the datascheme but this is some overview of what certain code can do 
#df["salary"].median 
#df.describe ->  gives us valuable math kind data 
#df.["salary"].count() -> this gives us the count(amount) of peopele who answered the salry question if we had the data scheeme file
#df["hobbies"].values_counts() -> for this one its "yes" or "no" questions meaning this will coutn the amount of yes's and no's (dosnt have to be)
#country_grp = df.groupby(["country"])
#country_grp.get_group("USA") -> we get results of only "USA" salry, hobbies etc.. 
#filt = df["country"] == "USA"
    #  ^ df.loc[filt]["socialmedia"].value_counts() collumn 84 and 85 has a code where we get the most popular apps in the "USA"
#country_grp["socialmedia"].value_counts().loc["india"] -> we get the most popular websites from each country if we didnt add "loc.india"
#country_grp["salary"].median -> we get median slary from each country 
#filt = df["country"]
    #df.loc[filt]["languagesworkedwith"].str contains("python").sum() 88 - 89 grab those people that either use or do not use pyton 
#he also did a problem where he gets the percentage of people that know python in each country 
#percentage_of_python = df.groupby("country")["languagesworkedwith"].str.contains("Python").mean() * 100
filter = (df["country"] == "USA") & (df["salary"] > 70000) 
print(df.loc[filter , ["first" , "country", "salary"]])
median_salary = df.groupby("country")["salary"].median().sort_values(ascending=False)
print(median_salary)

java_users = df.groupby("country")["languagesworkedwith"].str.contains("java").mean()