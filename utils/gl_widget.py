
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import Qt, QTimer
from OpenGL.GL import *
import math

class GLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.last_pos = None
        self.x_rot = 20
        self.y_rot = 30
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(16)

    def update_angle(self):
        self.angle += 1
        self.update()

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = w / h if h != 0 else 1
        glFrustum(-aspect, aspect, -1, 1, 1.5, 40.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.x_rot, 1, 0, 0)
        glRotatef(self.y_rot, 0, 1, 0)
        self.draw_cube()

    def draw_cube(self):
        glBegin(GL_QUADS)
        for surface in self.cube_surfaces():
            for vertex in surface:
                glVertex3fv(vertex)
        glEnd()

    def cube_surfaces(self):
        v = [
            [-1, -1, -1],
            [ 1, -1, -1],
            [ 1,  1, -1],
            [-1,  1, -1],
            [-1, -1,  1],
            [ 1, -1,  1],
            [ 1,  1,  1],
            [-1,  1,  1],
        ]
        return [
            [v[0], v[1], v[2], v[3]],
            [v[4], v[5], v[6], v[7]],
            [v[0], v[1], v[5], v[4]],
            [v[2], v[3], v[7], v[6]],
            [v[1], v[2], v[6], v[5]],
            [v[4], v[7], v[3], v[0]],
        ]

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.last_pos:
            dx = event.x() - self.last_pos.x()
            dy = event.y() - self.last_pos.y()
            self.x_rot += dy
            self.y_rot += dx
            self.last_pos = event.pos()
            self.update()
