from sys import stdin

#Juan Esteban Acosta Lopez - Agosto 2021
                
def main():
    numeroElecciones = int( stdin.readline() )
    while numeroElecciones != 0:
        if stdin.readline() != "":
            numeroCandidatos = int( stdin.readline() )
            partidos = {}
            for i in range( numeroCandidatos ):
               nombreCandidato = stdin.readline().strip()
               nombrePartido = stdin.readline().strip()
               partidos[ nombreCandidato ] = [ nombrePartido, 0 ]
            numeroVotos = int( stdin.readline() )
            nombresCandidatos = partidos.keys()
            for i in range( numeroVotos ):
                candidatoTemporal = stdin.readline().strip()
                if candidatoTemporal in nombresCandidatos:
                    partidos[ candidatoTemporal ][ 1 ] += 1
            mayor = 0
            candidatoGanador = None
            partidoGanador = None
            for nombreCandidato in partidos:
                if partidos[ nombreCandidato ][ 1 ] > mayor:
                    mayor = partidos[ nombreCandidato ][ 1 ]
                    partidoGanador = partidos[ nombreCandidato ][ 0 ]
                    candidatoGanador = nombreCandidato
            for nombreCandidato in partidos:
                if partidos[ nombreCandidato ][ 1 ] == mayor and nombreCandidato != candidatoGanador:
                    partidoGanador = "tie"
            if numeroElecciones > 1:
                print( f"{ partidoGanador }\n" )
            else:
                print( f"{ partidoGanador }" )
            numeroElecciones -= 1
main()