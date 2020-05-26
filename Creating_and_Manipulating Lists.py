#A list is created by using brackets [] and separating each element with commas
program_languages=["Python","Java","C++","C#"]
#We can use the command TYPE() to verify that program_languages is a list
print(type(program_languages))
#To know how many elements have been added to the list we can use the len() command
print("The number of elements of the list is: "+str(len(program_languages)))
#If we prefere to show all the list, we can do it by executing a print command
print(program_languages)


#We can show only the first element of the list by using its index
print(program_languages[0])
#We can show only the last element of the list by using the index -1
print(program_languages[-1])

#If we prefere to change an element by its index, we can use this command
program_languages[1]="GO"
#Let's check the change
print(program_languages)
