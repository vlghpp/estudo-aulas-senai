from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Henrique')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta

escritor.ferramenta.escrever() ## Vai printar: A CANETA está escrevendo...

# O mesmo se aplica caso fizer com a máquina

escritor.ferramenta = maquina

escritor.ferramenta.escrever()