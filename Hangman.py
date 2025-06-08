import random
hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_bank = [
    # AI & ML
    "neuron", "model", "dataset", "learning", "training", "inference", "epoch", "batch", "optimizer",
    "gradient", "tensor", "vector", "matrix", "loss", "activation", "network", "weights", "bias",

    # Programming
    "python", "script", "function", "loop", "class", "object", "variable", "array", "string",
    "debug", "compile", "syntax", "logic", "runtime", "integer", "float", "index", "stack", "heap",

    # Tech & CS
    "algorithm", "binary", "bit", "byte", "cloud", "server", "client", "router", "socket",
    "crypto", "blockchain", "cache", "thread", "kernel", "api", "query", "hash", "data", "protocol",

    # Creative / Futuristic
    "vision", "dream", "prompt", "pixel", "render", "quantum", "hacker", "core", "smart", "meta",
    "cyber", "virtual", "matrix", "future", "robot", "fusion", "autonomous", "singularity", "thought",

    # Extra General Useful Words
    "engineer", "design", "system", "node", "module", "flow", "input", "output", "code", "compile",
    "task", "feature", "signal", "channel", "command", "frame", "stream", "pipeline"
]
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
''')
random_word = random.choice(word_bank)
total_letters = len(random_word)
placeholder = []
for x in range(total_letters):
    placeholder.append('_')
print('Word to guess: '+' '.join(placeholder))
n = 0
game_result = True
while game_result:
    guess = input('\nGuess a letter : ')
    if guess.lower() in placeholder:
        print('Already chosen, choose another one!')
    for x in range(total_letters):
        if guess.lower() == random_word[x]:
            placeholder[x] = guess
    if guess.lower() in placeholder:
        print('************ correct guess ************')
    if ''.join(placeholder) == random_word:
            game_result = False
    if not guess in random_word:
        print("You chose a letter that's not in the word, you lose a life.")
        if n < 6:
            n += 1
        print(f'**********  You have {6-n}/6 lives left **********')
        if n == 6:
            game_result = False
    print(' '.join(placeholder))
    print(hangman_art[n])
if ''.join(placeholder) == random_word:
    print('\n******************************** You Win! **************************************')
else:
    print('\n******************************** you lose **************************************')
    print('\n******************************** Game Over **************************************')
input()