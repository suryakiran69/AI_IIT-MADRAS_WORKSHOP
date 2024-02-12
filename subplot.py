import matplotlib.pyplot as plt
categories=['Physics','Maths','Drawing','Devices','ET']
vaules=[60,30,45,78,12]
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,1,1,1,1]
plt.subplot(2,2,1)
plt.pie(vaules,labels=categories,autopct='%d%%',startangle=90,colors=['blue','pink','blue','red','white'])
plt.title('Subplots')
plt.ylabel('Y1-axis')
plt.subplot(2,2,2)
plt.bar(categories,vaules,color='red')
plt.xlabel('X-axis')
plt.ylabel('Y2-axis')
plt.subplot(2,2,3)
plt.plot(x,y1)
plt.subplot(2,2,4)
plt.plot(x,y2)

plt.show()