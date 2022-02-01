import random


rw = ['scissors', 'rock', 'paper']  # rw (random weapon)
uc = ''
u_points = 0  # user points
c_points = 0  # computer poins


while uc != 'exit':
    cc = random.choice(rw)  # cc (computer choice)

    # użytkownik wybiera broń + sprawdzam czy wybrał legitnie
    uc = input("Choose wisely - rock, paper, or scissors? :\n")  # uc (user choice)
    if uc not in rw:
        print('Ohh crap. You mistyped. Try one more time! \n '
              '"You have to choose weapon! - paper, scissors or rock \n')
        continue

    # sprawdzam kto wygrał
    if uc == cc:
        print(f'user {uc} vs computer {cc}\n'
              f'Tie!! \nuser {u_points} : {c_points} computer\n')
        continue
    elif uc == 'rock' and cc == 'scissors' or uc == 'rock' and cc == 'scissors' or uc == 'scissors' and cc == 'paper':
        win = 'user'
        u_points += 1
    else:
        win = 'computer'
        c_points += 1
    # Poprzednia wesja kodu
    '''
    elif uc == 'rock' and cc == 'scissors':
        win = 'user'
        u_points += 1
    elif uc == 'paper' and cc == 'rock':
        win = 'user'
        u_points += 1
    elif uc == 'scissors' and cc == 'paper':
        win = 'user'
        u_points += 1
    '''
    print(f'user {uc} vs computer {cc}\n'
          f'The winner is {win} \n'
          f'user {u_points} : {c_points} computer\n')

    if u_points == 3 or c_points == 3:
        print(f'The final winner is: {win} \nThank you for the game!')
        break
