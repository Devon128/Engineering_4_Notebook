# Function to determine the area of a triangle 
def triangle_area(x1y1, x2y2, x3y3):
   try:
      # seperate each entry into a list
      x1y1 = x1y1.split(",")
      x2y2 = x2y2.split(",")
      x3y3 = x3y3.split(",")

      # pull coordinates out of each list and change them 

      x1 = float(x1y1[0])
      y1 = float(x1y1[1])
      x2 = float(x2y2[0])
      y2 = float(x2y2[1])
      x3 = float(x3y3[0])
      y3 = float(x3y3[1])

      # caculate area
      area = 0.5*abs(x1*(y2-y3)+x3*(y1-y2))
      return area 

   except:
      print("error")

      area = 0
      return area

# code to run ina loop
while True:
   # request input
   val1 = input("input first set of coords")
   val2 = input("input second set of coords")
   val3 = input("input third set of coords")
   # run function and save output to area variable 
   area = triangle_area(val1, val2, val3)   

   # if error in function, skip printed output and start loop over
   if area == 0:
      continue

   # if no error, print the area message and start loop over 
   else:
      print(area)