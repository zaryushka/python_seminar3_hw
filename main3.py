# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
eng = {'A, E, I, O, U, L, N, S, T, R':1, 'D, G':2, 'B, C, M, P':3, 'F, H, V, W, Y':4, 'K':5, 'J, X':8, 'Q, Z':10}
rus = {'А, В, Е, И, Н, О, Р, С, Т':1, 'Д, К, Л, М, П, У':2, 'Б, Г, Ё, Ь, Я':3, 'Й, Ы':4, 'Ж, З, Х, Ц, Ч':5, 'Ш, Э, Ю':8, 'Ф, Щ, Ъ':10}
str = input('введите слово на английском языке:').upper()
list = []
for i in range(len(str)):
    if str[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in eng.keys():
            if str[i] in j:
                list.append(eng[j])
    else:
        for g in rus.keys():
            if str[i] in g:
                list.append(rus[g])
print(sum(list))