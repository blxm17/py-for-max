import random


def play_guess_number():
    # Generiere eine zufällige Zahl zwischen 1 und 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Willkommen zum Zahlenraten-Spiel!")
    print(
        f"Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast {max_attempts} Versuche."
    )
    print("Lass uns anfangen!")

    while attempts < max_attempts:
        try:
            # Hole die Vermutung des Spielers
            guess = int(input("\nBitte gib deine Vermutung ein: "))
            attempts += 1

            # Überprüfe, ob die Vermutung richtig ist
            if guess < secret_number:
                print(f"Zu klein! Du hast noch {max_attempts - attempts} Versuche")
            elif guess > secret_number:
                print(f"Zu groß! Du hast noch {max_attempts - attempts} Versuche")
            else:
                print("\nGlückwunsch! Du hast es geschafft!")
                print(f"Du hast {attempts} Versuche gebraucht!")
                break

        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")
            continue

    if attempts == max_attempts and guess != secret_number:
        print(f"\nSpiel vorbei! Die richtige Zahl war {secret_number}")

    # Frage, ob der Spieler noch einmal spielen möchte
    play_again = input("\nMöchtest du noch einmal spielen? (ja/nein): ")
    if play_again.lower() in ["ja", "j", "yes", "y"]:
        play_guess_number()
    else:
        print("Danke fürs Spielen! Auf Wiedersehen!")


if __name__ == "__main__":
    play_guess_number()
