from Color.Color import Color

person = input("Which person?")
room = input("Which room?")
print("person"+person)
print("room"+room)
#print(type(person))
#print(type(room))
huelight1 = Color("Hue_1")
huelight2 = Color("Hue_2")

data1='100,100,100'
data2='50,50,50'

if room=="1":
	if person=="1":
		print("Room1  Person1")
		huelight1.postData(data1)
	else:
		print("Room1  Person2")
		huelight1.postData(data2)
else:
	if person=="1":
		print("Room2  Person1")
		huelight2.postData(data1)
	else:
		print("Room2  Person2")
		huelight2.postData(data2)

