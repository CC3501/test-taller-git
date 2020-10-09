import glfw
from OpenGL.GL import *
import numpy as np
import sys

import transformations2 as tr2
import basic_shapes as bs
import easy_shaders as es

from model import *
from controller import *

if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 600
    height = 600

    window = glfw.create_window(width, height, "EPIC TPOSE VIEWER", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    controller = Controller()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controller.on_key)

    # Creating shader programs for textures and for colores
    textureShaderProgram = es.SimpleTextureModelViewProjectionShaderProgram()  # TEXTURAS
    colorShaderProgram = es.SimpleModelViewProjectionShaderProgram()  # COLORES

    # Setting up the clear screen color
    glClearColor(0.15, 0.15, 0.15, 1.0)

    # As we work in 3D, we need to check which part is in front,
    # and which one is at the back
    glEnable(GL_DEPTH_TEST)

    # crear la camara y la proyeccion son usadas por el shader
    projection = tr2.ortho(-1, 1, -1, 1, 0.1, 100)  # volumen de visualizacion
    view = tr2.lookAt(  # hacia donde apunto y donde está la camara
        np.array([10, 10, 5]),
        np.array([0, 0, 0]),
        np.array([0, 0, 1])
    )

    tpose = Tpose('img/mememan.png')
    axis = Axis()

    # Definimos las referencias cruzadas
    controller.set_tpose(tpose)

    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        axis.draw(colorShaderProgram, projection, view)
        tpose.draw(colorShaderProgram, textureShaderProgram, projection, view)

        # Once the drawing is rendered, buffers are swap so an uncomplete drawing is never seen.
        glfw.swap_buffers(window)

    glfw.terminate()
