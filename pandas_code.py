import pandas as p
data={'name':['umesh','surya','kiran'],'age':[20,21,21],'city':['raj','mahen','radvarm'],'subject':['ece','cse','eee']}
df=p.DataFrame(data)
print(df)

#Loading data from csv file 
url='https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
covid_data=p.read_csv(url)
print("Top data \n\n",covid_data.head()) #head means top data
print("End data \n\n",covid_data.tail()) #end data 
print("End data \n\n",covid_data) #Total data 
print("End data \n\n",covid_data.tail()) #end data 
df1=p.DataFrame(covid_data)
print(df1)
death_people=df1[df1['Deaths']<2000]
print(death_people)
