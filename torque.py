print('calculate the force required to balance a given beam')
print('the input requires :-' "\n" 'forces applied on either side of the beam' "\n" 'their distances from centre of the beam')
print('for the left side of the beam')
left = int(input('specify the number of forces acting on left side of the beam --->'))
force1 = 0
for left in range(left):
  f = int(input('enter the force value -->'))
  d = int(input('enter the distance from centre -->'))
  u = input('enter the direction of force, upwards or downwards (u/d) ---->')
  if u =='u':
    force1 = force1 + (f*d)
  elif u =="d":
    force1 = force1 - (f*d)

print('for right side of beam')
r = int(input('specify the number of forces acting on right side of the beam --->'))
force2 = 0
for r in range(r):
  f = int(input('enter the force value -->'))
  d = int(input('enter the distance from centre -->'))
  u = input('enter the direction of force, upwards or downwards (u/d) ---->')
  if u =='u':
    force2 = force2 + (f*d)
  elif u =="d":
    force2 = force2 - (f*d)
fn = force2 - force1
if fn > 0:
  print('the net torque is', fn, 'upwards on right side')
  ans_dis = int(input('specify the distance to apply balancing force -->'))
  ans = fn/ans_dis
  print('the required force is', ans, 'acting downward on right side of beam')
elif fn < 0:
  print('the net torque is', fn, 'upwards on left side')
  ans_dis = int(input('specify the distance to apply balancing force -->'))
  ans = fn/ans_dis
  print('the required force is', ans, 'acting downward on left side of beam')
else:
  print('beam is balanced')
  exit()

  