import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width = 40, theme = Theme({"warning": "red on yellow"}))

def main():
    word = get_random_word()
    guesses = ["_" * 5] * 6
    for idx in range(6):
        refresh_page(headline = f"猜测 {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = guess_word(previous_guesses=guesses[:idx])
        if guesses[idx] == word:
            break
    game_over(guesses, word, guessed_correctly=guesses[idx] == word)

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def get_random_word():
    if words := [
        "Apple",
        "Bread",
        "Cloud",
        "Dance",
        "Early",
        "Adder",
        "Grape"
    ]:
        return random.choice(words)
    else:
        console.print("单词列表中没有长度为5的单词", style="warning")
        raise SystemExit()

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

        console.print("".join(styled_guess), justify="center")

def guess_word(previous_guesses):
    if(len(previous_guesses) > 10):raise ValueError
    guess = console.input("\n猜测单词：").upper()

    if guess in previous_guesses:
        console.print(f"您已经猜测了 {guess}.", style="warning")
        return guess_word(previous_guesses)

    if len(guess) != 5:
        console.print("您的猜测必须为5个字母。", style="warning")
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"非法字母：'{invalid}'。请使用英文字母.",
            style="warning",
        )
        return guess_word(previous_guesses)

    return guess

def game_over(guesses, word, guessed_correctly):
    if(not guessed_correctly in [0,1]) : raise ValueError
    refresh_page(headline="游戏结束")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]正确，单词是{word}[/]")
    else:
        console.print(f"\n[bold white on red]对不起，单词是{word}[/]")

if __name__ == "__main__":
    main()