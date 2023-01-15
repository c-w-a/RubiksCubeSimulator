
# WRITTEN BY: Chris W Anglin

import matplotlib.pyplot as plt
import numpy as np
from cubelogic import *

# PLOT SETUP / SETTINGS
plt.style.use('seaborn-v0_8-notebook')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_axis_off()
ax.view_init(elev=23, azim=-119)

# CREATE cube OBJECT
cube = Cube(scrambled=False)

# LINE-WIDTH FOR EDGE OF FACES
lw = 3.3

# RED SIDE FACES (front)
r0x = np.array([0.04, 0.04, 0.96, 0.96])
r0y = np.array([0, 0, 0, 0])
r0x, r0y = np.meshgrid(r0x, r0y)
r0z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(-1, 1)

r1x = np.array([1.04, 1.04, 1.96, 1.96])
r1y = np.array([0, 0, 0, 0])
r1x, r1y = np.meshgrid(r1x, r1y)
r1z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(-1, 1)

r2x = np.array([2.04, 2.04, 2.96, 2.96])
r2y = np.array([0, 0, 0, 0])
r2x, r2y = np.meshgrid(r2x, r2y)
r2z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(-1, 1)

r3x = np.array([0.04, 0.04, 0.96, 0.96])
r3y = np.array([0, 0, 0, 0])
r3x, r3y = np.meshgrid(r3x, r3y)
r3z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(-1, 1)

r4x = np.array([1.04, 1.04, 1.96, 1.96])
r4y = np.array([0, 0, 0, 0])
r4x, r4y = np.meshgrid(r4x, r4y)
r4z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(-1, 1)

r5x = np.array([2.04, 2.04, 2.96, 2.96])
r5y = np.array([0, 0, 0, 0])
r5x, r5y = np.meshgrid(r5x, r5y)
r5z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(-1, 1)

r6x = np.array([0.04, 0.04, 0.96, 0.96])
r6y = np.array([0, 0, 0, 0])
r6x, r6y = np.meshgrid(r6x, r6y)
r6z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(-1, 1)

r7x = np.array([1.04, 1.04, 1.96, 1.96])
r7y = np.array([0, 0, 0, 0])
r7x, r7y = np.meshgrid(r7x, r7y)
r7z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(-1, 1)

r8x = np.array([2.04, 2.04, 2.96, 2.96])
r8y = np.array([0, 0, 0, 0])
r8x, r8y = np.meshgrid(r8x, r8y)
r8z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(-1, 1)

# YELLOW SIDE FACES (top)
y0x = np.array([0.04, 0.04, 0.96, 0.96])
y0y = np.array([2.04, 2.04, 2.96, 2.96])
y0x, y0y = np.meshgrid(y0x, y0y)
y0z = np.array([3, 3, 3, 3]).reshape(1, -1)

y1x = np.array([1.04, 1.04, 1.96, 1.96])
y1y = np.array([2.04, 2.04, 2.96, 2.96])
y1x, y1y = np.meshgrid(y1x, y1y)
y1z = np.array([3, 3, 3, 3]).reshape(1, -1)

y2x = np.array([2.04, 2.04, 2.96, 2.96])
y2y = np.array([2.04, 2.04, 2.96, 2.96])
y2x, y2y = np.meshgrid(y2x, y2y)
y2z = np.array([3, 3, 3, 3]).reshape(1, -1)

y3x = np.array([0.04, 0.04, 0.96, 0.96])
y3y = np.array([1.04, 1.04, 1.96, 1.96])
y3x, y3y = np.meshgrid(y3x, y3y)
y3z = np.array([3, 3, 3, 3]).reshape(1, -1)

y4x = np.array([1.04, 1.04, 1.96, 1.96])
y4y = np.array([1.04, 1.04, 1.96, 1.96])
y4x, y4y = np.meshgrid(y4x, y4y)
y4z = np.array([3, 3, 3, 3]).reshape(1, -1)

y5x = np.array([2.04, 2.04, 2.96, 2.96])
y5y = np.array([1.04, 1.04, 1.96, 1.96])
y5x, y5y = np.meshgrid(y5x, y5y)
y5z = np.array([3, 3, 3, 3]).reshape(1, -1)

y6x = np.array([0.04, 0.04, 0.96, 0.96])
y6y = np.array([0.04, 0.04, 0.96, 0.96])
y6x, y6y = np.meshgrid(y6x, y6y)
y6z = np.array([3, 3, 3, 3]).reshape(1, -1)

y7x = np.array([1.04, 1.04, 1.96, 1.96])
y7y = np.array([0.04, 0.04, 0.96, 0.96])
y7x, y7y = np.meshgrid(y7x, y7y)
y7z = np.array([3, 3, 3, 3]).reshape(1, -1)

y8x = np.array([2.04, 2.04, 2.96, 2.96])
y8y = np.array([0.04, 0.04, 0.96, 0.96])
y8x, y8y = np.meshgrid(y8x, y8y)
y8z = np.array([3, 3, 3, 3]).reshape(1, -1)

# BLUE SIDE FACES (left)
b0x = np.array([0, 0, 0, 0])
b0y = np.array([2.04, 2.04, 2.96, 2.96])
b0x, b0y = np.meshgrid(b0x, b0y)
b0z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

b1x = np.array([0, 0, 0, 0])
b1y = np.array([1.04, 1.04, 1.96, 1.96])
b1x, b1y = np.meshgrid(b1x, b1y)
b1z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

b2x = np.array([0, 0, 0, 0])
b2y = np.array([0.04, 0.04, 0.96, 0.96])
b2x, b2y = np.meshgrid(b2x, b2y)
b2z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

b3x = np.array([0, 0, 0, 0])
b3y = np.array([2.04, 2.04, 2.96, 2.96])
b3x, b3y = np.meshgrid(b3x, b3y)
b3z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

b4x = np.array([0, 0, 0, 0])
b4y = np.array([1.04, 1.04, 1.96, 1.96])
b4x, b4y = np.meshgrid(b4x, b4y)
b4z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

b5x = np.array([0, 0, 0, 0])
b5y = np.array([0.04, 0.04, 0.96, 0.96])
b5x, b5y = np.meshgrid(b5x, b5y)
b5z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

b6x = np.array([0, 0, 0, 0])
b6y = np.array([2.04, 2.04, 2.96, 2.96])
b6x, b6y = np.meshgrid(b6x, b6y)
b6z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

b7x = np.array([0, 0, 0, 0])
b7y = np.array([1.04, 1.04, 1.96, 1.96])
b7x, b7y = np.meshgrid(b7x, b7y)
b7z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

b8x = np.array([0, 0, 0, 0])
b8y = np.array([0.04, 0.04, 0.96, 0.96])
b8x, b8y = np.meshgrid(b8x, b8y)
b8z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

# GREEN SIDE FACES (right)
g0x = np.array([3, 3, 3, 3])
g0y = np.array([0.04, 0.04, 0.96, 0.96])
g0x, g0y = np.meshgrid(g0x, g0y)
g0z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

g1x = np.array([3, 3, 3, 3])
g1y = np.array([1.04, 1.04, 1.96, 1.96])
g1x, g1y = np.meshgrid(g1x, g1y)
g1z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

g2x = np.array([3, 3, 3, 3])
g2y = np.array([2.04, 2.04, 2.96, 2.96])
g2x, g2y = np.meshgrid(g2x, g2y)
g2z = np.array([2.04, 2.04, 2.96, 2.96]).reshape(1, -1)

g3x = np.array([3, 3, 3, 3])
g3y = np.array([0.04, 0.04, 0.96, 0.96])
g3x, g3y = np.meshgrid(g3x, g3y)
g3z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

g4x = np.array([3, 3, 3, 3])
g4y = np.array([1.04, 1.04, 1.96, 1.96])
g4x, g4y = np.meshgrid(g4x, g4y)
g4z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

g5x = np.array([3, 3, 3, 3])
g5y = np.array([2.04, 2.04, 2.96, 2.96])
g5x, g5y = np.meshgrid(g5x, g5y)
g5z = np.array([1.04, 1.04, 1.96, 1.96]).reshape(1, -1)

g6x = np.array([3, 3, 3, 3])
g6y = np.array([0.04, 0.04, 0.96, 0.96])
g6x, g6y = np.meshgrid(g6x, g6y)
g6z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

g7x = np.array([3, 3, 3, 3])
g7y = np.array([1.04, 1.04, 1.96, 1.96])
g7x, g7y = np.meshgrid(g7x, g7y)
g7z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

g8x = np.array([3, 3, 3, 3])
g8y = np.array([2.04, 2.04, 2.96, 2.96])
g8x, g8y = np.meshgrid(g8x, g8y)
g8z = np.array([0.04, 0.04, 0.96, 0.96]).reshape(1, -1)

# PLOT ALL FACES
def plot_all():
    r0 = ax.plot_surface(r0x, r0y, r0z, color='#' + cube.front[0][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r1 = ax.plot_surface(r1x, r1y, r1z, color='#' + cube.front[0][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r2 = ax.plot_surface(r2x, r2y, r2z, color='#' + cube.front[0][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r3 = ax.plot_surface(r3x, r3y, r3z, color='#' + cube.front[1][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r4 = ax.plot_surface(r4x, r4y, r4z, color='#' + cube.front[1][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r5 = ax.plot_surface(r5x, r5y, r5z, color='#' + cube.front[1][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r6 = ax.plot_surface(r6x, r6y, r6z, color='#' + cube.front[2][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r7 = ax.plot_surface(r7x, r7y, r7z, color='#' + cube.front[2][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    r8 = ax.plot_surface(r8x, r8y, r8z, color='#' + cube.front[2][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)

    y0 = ax.plot_surface(y0x, y0y, y0z, color='#' + cube.top[0][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y1 = ax.plot_surface(y1x, y1y, y1z, color='#' + cube.top[0][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y2 = ax.plot_surface(y2x, y2y, y2z, color='#' + cube.top[0][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y3 = ax.plot_surface(y3x, y3y, y3z, color='#' + cube.top[1][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y4 = ax.plot_surface(y4x, y4y, y4z, color='#' + cube.top[1][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y5 = ax.plot_surface(y5x, y5y, y5z, color='#' + cube.top[1][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y6 = ax.plot_surface(y6x, y6y, y6z, color='#' + cube.top[2][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y7 = ax.plot_surface(y7x, y7y, y7z, color='#' + cube.top[2][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    y8 = ax.plot_surface(y8x, y8y, y8z, color='#' + cube.top[2][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)

    b0 = ax.plot_surface(b0x, b0y, b0z, color='#' + cube.left[0][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b1 = ax.plot_surface(b1x, b1y, b1z, color='#' + cube.left[0][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b2 = ax.plot_surface(b2x, b2y, b2z, color='#' + cube.left[0][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b3 = ax.plot_surface(b3x, b3y, b3z, color='#' + cube.left[1][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b4 = ax.plot_surface(b4x, b4y, b4z, color='#' + cube.left[1][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b5 = ax.plot_surface(b5x, b5y, b5z, color='#' + cube.left[1][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b6 = ax.plot_surface(b6x, b6y, b6z, color='#' + cube.left[2][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b7 = ax.plot_surface(b7x, b7y, b7z, color='#' + cube.left[2][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    b8 = ax.plot_surface(b8x, b8y, b8z, color='#' + cube.left[2][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)

    g0 = ax.plot_surface(g0x, g0y, g0z, color='#' + cube.right[0][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g1 = ax.plot_surface(g1x, g1y, g1z, color='#' + cube.right[0][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g2 = ax.plot_surface(g2x, g2y, g2z, color='#' + cube.right[0][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g3 = ax.plot_surface(g3x, g3y, g3z, color='#' + cube.right[1][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g4 = ax.plot_surface(g4x, g4y, g4z, color='#' + cube.right[1][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g5 = ax.plot_surface(g5x, g5y, g5z, color='#' + cube.right[1][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g6 = ax.plot_surface(g6x, g6y, g6z, color='#' + cube.right[2][0], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g7 = ax.plot_surface(g7x, g7y, g7z, color='#' + cube.right[2][1], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)
    g8 = ax.plot_surface(g8x, g8y, g8z, color='#' + cube.right[2][2], antialiased=True, edgecolor='black', linewidth=lw, shade=True, rcount=50, ccount=50)

# SCRAMBLE BUTTON LOGIC
def scramble_(event):
    for i in range(77):
        cube.scramble()
    plot_all()
    plt.draw()

# R BUTTON LOGIC
def r_move(event):
    cube.R()
    plot_all()
    plt.draw()

# Ri BUTTON LOGIC
def ri_move(event):
    cube.Ri()
    plot_all()
    plt.draw()

# L BUTTON LOGIC
def l_move(event):
    cube.L()
    plot_all()
    plt.draw()

# Li BUTTON LOGIC
def li_move(event):
    cube.Li()
    plot_all()
    plt.draw()

# F BUTTON LOGIC
def f_move(event):
    cube.F()
    plot_all()
    plt.draw()

# Fi BUTTON LOGIC
def fi_move(event):
    cube.Fi()
    plot_all()
    plt.draw()

# U BUTTON LOGIC
def u_move(event):
    cube.U()
    plot_all()
    plt.draw()

# Ui BUTTON LOGIC
def ui_move(event):
    cube.Ui()
    plot_all()
    plt.draw()

# B BUTTON LOGIC
def b_move(event):
    cube.B()
    plot_all()
    plt.draw()

# Bi BUTTON LOGIC
def bi_move(event):
    cube.Bi()
    plot_all()
    plt.draw()

# D BUTTON LOGIC
def d_move(event):
    cube.D()
    plot_all()
    plt.draw()

# Di BUTTON LOGIC
def di_move(event):
    cube.Di()
    plot_all()
    plt.draw()

# RESET BUTTON LOGIC
def reset_(event):
    cube.reset()
    plot_all()
    plt.draw()

# SCRAMBLE BUTTON
button1_ax = plt.axes([0.05, 0.85, 0.15, 0.075])
button1 = plt.Button(button1_ax, 'SCRAMBLE !')
button1.on_clicked(scramble_)

# R BUTTON
button2_ax = plt.axes([0.05, 0.75, 0.075, 0.075])
button2 = plt.Button(button2_ax, 'R')
button2.on_clicked(r_move)

# Ri BUTTON
button3_ax = plt.axes([0.125, 0.75, 0.075, 0.075])
button3 = plt.Button(button3_ax, 'Ri')
button3.on_clicked(ri_move)

# L BUTTON
button4_ax = plt.axes([0.05, 0.65, 0.075, 0.075])
button4 = plt.Button(button4_ax, 'L')
button4.on_clicked(l_move)

# Li BUTTON
button5_ax = plt.axes([0.125, 0.65, 0.075, 0.075])
button5 = plt.Button(button5_ax, 'Li')
button5.on_clicked(li_move)

# F BUTTON
button6_ax = plt.axes([0.05, 0.55, 0.075, 0.075])
button6 = plt.Button(button6_ax, 'F')
button6.on_clicked(f_move)

# Fi BUTTON
button7_ax = plt.axes([0.125, 0.55, 0.075, 0.075])
button7 = plt.Button(button7_ax, 'Fi')
button7.on_clicked(fi_move)

# U BUTTON
button8_ax = plt.axes([0.05, 0.45, 0.075, 0.075])
button8 = plt.Button(button8_ax, 'U')
button8.on_clicked(u_move)

# Ui BUTTON
button9_ax = plt.axes([0.125, 0.45, 0.075, 0.075])
button9 = plt.Button(button9_ax, 'Ui')
button9.on_clicked(ui_move)

# B BUTTON
button10_ax = plt.axes([0.05, 0.35, 0.075, 0.075])
button10 = plt.Button(button10_ax, 'B')
button10.on_clicked(b_move)

# Bi BUTTON
button11_ax = plt.axes([0.125, 0.35, 0.075, 0.075])
button11 = plt.Button(button11_ax, 'Bi')
button11.on_clicked(bi_move)

# D BUTTON
button12_ax = plt.axes([0.05, 0.25, 0.075, 0.075])
button12 = plt.Button(button12_ax, 'D')
button12.on_clicked(d_move)

# Di BUTTON
button13_ax = plt.axes([0.125, 0.25, 0.075, 0.075])
button13 = plt.Button(button13_ax, 'Di')
button13.on_clicked(di_move)

# RESET BUTTON
button14_ax = plt.axes([0.05, 0.15, 0.15, 0.075])
button14 = plt.Button(button14_ax, 'RESET')
button14.on_clicked(reset_)

# PLOT ALL & SHOW
plot_all()
plt.show()