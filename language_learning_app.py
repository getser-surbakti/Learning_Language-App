import random

# List of common words in Spanish and their English translations
words = [
    {"Spanish": "hola", "English": "hello"},
    {"Spanish": "adiós", "English": "goodbye"},
    {"Spanish": "por favor", "English": "please"},
    {"Spanish": "gracias", "English": "thank you"},
    {"Spanish": "sí", "English": "yes"},
    {"Spanish": "no", "English": "no"},
    {"Spanish": "¿cómo?", "English": "how?"},
    {"Spanish": "¿qué?", "English": "what?"},
    {"Spanish": "¿dónde?", "English": "where?"},
    {"Spanish": "¿cuándo?", "English": "when?"},
    {"Spanish": "¿por qué?", "English": "why?"},
    {"Spanish": "quién", "English": "who"},
    {"Spanish": "cuál", "English": "which"},
    {"Spanish": "este", "English": "this"},
    {"Spanish": "ese", "English": "that"},
    {"Spanish": "aquí", "English": "here"},
    {"Spanish": "allí", "English": "there"},
    {"Spanish": "yo", "English": "I"},
    {"Spanish": "tú", "English": "you"},
    {"Spanish": "él", "English": "he"},
    {"Spanish": "ella", "English": "she"},
    {"Spanish": "nosotros", "English": "we"},
    {"Spanish": "ellos", "English": "they"},
    {"Spanish": "mi", "English": "my"},
    {"Spanish": "tu", "English": "your"},
    {"Spanish": "su", "English": "his/her"},
    {"Spanish": "nuestro", "English": "our"},
    {"Spanish": "un", "English": "a/an"},
    {"Spanish": "una", "English": "a/an"},
    {"Spanish": "y", "English": "and"},
    {"Spanish": "o", "English": "or"},
    {"Spanish": "pero", "English": "but"},
    {"Spanish": "porque", "English": "because"},
    {"Spanish": "muy", "English": "very"},
    {"Spanish": "mucho", "English": "a lot"},
    {"Spanish": "más", "English": "more"},
    {"Spanish": "menos", "English": "less"},
    {"Spanish": "bien", "English": "good/well"},
    {"Spanish": "mal", "English": "bad/ill"},
    {"Spanish": "grande", "English": "big"},
    {"Spanish": "pequeño", "English": "small"},
    {"Spanish": "nuevo", "English": "new"},
    {"Spanish": "viejo", "English": "old"},
    {"Spanish": "bueno", "English": "good"},
    {"Spanish": "malo", "English": "bad"},
    {"Spanish": "fácil", "English": "easy"},
    {"Spanish": "difícil", "English": "difficult"},
    {"Spanish": "rápido", "English": "fast"},
    {"Spanish": "lento", "English": "slow"},
    {"Spanish": "caliente", "English": "hot"},
    {"Spanish": "frío", "English": "cold"},
    {"Spanish": "amigo", "English": "friend"},
    {"Spanish": "familia", "English": "family"},
    {"Spanish": "comida", "English": "food"},
    {"Spanish": "agua", "English": "water"},
    {"Spanish": "casa", "English": "house"},
    {"Spanish": "trabajo", "English": "work"},
    {"Spanish": "escuela", "English": "school"},
    {"Spanish": "niño", "English": "child"},
    {"Spanish": "día", "English": "day"},
    {"Spanish": "noche", "English": "night"},
    {"Spanish": "mañana", "English": "morning/tomorrow"},
    {"Spanish": "hoy", "English": "today"},
    {"Spanish": "ayer", "English": "yesterday"},
    {"Spanish": "uno", "English": "one"},
    {"Spanish": "dos", "English": "two"},
    {"Spanish": "tres", "English": "three"},
    {"Spanish": "cuatro", "English": "four"},
    {"Spanish": "cinco", "English": "five"},
    {"Spanish": "seis", "English": "six"},
    {"Spanish": "siete", "English": "seven"},
    {"Spanish": "ocho", "English": "eight"},
    {"Spanish": "nueve", "English": "nine"},
    {"Spanish": "diez", "English": "ten"},
    {"Spanish": "cien", "English": "hundred"},
    {"Spanish": "mil", "English": "thousand"},
    {"Spanish": "alto", "English": "high"},
    {"Spanish": "bajo", "English": "low"},
    {"Spanish": "blanco", "English": "white"},
    {"Spanish": "negro", "English": "black"},
    {"Spanish": "rojo", "English": "red"},
    {"Spanish": "azul", "English": "blue"},
    {"Spanish": "verde", "English": "green"},
    {"Spanish": "amarillo", "English": "yellow"},
    {"Spanish": "gordo", "English": "fat"},
    {"Spanish": "delgado", "English": "thin"},
    {"Spanish": "feliz", "English": "happy"},
    {"Spanish": "triste", "English": "sad"},
    {"Spanish": "izquierda", "English": "left"},
    {"Spanish": "derecha", "English": "right"},
    {"Spanish": "hombre", "English": "man"},
    {"Spanish": "mujer", "English": "woman"},
    {"Spanish": "niña", "English": "girl"},
    {"Spanish": "perro", "English": "dog"},
    {"Spanish": "gato", "English": "cat"},
    {"Spanish": "coche", "English": "car"},
    {"Spanish": "tren", "English": "train"},
    {"Spanish": "avión", "English": "plane"},
    {"Spanish": "ciudad", "English": "city"},
    {"Spanish": "mundo", "English": "world"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['Spanish']}'?")
        user_answer = input("Your answer (or type 'quit' to stop the quiz): ").strip().lower()

        if user_answer == 'quit':
            print(f"Quiz stopped. Your score: {score}/{len(words)}")
            break

        correct_answer = word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['English']}'.\n")
    
    else:
        print(f"Quiz complete! Your final score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
