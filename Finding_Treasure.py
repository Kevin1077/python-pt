line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter the posiiton to hide your treasure:'a-c''1-3'")
# Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter=position[0].lower()
alph=["a","b","c"]
ind=alph.index(letter)
num=int(position[1])-1
map[num][ind]="X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")