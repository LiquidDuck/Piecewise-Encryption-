
def normalize(file_name):
    file=open(file_name)
    file_list=[]
    for line in file:
        line=line.strip()
        file_list.append(line)
    lines=file_list[0]
    file_list=file_list[1:]
    for i in range (len(file_list)):
        if "" in file_list:
            file_list.remove("")
    return [file_list, lines]
    

def a_through_e(character):
    character=character+6
    return (character)

def f_through_j(character):
    character=character*character
    return (character)

def k_through_o(character):
    variable=character%3
    variable=variable*5
    variable=variable+1
    return (variable)

def p_through_t(character):
    variables=[int(i) for i in str(character)]
    variable=0
    count=0
    while True:
        variable=variable+variables[count]
        if count==(len(variables))-1:
            break
        count=count+1
        
    variable=variable*8
    return (variable)
        
def u_through_z(character):
    factor_list=[]
    for i in range(1, character + 1):
       if character % i == 0:
           factor_list.append(i)
    variable= factor_list[-2]
    variable=variable*2
    return (variable)


def encryption(universial_dictionary):
    range_1=["A","B","C","D","E"]
    range_2=["F","G","H","I","J"]
    range_3=["K","L","M","N","O"]
    range_4=["P","Q","R","S","T"]
    range_5=["U","V","W","X","Y","Z"]
    for character in universial_dictionary:
        if character in range_1:
            universial_dictionary[character]=a_through_e(universial_dictionary[character])
        if character in range_2:
            universial_dictionary[character]=f_through_j(universial_dictionary[character])
        if character in range_3:
            universial_dictionary[character]=k_through_o(universial_dictionary[character])
        if character in range_4:
            universial_dictionary[character]=p_through_t(universial_dictionary[character])
        if character in range_5:
            universial_dictionary[character]=u_through_z(universial_dictionary[character])
    return universial_dictionary
    
def refine(universial_dictionary):
    for letter in universial_dictionary:
        if universial_dictionary[letter] > 26:
            universial_dictionary[letter]=universial_dictionary[letter]%26
    return universial_dictionary
    
def any_zeroes(universial_dictionary, backwards_alphabet_dictionary):
    for letter in universial_dictionary:
        if universial_dictionary[letter] == 0:
            universial_dictionary[letter]=backwards_alphabet_dictionary[letter]
    return universial_dictionary
    
def output(universial_dictionary, alphabet_dictionary, file_list):
    for row in range(len(file_list)):
        new_row=list(file_list[row])
        statement=""
        for letter in new_row:
            variable=universial_dictionary[letter]
            statement=statement + alphabet_dictionary[variable]
        print(statement)
        
alphabet_dictionary={
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H",
    9:"I",
    10:"J",
    11:"K",
    12:"L",
    13:"M",
    14:"N",
    15:"O",
    16:"P",
    17:"Q",
    18:"R",
    19:"S",
    20:"T",
    21:"U",
    22:"V",
    23:"W",
    24:"X",
    25:"Y",
    26:"Z"
}

backwards_alphabet_dictionary={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26
}

universial_dictionary={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26
}

file_data=normalize("Prob15.in.txt")

file_list=file_data[0]

num_of_lines=file_data[1]

universial_dictionary= encryption(universial_dictionary)


universial_dictionary=refine(universial_dictionary)

universial_dictionary=any_zeroes(universial_dictionary, backwards_alphabet_dictionary)

output(universial_dictionary, alphabet_dictionary, file_list)