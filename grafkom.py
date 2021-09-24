from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


x, y = 500, 500
def titik():
# function untuk membuat objek titik
    glPointSize(5) #glpointsize untuk mengatur ukuran titik
    glBegin(GL_POINTS) #membuat onject titik
    glColor3ub(34, 227, 169) #mengatur warna dari titik menggunakan rgb
    glVertex2f(250, 250) #mengatur titik koordinat
    glVertex2f(150, 150)
    glVertex2f(150, 250)
    glVertex2f(250, 150)
    glEnd() #mengakhiri pembuatan objek

def garis():
    glPointSize(10)
    glBegin(GL_LINES)
    glColor3ub(34, 227, 169)
    glVertex2f(100, 100)
    glVertex2f(300, 300)
    glVertex2f(300, 100)
    glVertex2f(100, 300)
    glEnd()

def iterate():
    glViewport(0, 0, 200, 200) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #utk membersihkan layar
    glLoadIdentity()
    iterate()
    titik()
    garis()
    #garisloop()
    #kotak()
    #tak_beraturan()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(500, 500) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
#utk transparansi (tapi belum bisa)
#glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#glEnable(GL_BLEND)
wind = glutCreateWindow("Point and Lines") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program
