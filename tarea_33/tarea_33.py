"""
En este caso, tenéis que entender y dibujar el diagrama de flujo del programa de picachu tal y como se explica en el vídeo que adjuntamos y posteriormente codificarlo mediante un lenguaje de programación, es decir, construir el programa tal cual se indica en el diagrama.
"""
"""
Adjunto el Diagrama. He creado una clase pokemon que contiene ataque y vida. El algoritmo es simple!
"""
class Pokemon:
  def __init__(self, ataque, vida):
    self.ataque = ataque
    self.vida = vida


def algoritmo_pikachu():
    Pikachu = Pokemon(55, 100)
    Jigglypuff = Pokemon(45, 100)
    turno = 1
    while (Pikachu.vida > 0 and Jigglypuff.vida > 0):
        if turno == 1:
            Jigglypuff.vida = Jigglypuff.vida - Pikachu.ataque
            turno = 0
        else:
            Pikachu.vida = Pikachu.vida - Jigglypuff.ataque
            turno = 1
    
    if Pikachu.vida > 0:
        print("Pikachu wins!")
    else:
        print("Jigglypuff wins!")



if __name__ == "__main__":
    algoritmo_pikachu()

