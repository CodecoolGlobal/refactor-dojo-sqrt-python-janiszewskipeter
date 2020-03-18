# import random - nie potrzebny
import math
# funkcja daje sumę pierwiastków kwadratowych z sumy liczb z kazdej linijki 
sqrt = 0
dictionary = {}


def read_file():
    with open('100.txt') as file:
        data = file.read()
        return data


def built_dictionary(data):
    for elem in file: # bierze duzy element(23,21,5)----> 23
        place_holder = ''
        for small_elem in elem: # bierze maly element czyli najpierw -->2
            elemnt_stripped = elem.strip() # usuwamy newline na koncu
            if small_elem != ',': # jezeli 2 nie jest przecinkiem to '' = 2
                place_holder += small_elem # dodaj cyfe do place_holdera
            else:
                if elemnt_stripped not in dictionary:
                    dictionary[elemnt_stripped] = int(place_holder)
                else:
                    dictionary[elemnt_stripped] += int(place_holder)
                place_holder = ''
        if elemnt_stripped not in dictionary: # do refaktoringu
            dictionary[elemnt_stripped] = int(place_holder)
        else:
            dictionary[elemnt_stripped] += int(place_holder)

            
def print_sqrt():
    finall2 = 0
    for values in dictionary.values():
        finall = math.sqrt(values)
        finall2 += finall
    print(finall2)

# sqrt += math.sqrt(dictionary['23,21,5'])
# sqrt += math.sqrt(dictionary['342,2,5'])
# sqrt += math.sqrt(dictionary['32,1,777'])
# sqrt += math.sqrt(dictionary['234,645,223'])
# sqrt += math.sqrt(dictionary['243,646,2342'])
# sqrt += math.sqrt(dictionary['6346,3434,222'])
# sqrt += math.sqrt(dictionary['3,6,2'])


