import numpy as np
import scipy
import matplotlib.pyplot as plt
import turtle as trtl
import scipy.constants as spc

#turtle window
wn=trtl.Screen()
wn.setup(1200,675,0,1)
wn.bgcolor('black')
wn.title('osu!')

#constant setup, masses in kilograms
mSun = float(1.9891*10**30)
mEarth = float(5.97219*10**24)
mMoon = float(3.4767309*10**22)

G=spc.gravitational_constant
dt=0.001

#kilometers
xEarth = 105781776.869
yEarth = 105781776.869
angleEarth=np.arctan(yEarth/xEarth)

xMoon = 105781776.869 + np.sqrt(2*286661**2)
yMoon = 105781776.869 - np.sqrt(2*286661**2)

#turtle setup
Earth=trtl.Turtle()
Earth.penup()
Earth.color('blue')
Earth.turtlesize(.5,.5)
Earth.shape('circle')
Earth.speed(0)
Earth.goto(xEarth*10**-6,yEarth*10**-6)
Earth.pendown()
#Earth.hideturtle()

Sun=trtl.Turtle()
Sun.penup()
Sun.color('Yellow')
Sun.turtlesize(2,2)
Sun.shape('circle')

Moon=trtl.Turtle()
Moon.penup()
Moon.color('grey')
Moon.shape('circle')
Moon.turtlesize(.25,.25)
Moon.speed(0)
Moon.goto(xMoon*10**-6,yMoon*10**-6)
Moon.pendown()


#v=sqrt(ac/r)

aSEarth=-G*mSun/(xEarth**2+yEarth**2)
#v0Earth=float(27.7827)
v0Earth=float((-aSEarth*((xEarth**2+yEarth**2)**(1/2)))**(1/2))
vxEarth=-v0Earth*np.cos(angleEarth)
vyEarth=v0Earth*np.sin(angleEarth)


aSMoon=-G*mSun/(xMoon**2+yMoon**2)
#aSMoon=0
aEMoon=-G*mEarth/((xMoon-xEarth)**2+(yMoon-yEarth)**2)

v0Moon=float(((-aSMoon)*((xMoon**2+yMoon**2)**(1/2)))**(1/2)+((-aEMoon)*(((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2)))**(1/2))*1.00
vxMoon=v0Moon*np.cos(angleEarth+np.pi/2)
vyMoon=v0Moon*np.sin(angleEarth)

#vxMoon=v0Moon*(xMoon/(xMoon**2+yMoon**2)**(1/2))
#vyMoon=v0Moon*(yMoon/(xMoon**2+yMoon**2)**(1/2))

print(aEMoon)

for i in range (0,100000000):
  #moving the Earth
  aSEarth=-G*mSun/(xEarth**2+yEarth**2)
  aMEarth=-G*mMoon/((xMoon-xEarth)**2+(yMoon-yEarth)**2)
  axEarth=aSEarth*(xEarth/(xEarth**2+yEarth**2)**(1/2))+aMEarth*((xMoon+xEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2))
  ayEarth=aSEarth*(yEarth/(yEarth**2+yEarth**2)**(1/2))+aMEarth*((yMoon+yEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2))
  vxEarth=vxEarth+axEarth*dt
  vyEarth=vyEarth+ayEarth*dt
  xEarth=xEarth+vxEarth*dt
  yEarth=yEarth+vyEarth*dt

  #if the Earth goes too far, it bounces back
  if abs(xEarth) >= 6*10**8:
    vxEarth = vxEarth*-1 
  if abs(yEarth) >= 3.2*10**8:
    vyEarth = vyEarth*-1
  

  #moving the Moon
  aSMoon=-G*mSun/(xMoon**2+yMoon**2)
  aEMoon=-G*mEarth/((xMoon-xEarth)**2+(yMoon-yEarth)**2)
  axMoon=aSMoon*(xMoon/(xMoon**2+yMoon**2)**(1/2))+aEMoon*((xMoon-xEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2))
  ayMoon=aSMoon*(yMoon/(xMoon**2+yMoon**2)**(1/2))+aEMoon*((yMoon-yEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2))
  vxMoon=vxMoon+axMoon*dt
  vyMoon=vyMoon+ayMoon*dt
  xMoon=xMoon+vxMoon*dt
  yMoon=yMoon+vyMoon*dt

  #if the Moon goes too far, it bounces back
  if abs(xMoon) >= 6*10**8:
    vxMoon = vxMoon*-1 
  if abs(yMoon) >= 3.2*10**8:
    vyMoon = vyMoon*-1

  #drawing the Earth and Moon every 20 loops
  if i%20000 == 0:
    Earth.goto(xEarth*10**-6,yEarth*10**-6)
    Moon.goto(xMoon*10**-6,yMoon*10**-6)
    Sun.showturtle()
  if i == 1:
    print(aEMoon)
  #print(aEMoon*((xMoon-xEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2)))
  #print(aEMoon*((yMoon-yEarth)/((xMoon-xEarth)**2+(yMoon-yEarth)**2)**(1/2)))
  #print(yEarth)

  


wn.mainloop()


