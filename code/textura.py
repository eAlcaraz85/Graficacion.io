from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def load_texture(image_path):
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Cargar imagen de textura
    from PIL import Image
    img = Image.open(image_path)
    img_data = img.tobytes("raw", "RGB", 0, -1)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture_id

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    
    # Crear un objeto cuadrático
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)  # Habilitar texturas
    gluQuadricNormals(quadric, GLU_SMOOTH)
    
    # Dibujar una esfera con textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    gluSphere(quadric, 1.0, 32, 32)
    
    gluDeleteQuadric(quadric)
    glDisable(GL_TEXTURE_2D)
    glutSwapBuffers()

def main():
    global texture_id
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Textura")
    
    glEnable(GL_DEPTH_TEST)
    texture_id = load_texture("/home/likcos/Materias/Graficacion/code/foliage.bmp")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
