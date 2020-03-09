from .node import Node

class Queue:

    def __init__(self):
        self.first_element = None
        self.last_element = None
        self.size = 0

    def push(self, element):
        """
        ADICIONA ELEMENTOS NA FILA.
        """

        node = Node(element)

        # PREENCHE DADOS SEMPRE NA ULTIMA POSIÇÃO
        if self.last_element is None:
            self.last_element = node
        else:
            self.last_element.next = node
            self.last_element = node

        # PREENCHE DADOS NA PRIMEIRA POSIÇÃO
        if self.first_element is None:
            self.first_element = node

        # AUMENTA TAMANHO DA FILA
        self.size = self.size + 1

    def pop(self):
        """
        REMOVE ELEMENTO DA PRIMEIRA POSIÇÃO NA FILA.
        """

        if self.size > 0:
            # VALOR DO PRIMEIRO CAMPO PARA RETORNO
            element = self.first_element.data 
            
            # AVANÇA AS POSIÇÕES DA FILA
            self.first_element = self.first_element.next

            # DIMINUI TAMANHO DA FILA
            self.size = self.size - 1

            return element

        return IndexError('Fila Vazia!')

        
    def peek(self):
        """
        LÊ PRIMEIRO ELEMENTO DA FILA.
        """

        if self.size > 0:
            # VALOR DO PRIMEIRO CAMPO PARA RETORNO
            element = self.first_element.data 
            
            return element

        return IndexError('Fila Vazia!')

    '''def last(self):
        n = self.size
        first_n_elements = [my_queue.peek() for _ in range(N)]

        if self.size > 0:
            return self.last_element'''        

    def __repr__(self):
        r = ""
        pointer = self.first_element

        while (pointer != None):
            r = r + str(pointer.data)

        return r


    def len(self):
        return self.size