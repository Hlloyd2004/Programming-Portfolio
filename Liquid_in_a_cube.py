width = int(input("What is the width of your box in centimeters?\n"))
height = int(input("What is the height of your box in centimeters?\n"))
depth = int(input("What is the depth of your box in centimeters?\n"))
# These variables are the measurements of the box

volume_in_centimeters = (width * height * depth)
#This line calculates the volume of the box in centimeters

volume_in_litres = str(volume_in_centimeters / 1000) # I used the previous calculation to work out the volume in litres
print("The volume of the box in litres is " + volume_in_litres)
# In this line I have concatenated the strings togeather