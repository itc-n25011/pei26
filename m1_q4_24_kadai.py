animals = ['Dog', 'Cat', 'Rabbit','Hors','Dlphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
    else:
        total += len(animal)
        print('totalの値は',total)

        print(total)



'''計算欄
startwithメゾットについて、今回は
'D'で始まっていたらTrue、そうでなければFalseを返す
find('b')メッソドについて、bが最初にみつかったインデックスを返す。見つからなければ

animal from_D is long 処理
'Dog' True False total += len(animal) 3
'Cat' False False total += len(animal) 3
'Rabbit' False True total += animal.find('b') インデックスを返すので 2
'Dolphin' True True break

'''
