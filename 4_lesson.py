#data = []  #Homework1
#for i in range(3):
#    first_name = input(f"Enter first name of customer {i + 1}: ")
#    last_name = input(f"Enter last name of customer {i + 1}: ")
#    age = input(f"Enter age of customer {i + 1}: ")
#    data.append([first_name, last_name, age])
#index = int(input("Enter the index of the customer to display (0-2): "))
#if 0 <= index < len(data):
#    selected_customer = data[index]
#    print(f"Name: {selected_customer[0]}, last name: {selected_customer[1]}, age: {selected_customer[2]}")
#else:
#    print("Invalid index. Please enter a number between 0 and 2.")

#Homework2

#actors = [
#    {"first_name": "Ia", "last_name": "Sukhitashvili", "age": 41,
#     "movies": ["Begggining","Keep smiling","Tbilisi, I love you",]},
#   {"first_name": "Leonardo", "last_name": "DiCaprio", "age": 48,
#     "movies": ["The Basketball Diaries", "Revolutionary Road", "What's Eating Gilbert Grape",]},
#    {"first_name": "kakha", "last_name": " kintsurashvili", "age": 38,
#     "movies": ["Tiflis", "The Enemies", "Gamopituli khalkhi",]}
#]
#def search(actor_name):
#    for actor in actors:
#        if actor_name.lower() in [actor["first_name"].lower(), actor["last_name"].lower()]:
#            print(f"{actor["first_name"]}{actor["last_name"]} - age:{actor["age"]}")
#            print("Movies:")
#           for movie in actor["movies"]:
#                print("-",movie)
#            return
#    print("Actor not found.")
#actor_name = input("Enter actor's first or last name: ")

#search(actor_name)

#homework4
#def set_to_tuple(set1, set2):
#   combined_set = set1.union(set2)
#    combined_tuple = tuple(combined_set)
#    return combined_tuple

#set1 = {1, 2, 3}
#set2 = {3, 4, 5}
#result = set_to_tuple(set1, set2)
#print(result)

#homework6
#def str_to_dict (string):
#    for i in string:
#        if i in dict:
#            dict[i]+=1
#        else:
#           dict[i]=1
#     return dict
#print(str_to_dict('w3schools'))









