import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Variables globales para el ángulo de rotación
angle = 0.0

def init():
    """Inicializa los parámetros de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Habilita la prueba de profundidad

def draw_cube():
    """Dibuja la base de la casa como un cubo"""
    glBegin(GL_QUADS)
    # Frente
    glColor3f(0.8, 0.5, 0.2)  # Marrón
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Atrás
    glColor3f(0.7, 0.4, 0.2)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Izquierda
    glColor3f(0.6, 0.3, 0.1)
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # Derecha
    glColor3f(0.6, 0.3, 0.1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Arriba
    glColor3f(0.9, 0.5, 0.3)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Abajo
    glColor3f(0.5, 0.3, 0.1)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    """Dibuja el techo de la casa como una pirámide"""
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)  # Rojo

    # Frente
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)

    # Atrás
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)

    # Izquierda
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(0, 2, 0)

    # Derecha
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)
    glEnd()

def display():
    """Renderiza la escena"""
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(4, 3, 10, 0, 1, 0, 0, 1, 0)  # Mira la casa desde un poco más lejos

    # Rotar la escena
    glRotatef(angle, 0, 1, 0)

    # Dibujar la casa
    draw_cube()
    draw_roof()

def main():
    """Función principal"""
    global angle

    # Inicializa GLFW
    if not glfw.init():
        print("No se pudo inicializar GLFW")
        return

    # Crea la ventana
    window = glfw.create_window(800, 600, "Casa 3D con GLFW y OpenGL", None, None)
    if not window:
        glfw.terminate()
        print("No se pudo crear la ventana")
        return

    glfw.make_context_current(window)

    # Configura OpenGL
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        # Rotación automática
        angle += 0.5
        if angle > 360:
            angle -= 360

        # Renderizar
        display()

        # Intercambiar buffers
        glfw.swap_buffers(window)

        # Poll events
        glfw.poll_events()

    # Finaliza GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
