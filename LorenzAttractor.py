"""Solving Lorenz Attractor equations by Euler Method and Plotting the result in both 2D and 3D.
Also, visualized using Pygame."""

### Sahil Islam ###
### 04/06/2020 ###

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import pygame


def fx(x, y, z):
    sig = 10
    return sig * (y - x)


def fy(x, y, z):
    roh = 28
    return x * (roh - z) - y


def fz(x, y, z):
    beta = 8.0 / 3.0
    return x * y - beta * z


def calculation(initX, initY, initZ):
    xs = []
    ys = []
    zs = []
    ts = []
    x = initX
    y = initY
    z = initZ
    t = 0

    h = 0.01
    for i in range(10000):
        x = x + h * fx(x, y, z)
        y = y + h * fy(x, y, z)
        z = z + h * fz(x, y, z)
        t = t + h
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ts.append(t)
    return xs, ys, zs, ts


def twoDplot1(initX, initY, initZ):
    xs, ys, zs, ts = calculation(initX, initY, initZ)
    a = []
    b = []

    plt.subplot(2, 2, 1)
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("X vs Y")

    plt.subplot(2, 2, 2)
    plt.plot(xs, zs)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.title("X vs Z")

    plt.subplot(2, 2, 3)
    plt.plot(ys, zs)
    plt.xlabel("y")
    plt.ylabel("z")
    plt.title("Y vs Z")

    plt.subplot(2, 2, 4)
    plt.plot(a, b, label="sigma = 10")
    plt.plot(a, b, label="roh = 28")
    plt.plot(a, b, label="beta = 8/3")
    plt.xlabel("")
    plt.ylabel("")
    plt.legend()
    plt.title("Constants")

    plt.suptitle("Lorenz Attractor\n" + "Initial (x,y,z): " + "(" + str(initX) +
                 "," + str(initY) + ',' + str(initZ) + ")")
    plt.subplots_adjust(hspace=0.39)
    plt.show()

def twoDplot2(initX, initY, initZ):
    xs, ys, zs, ts = calculation(initX, initY, initZ)
    a = []
    b = []

    plt.subplot(2, 2, 1)
    plt.plot(ts, xs)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("X vs t")

    plt.subplot(2, 2, 2)
    plt.plot(ts, ys)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Y vs t")

    plt.subplot(2, 2, 3)
    plt.plot(ts, zs)
    plt.xlabel("t")
    plt.ylabel("z")
    plt.title("Z vs t")

    plt.subplot(2, 2, 4)
    plt.plot(a, b, label="sigma = 10")
    plt.plot(a, b, label="roh = 28")
    plt.plot(a, b, label="beta = 8/3")
    plt.xlabel("")
    plt.ylabel("")
    plt.legend()
    plt.title("Constants")

    plt.suptitle("Lorenz Attractor\n" + "Initial (x,y,z): " + "(" + str(initX) +
                 "," + str(initY) + ',' + str(initZ) + ")")
    plt.subplots_adjust(hspace=0.39)
    plt.show()


def threeDplot(initX, initY, initZ):
    xs, ys, zs, ts = calculation(initX, initY, initZ)
    ax = plt.axes(projection="3d")

    ax.plot3D(xs, ys, zs, color='k')
    ax.scatter3D(xs, ys, zs, c=zs, cmap='hsv')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Lorenz Attractor 3D plot\n" + "Initial (x,y,z): " + "(" + str(initX) +
                 "," + str(initY) + ',' + str(initZ) + ")")

    plt.show()


def dynamic_pygameLoop(initX, initY, initZ):
    xs, ys, zs, ts = calculation(initX, initY, initZ)
    pygame.init()
    display_width = 900
    display_height = 650

    black = [0, 0, 0]
    white = [255, 255, 255]
    green = [0, 255, 0]
    red = [255, 0, 0]

    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Lorenz Attractor")

    def point(x, y):
        pygame.draw.circle(screen, red, [int(x), int(y)], 2)

    xo = display_width / 2.0
    yo = 0
    scale = 10

    screen.fill(black)
    for i in range(len(ys)):

        plotx = (xs[i] * scale) + xo
        ploty = (ys[i] * scale) + xo
        plotz = (zs[i] * scale) + yo

        point(ploty, plotz)
        pygame.display.update()
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


threeDplot(0.01, 0, 0)
