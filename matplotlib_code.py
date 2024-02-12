import matplotlib as m
import matplotlib.pyplot as mplot

x=[1,2,3,4,4,5]
y=[1,2,3,4,4,5]
mplot.plot(x,y)
mplot.xlabel('X-axis')
mplot.ylabel('y-axis ')
mplot.title('Y=2x')
mplot.show()


#Scatter plot
x1=[1,2,3,4,5]
y2=[1,2,3,4,5]
mplot.scatter(x1,y2,color='red',marker='o')
mplot.xlabel('x')
mplot.ylabel('y')
mplot.title("Surya Kiran")
mplot.show()

#bar chat 
categories=['Physics','Maths','Drawing','Devices','ET']
vaules=[60,30,45,78,12]
mplot.xlabel('categories')
mplot.bar(categories,vaules,color='red')
mplot.ylabel('vaules')
mplot.title('Bar chat')
mplot.show()  

#Histogram
data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5]
mplot.hist(data,bins=7,color='blue',edgecolor='black')
mplot.hist(data,bins=10,color='red',edgecolor='black')
mplot.xlabel('values')
mplot.ylabel('Histogram')
mplot.title('Hisogram')
mplot.show()


#pie chat
mplot.pie(vaules,labels=categories,autopct='%d%%',startangle=90,colors=['blue','pink','blue','red','white'])
mplot.pie(vaules,labels=categories,autopct='%5.2f%%',startangle=90,colors=['blue','pink','blue','red','white'])
mplot.axis('equal')
mplot.show()



#Exploded pie chat 
explode=(0.7,0.7,0.7,0.7,0.7)
mplot.pie(vaules,labels=categories,autopct='%1.1f%%',startangle=90,explode=explode,colors=['blue','pink','blue','red','white'])
mplot.pie(vaules,labels=categories,autopct='%1.1f%%',startangle=90,colors=['blue','pink','blue','red','white'])
mplot.axis('equal')
mplot.show()


