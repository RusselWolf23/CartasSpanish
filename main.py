from Carta import Carta
import random


def baraja():
    numeros = list(range(1, 10))
    numeros.append("👩")
    numeros.append("🐴")
    numeros.append("👑")
    palos = ["⚔️", "🏆", "🌵", "🥇"]
    cosa=Carta(1,"⚔️")
    baraja = []

    for palo in palos:
        for num in numeros:
            carta=Carta(num,palo)
            baraja.append(carta)

    # while len(baraja) < 5:
    #     num = random.choice(numeros)
    #     palo = random.choice(palos)
    #     carta = Carta(num, palo)

    #     for cart in baraja:
    #         if cart.numero != carta.numero and cart.palo != carta.palo:
    #             baraja.append(carta)
    #             break

    for cart in baraja:
        print(cart.ver())
    print(f"Hay {len(baraja)} cartas en la baraja")


if __name__ == "__main__":
    baraja()
