import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import struct

# Función para cargar una textura BMP
def load_texture(filename):
    """Carga un archivo BMP y genera una textura de OpenGL"""
    with open(filename, "rb") as f:
        header = f.read(54)  # Cabecera BMP de 54 bytes
        width, height = struct.unpack("ii", header[18:26])
        data_offset = struct.unpack("I", header[10:14])[0]
        
        f.seek(data_offset)
        data = f.read()

    # almacena píxeles en orden BGR, los convertimos a RGB
    image_data = bytearray()
    for i in range(0, len(data), 3):
        image_data.extend([data[i + 2], data[i + 1], data[i]])

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad
    glEnable(GL_TEXTURE_2D)           # Activar texturas
    glShadeModel(GL_SMOOTH)           # Sombreado suave

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión
    glMatrixMode(GL_MODELVIEW)

def draw_trunk(texture_id):
    """Dibuja el tronco del árbol como un cilindro texturizado"""
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glColor3f(1.0, 1.0, 1.0)  # Blanco para mostrar la textura
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(-90, 1, 0, 0)  # Rotar para orientar verticalmente
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, 0.3, 0.3, 2.0, 32, 32)
    glPopMatrix()

def draw_foliage(texture_id):
    """Dibuja las hojas del árbol como una esfera texturizada"""
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glColor3f(1.0, 1.0, 1.0)  # Blanco para mostrar la textura
    glTranslatef(0.0, 2.0, 0.0)
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, 1.0, 32, 32)
    glPopMatrix()

def draw_ground(texture_id):
    """Dibuja un plano para representar el suelo con textura"""
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)  # Blanco para mostrar la textura
    glTexCoord2f(0.0, 0.0); glVertex3f(-10, 0, 10)
    glTexCoord2f(1.0, 0.0); glVertex3f(10, 0, 10)
    glTexCoord2f(1.0, 1.0); glVertex3f(10, 0, -10)
    glTexCoord2f(0.0, 1.0); glVertex3f(-10, 0, -10)
    glEnd()

def draw_tree(trunk_texture, foliage_texture, ground_texture):
    """Dibuja un árbol completo"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(4, 3, 8,  # Posición de la cámara
              0, 1, 0,  # Punto al que mira
              0, 1, 0)  # Vector hacia arriba

    draw_ground(ground_texture)  # Dibuja el suelo
    draw_trunk(trunk_texture)   # Dibuja el tronco
    draw_foliage(foliage_texture) # Dibuja las hojas

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Árbol con Texturas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Carga de texturas BMP
    trunk_texture = load_texture("trunk.bmp")      # Textura para el tronco
    foliage_texture = load_texture("foliage.bmp") # Textura para las hojas
    ground_texture = load_texture("groud.bmp")   # Textura para el suelo

    if not trunk_texture or not foliage_texture or not ground_texture:
        print("Error al cargar texturas.")
        glfw.terminate()
        sys.exit()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_tree(trunk_texture, foliage_texture, ground_texture)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
