import random
import sys

def jugar_cachipum(usuario):
    opciones = ['piedra', 'papel', 'tijera']
    npc = random.choice(opciones)
    
    print("El jugador elige:", npc)
    print("La computadora elige:", npc)

    if usuario == npc:
        print("¡Empate!")
    elif (usuario == 'piedra' and npc == 'tijera') or \
         (usuario == 'papel' and npc == 'piedra') or \
         (usuario == 'tijera' and npc== 'papel'):
        print("¡ Tu Ganaste. Genio!")
    else:
        print("¡La NPC gana!")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['piedra', 'papel', 'tijera']:
        print("Uso: python cachipum.py [piedra|papel|tijera]")
    else:
        usuario = sys.argv[1]
        jugar_cachipum(usuario)


