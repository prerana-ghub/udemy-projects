names = ["A", "B", "C"]
print(names[1])
 
sports = ["Cricket", "Tennis", "Badminton"]
sports[1] = "Football"
 
num = [1,2,3,4,5,6,7]
del num[4]
 
num1 = [1,2,3]
num2 = [4,5,6]
nums = num1 + num2
 
num = [1,2,3,4,5]
print(max(num))
print(min(num))
print(len(num))
 
students = {"A":50, "B":70,"C": 80}
print(students["B"])
 
random = {"A":50, "B":70,"C": 80}
del random["B"]

random = {"A":50, "B":70,"C": 80}
print(random.keys)
print(random.values)
 
movies = ("Interstellar", "X-men", "Avengers")
print(movies)
 
items = (1,2,3,4,5)
print(items[0:2])