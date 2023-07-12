Programming has proven to be a powerful skill, creating billion-dollar tech companies and amazing technological advances. It’s easy to want to aim high with your own software creations, but biting off more than you can chew can leave you with half-finished programs and frustration. However, you don’t need to be a computer genius to code fun and creative programs.
where you’re encouraged to manually copy the programs, play with them, and inspect their inner workings by running them under a debugger.
Programming is a fun, creative skill to develop. Whether you’ve mastered the basics of Python syntax or simply want to dive into some real Python programs, the projects in this repo will spark new ideas for what’s possible with as little as a few pages of code.

The best way to work through these programs isn’t to merely read their code or copy and paste it to your computer. Take the time to manually type the code from this book into your editor to develop the muscle memory for writing code. This also slows you down so you can consider each line as you type, instead of merely skimming it over with your eyes. Look up any instructions you don’t recognize using an internet search engine, or experiment with them in the interactive shell.

  I will share 21 small projects to this repository Finally, take it upon yourself to re-create the program from scratch and then modify it with features of your own. These exercises give you a solid foundation for how programming concepts are applied to create actual, runnable programs. And most of all, don’t forget to have fun!



# Bagels_project(project 1)
python short game which is very good for beginners to start a small project which helps the understanding and maturity in python

In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
the game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place,
Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.


I insisted on all who are new to programming how to do  this small project some steps will be followed-
First step ---> You can copy the code to become familiar with how they work
Second step --> Experiment with your own changes and see what happen if you change something and see the output 
Third step --> re-attempt to recreate in your own as a practice which gives an idea of how to program and how to create
 #This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user. In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message. The provided bitmap resembles a world map, but you can change this to any image you’d like. The binary simplicity of the space-or-message-characters system makes it good for beginners. Try experimenting with different messages to see what the results look like!

# Bitmap message(project 2)
This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user. In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message. The provided bitmap resembles a world map, but you can change this to any image you’d like. The binary simplicity of the space-or-message-characters system makes it good for beginners. Try experimenting with different messages to see what the results look like!

# Caesar cipher(project 3)

The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

 # Calendar maker(project 4)
 This program generates printable text files of monthly calendars for the month and year you enter. Dates and calendars are a tricky topic in programming because there are so many different rules for determining the number of days in a month, which years are leap years, and which day of the week a particular date falls on. Fortunately, Python’s datetime module handles these details for you. This program focuses on generating the multiline string for the monthly calendar page.

 # Collatz Sequence(project 5)
  
The Collatz sequence, also called the 3n + 1 problem, is the simplest impossible math problem. (But don’t worry, the program itself is easy enough for beginners.) From a starting number, n, follow three rules to get the next number in the sequence:

If n is even, the next number n is n / 2.
If n is odd, the next number n is n * 3 + 1.
If n is 1, stop. Otherwise, repeat.

# Digital stream(project 6)

This program mimics the “digital stream” visualization from the science fiction movie The Matrix. Random beads of binary “rain” stream up from the bottom of the screen, creating a cool, hacker-like visualization. (Unfortunately, due to the way text moves as the screen scrolls down, it’s not possible to make the streams fall downward without using a module such as Bext.)

# Factor finder(project 7)

A number’s factors are any two other numbers that, when multiplied by each other, produce the number. For example, 2 × 13 = 26, so 2 and 13 are factors of 26. Also, 1 × 26 = 26, so 1 and 26 are also factors of 26. Therefore, we say that 26 has four factors: 1, 2, 13, and 26.

# Fast draw(project 8)
This program tests your reaction speed: press ENTER as soon as you see the word DRAW. But be careful, though. Press it before DRAW appears, and you lose. Are you the fastest keyboard in the West?
# Guess anumber(project 9)

Guess the Number is a classic game for beginners to practice basic programming techniques. In this game, the computer thinks of a random number between 1 and 100. The player has 10 chances to guess the number. After each guess, the computer tells the player if it was too high or too low.
# Leetspeak(project 10)

There’s no better way to demonstrate your mad hacker skills than by replacing letters in your text with numbers: m4d h4x0r 5k1llz!!! This word program automatically converts plain English into leetspeak, the coolest way to talk online. Or at least it was in 1993.

It takes a while to get used to, but with some practice, you’ll eventually be able to read leetspeak fluently. For example, 1t +@]<3s 4 w|-|1le +o g37 |_|s3|) 70, b|_|+ y0u (an 3\/3nt|_|/-\lly r3a|) l33t$peak phl|_|3n+ly. Leetspeak may be hard to read at first, but the program itself is simple and good for beginners. More information about leetspeak can be found at https://en.wikipedia.org/wiki/Leet.

# Million dice roll Statistics Simulator(project 11)

When you roll two six-sided dice, there’s a 17 percent chance you’ll roll a 7. That’s much better than the odds of rolling a 2: just 3 percent. That’s because there’s only one combination of dice rolls that gives you 2 (the one that occurs when both dice roll a 1), but many combinations add up to seven: 1 and 6, 2 and 5, 3 and 4, and so on.

But what about when you roll three dice? Or four? Or 1,000? You could mathematically calculate the theoretical probabilities, or you can have the computer roll a number of dice one million times to empirically figure them out. This program takes that latter approach. In this program, you tell the computer to roll N dice one million times and remember the results. It then displays the percentage chance of each sum.

This program does a massive amount of computation, but the computation itself isn’t hard to understand.
