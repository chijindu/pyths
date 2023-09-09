guests = ["Chidy", "Vivy", "Pedro", "Nono m", "Seun"]

def guestList( friends = []):
    for i in range(len(friends)):
        message = f"You are invited to dinner {friends[i].upper()}."
        print(message)

#jin = guestList(guests)

message = f"Unfortunately {guests[2]} can't make it to the dinner"

print(message)

guests[2] = "Ofor"

print(guestList(guests))

print("Just found a bigger dinner Table..")

guests.insert(0, "Jindu")
guests.insert(2, "Bobo")
guests.append("Onyi")

print(guestList(guests))

print(guests[:])

print("The first 3 elements in the guest list is:")

print(guests[:3])
print("The 3 names from the middle is: ")
print(guests[3: 6])
print("The last 3 names from the list is: ")
print(guests[:3])

boboguests = guests[:]
boboguests.append("Api")
guests.append("Amara")
print(guests)
print(boboguests[:])

print(guests[0] == "Jindu")
