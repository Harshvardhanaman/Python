# Write a small Python program that:
# Prints your favourite Indian food item on the first output line.
print("My favourite food item is Mutton Pullao")

# Prints the price of that item as a number (not text) on the second output line.
print("Price of meal is", 500)

# Write two separate print() statements that work together to display this exact single-line output on the screen:
# UPI ID: ramesh.kumar@okaxis [VERIFIED]
print("UPI ID: ramesh.kumar", "okaxis", sep="@", end=" ")
print("[VERIFIED]")

# Suppose a junior developer wants to print a Windows folder path and a quote on the screen like this:
# File saved in: C:\new_folder\test.py ("Success")
# They wrote this buggy code: print("File saved in: C:\new_folder\test.py ("Success")")
# Find the two bugs in their line of code.
# Two bugs in this line of code are: \n here it is used as next line. \t used as tab space.
# There should only be one pair of double quote in one line, the moment second " comes it will stop the string.

# Write the corrected print() statement so it outputs the exact line shown above
print("File saved in: C:\\new_folder\\test.py", end=" ")
print("(\"Success\")")

# When backend systems generate thermal bill receipts or terminal logs, they format columns cleanly. Using print(), sep, and \n, write a Python snippet that prints this exact formatted receipt:
# *** ZOMATO ORDER RECEIPT ***
# Order_ID -> ZM9988 -> Delivered
# ----------------------------
# Biryani : Rs. 250
# Raita   : Rs. 50
# ----------------------------
# Total Paid: Rs. 300

print("*** ZOMATO ORDER RECEIPT ***")
print("Order_ID", "ZM9988", "Delivered", sep=" -> ")
print("------------------------------")
print("Briyani :", "Rs.", 250, sep=" ")
print("Raita \t:", "Rs.", 50, sep=" ")
print("------------------------------")
print("Total Paid: Rs.", 300, sep=" ")

# Interview question:
# Is Python a strictly compiled language or a strictly interpreted language?, how would you explain the two steps (.pyc Bytecode and PVM) in 2–3 simple sentences?
# "Python is both compiled and interpreted. 
# When we run a .py file, Python first compiles the source code into intermediate Bytecode (.pyc), and then the Python Virtual Machine (PVM) interprets that bytecode line-by-line into machine code for the CPU."
# Without running it on a computer, predict the exact output of this tricky one-liner and explain why the two sides of the comma behave differently:
# print("50" + "50", 50 + 50, sep=" vs ")
# 5050 vs 100