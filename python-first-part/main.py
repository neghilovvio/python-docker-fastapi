from module2.get_connection import funzione
from file import print_something
from pydantic import BaseModel


class Schema(BaseModel):
    nome_proprietario: str


class Car(BaseModel):

    def __init__(self, schema: Schema):
        print(schema['nome_proprietario'])


schema = {
    'nome_proprietario': 1
}



var = [1,2,3]



def function(lista):
    new_list = lista.copy()
    new_list.pop()
    return new_list


new_list = function(var)


print(new_list)
print(var)


# car = Car(schema)




# list = []
# dict = {}

# print(requests.__version__)
