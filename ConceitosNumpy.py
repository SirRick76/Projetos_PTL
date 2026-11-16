import numpy as np
import cProfile

valores=np.array([10,20,30,40])
print(valores)
print(valores.dtype)

array1=np.array([10,20,30])
array2=np.array((10,20,30))
array3=np.array({10,20,30})
array4=np.array(range(10,40,10))
dados={"A":10,"B":20,"C":30}
array5=np.array(list(dados.values()))
array6=np.array(list(dados.keys()))
array7=np.array(dados)

print("array1:",array1)
print("array2:",array2)
print("array3:",array3)
print("array4:",array4)
print("array5:",array5)
print("array6:",array6)
print("array7:",array7)

vetor=np.array([10,20,30,40,50,60])
matriz1=np.array([
    [10,20,30],
    [40,50,60]
])
matriz2=np.array([
    [10,20],
    [30,40],
    [50,60]
])
forma=matriz2.shape
tamanho=matriz2.size
dimensoes=matriz2.ndim
print(vetor)
print(matriz1)
print("Matriz2:",matriz2,forma,tamanho,dimensoes)

array_3D=np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]],
    [[19,20,21],[22,23,24],[25,26,27]],
])
print("Array 3d:\n",array_3D)

array_zero=np.zeros((3,3))
print("Array 0:\n",array_zero)
array_um=np.ones((2,3))
print("Array 1:\n",array_um)
array_full=np.full((3,2),76)
print("Array Full:\n",array_full)

valores3=np.arange(10)
print("Valores arrange 10:",valores3)

valores4=np.arange(2,10,2)
print("Valores arrange 2-10 de 2 em 2:",valores4)

valores5=np.linspace(0,10,5)
print("Valores com espacamento",valores5)

valores6=np.linspace(0,10,5,endpoint=False)
print("Valores com espacamento, sem o final",valores6)

array8=np.random.randint(0,50,10)
print("Array random:",array8)

valores7= np.random.rand(5)
print(valores7)

valores8=np.random.uniform(10,50,5)
print(valores8)

valores9=np.random.uniform(10,50,5)
valores9=np.round(valores9,2)
print("Valores:", valores9)

#Funções estatisticas
print("Máximo:", valores9.max())
print("Mínimo:", valores9.min())
print("Soma:", valores9.sum())
print("Média", valores9.mean())
print("Desvio-Padrão", valores9.std())

#Funções de posição
print("Posição do máximo:", valores9.argmax())
print("Posição do mínimo:", valores9.argmin())

a=np.array([10,20,30])
b=np.array([2,4,5])

print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Potencialização:", a ** 2)

preços=np.array([10,20,30,40])
precos_com_desconto=preços-5
print(precos_com_desconto)

preços_atualizados=preços* 1.10
print(preços_atualizados)

abs=np.abs(valores9) 
sqrt=np.sqrt(valores9) 
power=np.power(valores9,2) 
exp=np.exp(valores9) 
log=np.log(valores9) 
round=np.round(valores9) 
floor=np.floor(valores9) 
ceil=np.ceil(valores9) 

print("Valor absoluto:", abs, "Raiz quadrada:", sqrt ,"Potência:",power,"Exponencial", exp ,"Logaritmo:", log , "Valores arredondados:", round ,"Arrendondos para baixo:", floor ,"Arrendondos para cima:", ceil)


temperaturas = np.array([
    [18,20,22],
    [19,21,23],
    [17,20,24],
    [16,19,21]
])
correcao= np.array([1,2,0.5])
temperaturas_corrigidas = temperaturas + correcao
print(temperaturas_corrigidas)

lista=list(range(1000000))
array1M=np.arange(1000000)
def operar_lista():
    resultado = [x+1 for x in lista]

def operar_array():
    resultado=array1M+1

print("ANÁLISE DA LISTA")
cProfile.run('operar_lista()')
print("ANÁLISE DO ARRAY NUMPY")
cProfile.run('operar_array()')

