import random

# Избира произволна дума от списъка и я връща като резултат
def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(words)

# Показва думата подадена в параметъра word, като "разкрива" тези букви, които се намиратв списъка guessed_letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

# Главен метод на приложението
def main():
    word = choose_word()
    guessed_letters = []
    max_attempts = 7


    print("Добре дошли в играта Бесеница!")
    print("Думата има ", len(word), "букви.")
    
    attempts = 0
    while attempts < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Познайте буква или цяла дума: ").lower()
        
        if len(guess) == 1:  # 
            if guess in guessed_letters:
                print("Вече пробвахте тази буква!")
            elif guess in word:
                guessed_letters.append(guess)
                if checkGuess(word, guessed_letters) == True:
                    print("Поздравления! Познахте думата:", word)
                    break
                else:
                    print("Правилна буква!")
            else:
                print("Буквата ", guess, " не се среща!")
            attempts += 1
        #TODO: Добавете логически случай, в който потребителят се опитва да познае ЦЯЛАТА дума наведнъж
        else:
            print("Please enter a single letter or the whole word.")
        #TODO: Добавете съобщение за оставащите опити
        
    
    if attempts == max_attempts:
        print("\nSorry, you ran out of attempts. The word was:", word)


# Връща истина ако списъка от букви guessed_letters_list съдържа всяка една буква в стринга word
def checkGuess(word, guessed_letters):
    guessed_count = 0
    for letter in guessed_letters:
        guessed_count += word.count(letter)
    if guessed_count == len(word):
        return True
    else:
        return False 
    #TODO: Проверете дали буквите от думата word се съдържат в масива guessed_letters_list и ако това е така върнете истина/True иначе върнете False
    print('Реализирайте функцията')

if __name__ == "__main__":
    main()