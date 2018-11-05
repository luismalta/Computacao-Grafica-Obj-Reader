
class file():
    def __init__(self):
        # Listas
        vertices = []
        faces = []

        file = open('hammer.obj', 'r')


    def linha_vertice(line):
        if line[0] == 'v':
            linha = str(line).split(' ')
            if len(linha) == 5:
                tipo, _,x, y,z = linha
                #print(tipo,x, y, z)
                return float(x),float(y),float(z)


    def linha_face(line):
        if line[0] == 'f':

            linha = str(line).split(' ')
            if len(linha) == 5:
                tipo, v1, v2, v3, _ = linha
                return v1,v2,v3


    def leitura_obj(self):
        for line in file.readlines():
            if linha_vertice(line) is not None:
                vertices.append(linha_vertice(line))
            if linha_face(line) is not None:
                vertices.append(linha_face(line))
        print(vertices)
        print(faces)
a = file()


a.leitura_obj()



    # for line in file:
    #      print(str(line[0:2]))
