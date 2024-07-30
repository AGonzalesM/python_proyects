#=============================================#
class Warship:
    def __init__(self, id, name, along):
        self.id = id
        self.name = name
        self.along = along

class Destroyer(Warship):
    def __init__(self):
        super().__init__('D', 'Destructor', 2)

class Submarine(Warship):
    def __init__(self):
        super().__init__('S', 'Submarine', 3)

class Battleship(Warship):
    def __init__(self):
        super().__init__('B', 'Battleship', 4)

#=============================================#
class Sea:
    def __init__(self, width, along):
        self.width  = width
        self.along = along
        self.battlefield = []

    def create_battlefield(self):
        row = []
        for w in range(self.width):
            row.append(0)
        for a in range(self.along):
            self.battlefield.append(row.copy())

    def view_battlefield(self):
        for row in self.battlefield:
            print(' '.join(map(str, row)))

    def position_is_available(self, positionX, positionY):
        if len(self.battlefield) > 0:
            if self.battlefield[positionX][positionY] == 0:
                return True
            else:
                return False

    def position_ship_sea(self, warship: Warship, positionX, positionY, orientation):
        positionX = positionX - 1
        positionY = positionY - 1
        orientation = orientation.upper()

        if not self.position_is_available(positionX, positionY):
            return (f'Hay una nave estacionada en la posición ({positionX+1}, {positionY+1}), intente con otra ubicación.')

        if not (orientation == 'V' or orientation == 'H'):
            return (f'La orientación {orientation} no es válida.')

        try:
            if orientation == 'V':
                self.battlefield[positionX + warship.along][positionY]
            else:
                self.battlefield[positionX][positionY + warship.along]
        except IndexError:
            return (f'La nave {warship.name} con la orientación {orientation} no puede ubicarse en la posición ({positionX+1}, {positionY+1}) porque excede los limites del campo de batalla.')

        for _ in range(warship.along):
            if orientation == 'V':
                self.battlefield[positionX][positionY] = warship.id
                positionX += 1
            else:
                self.battlefield[positionX][positionY] = warship.id
                positionY += 1

    def is_battlefield_without_ships(self):
        row = []
        for w in range(self.width):
            row.append(0)
        for ship in self.battlefield:
            if ship != row:
                return False
        return True

#=============================================#
class Player:
    def __init__(self, id):
        self.id = id
        self.sea = Sea(10, 10)

class Play():
    def __init__(self):
        self.players = [Player(1), Player(2)]

    def start(self):
        warship_list = [Destroyer(), Submarine(), Battleship()]
        print('Bienvenido al juego de Batalla Naval!')
        for player in self.players:
            player.sea.create_battlefield()
            print(f'\nJugador {player.id} coloca sus barcos.')
            for ship in warship_list:
                while True:
                    print(f'Jugador {player.id}, coloca tu {ship.name} de tamaño {ship.along}.')
                    while True:
                        try:
                            positionX = int(input('Fila inicial: '))
                            break
                        except ValueError:
                            print('El valor ingresado no es válido, recuerde que el campo de batalla es de 10x10')
                    while True:
                        try:
                            positionY = int(input('Columna inicial: '))
                            break
                        except ValueError:
                            print('El valor ingresado no es válido, recuerde que el campo de batalla es de 10x10')
                    orientation = input(f'Dirección (H para horizontal, V para Vertical): ')
                    player.sea.position_ship_sea(ship, positionX, positionY, orientation)
                    break

    def attack(self):
        while True:
            for player in self.players:
                if player.sea.is_battlefield_without_ships():
                    print(f'\nTodas las naves del Player {player.id} fueron destruidas!')
                    print(f'El player {'1' if player.id == 2 else '2'} ganó la batalla!')
                    return
                print(f'\nJugador {player.id}, elige una posición para atacar')
                while True:
                    try:
                        positionX = int(input('Fila: '))
                        break
                    except ValueError:
                        print('El valor ingresado no es válido, recuerde que el campo de batalla es de 10x10')
                while True:
                    try:
                        positionY = int(input('Columna: '))
                        break
                    except ValueError:
                        print('El valor ingresado no es válido, recuerde que el campo de batalla es de 10x10')

                idx = 0 if player.id == 2 else 1
                otherPlayer = self.players[idx]
                if not otherPlayer.sea.position_is_available(positionX-1, positionY-1):
                    otherPlayer.sea.battlefield[positionX-1][positionY-1] = 0
                    print('Impacto!')
                    otherPlayer.sea.view_battlefield()
                else:
                    print('Agua!')

#Iniciando el juego
play = Play()
#Posicionando las naves en el campo de batalla
play.start()
#Mostrando las naves de cada jugador en el campo de batalla
for player in play.players:
    print(f'\nCampo de batalla del player {player.id}')
    player.sea.view_battlefield()
#Empezando la batalla
play.attack()