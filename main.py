import pyautogui
import time


def solve(yellow_letter, grey_letters):
    found_words = []
    with open("possible_words.txt", "r") as file:
        for line in file:
            line = line[:-1]  # Remove "\n"
            all_char_in_line = True
            for char in line:
                if char not in (yellow_letter + grey_letters):
                    all_char_in_line = False
                    break

            if all_char_in_line and yellow_letter in line:
                found_words.append(line)

    return found_words


def type(words):
    for word in words:
        pyautogui.typewrite(word, interval=0.1)
        pyautogui.press('enter')
        time.sleep(0.5)


yellow_letter, grey_letters = input("Yellow Letter: "), input("Grey Letters: ")

words = sorted(solve(yellow_letter, grey_letters), key=len, reverse=True)
print(f'Words: {words}')

# type(words)
