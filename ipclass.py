def ipv4(ip):
  ip = []
  ips = int(input('Enter Ip'))
  ip.append(ips)
  if(ip[0] >= 0 and ip[0] <= 127):
    return "A"
   
  elif(ip[0] >=128 and ip[0] <= 191):
    return "B"
   
  elif(ip[0] >= 192 and ip[0] <= 223):
    return "C"
   
  elif(ip[0] >= 224 and ip[0] <= 239):
    return "D"
   
  else:
    return "E"

   