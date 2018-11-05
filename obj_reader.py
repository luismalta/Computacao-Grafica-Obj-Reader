
class file_obj():
    def __init__(self, file_name):
        # Listas
        self.vertices = []
        self.faces = []


        try:
            self.file = open(file_name, 'r')
        except Exception as e:
            print("Arquivo não encontrado.")
            raise



    def linha_vertice(self,line):
        if line[0] == 'v':
            linha = str(line).split(' ')
            if len(linha) == 5:
                tipo, _,x, y,z = linha
                return x,y,z


    def linha_face(self,line):
        if line[0] == 'f':

            linha = str(line).split(' ')
            if len(linha) == 5:
                tipo, v1, v2, v3, _ = linha
                return v1,v2,v3


    def leitura_obj(self):
        for line in self.file.readlines():
            if self.linha_vertice(line) is not None:
                self.vertices.append(self.linha_vertice(line))
            if self.linha_face(line) is not None:
                self.faces.append(self.linha_face(line))


    def escreve_obj(self, file_name):
        file_write = open(file_name, 'w')

        for line in self.vertices:
            file_write.write('v ' + str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]))
        for line in self.faces:
            file_write.write('f ' + str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + '\n')
