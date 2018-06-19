def ground_shipping(weight):
  if weight <= 2:
    return 20.00 + (weight * 1.50)
  elif (weight > 2) and (weight <= 6):
    return 20.00 + (weight * 3.00)
  elif (weight > 6) and (weight <= 10):
    return 20.00 + (weight * 4.00)
  else:
  	return 20.00 + (weight * 4.75)
print(ground_shipping(8.4))

p_g_s = 125

def drone_shipping(weight):
  if weight <= 2:
    return (weight * 4.50)
  elif (weight > 2) and (weight <= 6):
    return (weight * 9.00)
  elif (weight > 6) and (weight <= 10):
    return (weight * 12.00)
  else:
  	return (weight * 14.25)
 
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < p_g_s:
  	return "Ground shipping is cheapest method. It will cost " + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < p_g_s:
    return "Drone shipping is cheapest method. It will cost " + str(drone_shipping(weight))
  else:
  	return "Premium ground shipping is the cheapest. It will cost " +str(p_g_s)
  
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))



  