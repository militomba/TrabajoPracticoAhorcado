from Ahorcado import Ahorcado
from AhorcadoService import AhorcadoService


class Menu():
    def seleccion_jugadores(self):
        print("Seleccione Opcion")
        print("1 => 1 jugador")
        print("2 => 2 jugadores")
        print("3 => Ver resultados")
        return int(input("Seleccione opcion => "))


if __name__ == "__main__":

    while True:
        cant_jugadores = Menu().seleccion_jugadores()
        if cant_jugadores == 1:
            result = Ahorcado().un_jugador()
        if cant_jugadores == 2:
            result = Ahorcado().dos_jugadores()
        if cant_jugadores == 3:
            AhorcadoService().ver_partida_guardada()
        if cant_jugadores != 1 and cant_jugadores != 2 and cant_jugadores != 3:
            print("\n\n\nEsa no es una opcion, elija otra\n\n\n")
