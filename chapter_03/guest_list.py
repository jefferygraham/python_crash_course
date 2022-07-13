guest_list = ['Jelani', 'Aunt Betty', 'Pop-Pop']
msg = "I'd like to invite you to dinner."
print(f"{guest_list[0]}, {msg}")
print(f"{guest_list[1]}, {msg}")
print(f"{guest_list[2]}, {msg}")

print(f"\nSorry, {guest_list[2]} can't make it.")
guest_list[2] = "Uncle Billy"
print(f"{guest_list[0]}, {msg}")
print(f"{guest_list[1]}, {msg}")
print(f"{guest_list[2]}, {msg}")

print("\nWe got a bigger table!")
guest_list.insert(0, 'Melanie')
guest_list.insert(2, 'Uncle Mac')
guest_list.append('Aunt Kay')
print(f"{guest_list[0]}, {msg}")
print(f"{guest_list[1]}, {msg}")
print(f"{guest_list[2]}, {msg}")
print(f"{guest_list[3]}, {msg}")
print(f"{guest_list[4]}, {msg}")
print(f"{guest_list[5]}, {msg}")

print("\nSorry, I can only invite 2 people.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, I have to rescind my invitation.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, I have to rescind my invitation.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, I have to rescind my invitation.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, I have to rescind my invitation.\n")

print(f"{guest_list[0]}, you're still invited.")
print(f"{guest_list[1]}, you're still invited.")

del guest_list[:]
print(guest_list)