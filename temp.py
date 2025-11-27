import sys
if len(sys.argv)==2:
  script_name(sys.argv)
  print("Usage:python temperature_alert.py <temperature-in_C>")
    sys.exist(1)
else:
    temp=float(sys.argv[1])
expect ValueError:
    print("Please enter a valid temperature!")
    sys.exist(1)
if temp <15:
  print("Cold")
elif 15<=temp<=30:
   print("Normal")
else:
  print("Hot")
