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
        print(total)



"""計算欄
startwithメゾットについて、今回は
'D'で始まっていたらTrue、そうでなければFalseを返す
find('b')メッソドについて、bが最初にみつかったインデックスであればできる。

"""
