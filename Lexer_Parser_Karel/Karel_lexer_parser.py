import re

def tokenize(line, types):
    l = line.split(' ')
    dic = {}
    for j in range(len(l)):
        l[j] = l[j].rstrip()
        # print(len(l[j]), l[j], type(l[j]))
        if(l[j] != '' and l[j][-1] == ';'):
            l[j] = l[j][:-1]
            l.append(';')
    for k in l:
        if(k != ''):
            for m in types:
                if(k in types[m]):
                    dic[k] = m

    return dic

# TYPES - Lexico

primitive = ['move', 'turnleft', 'pickbeeper', 'putbeeper', 'turnoff']
instr_block = ['BEGINNING-OF-PROGRAM', 'BEGINNING-OF-EXECUTION', 'BEGIN',
              'END', 'END-OF-EXECUTION', 'END-OF-PROGRAM']
conditional = ['IF', 'THEN', 'ELSE']
loops = ['ITERATE', 'TIMES', 'WHILE', 'DO']
new_instr = ['DEFINE-NEW-INSTRUCTION', 'AS']
propositions = ['front-is-clear', 'front-is-blocked',
              'left-is-clear', 'left-is-blocked',
              'right-is-clear', 'right-is-blocked',
              'next-to-a-beeper', 'not-next-to-a-beeper',
              'facing-north', 'not-facing-north',
              'facing-south', 'not-facing-south',
              'facing-east', 'not-facing-east',
              'facing-west', 'not-facing-west',
              'any-beepers-in-beeper-bag', 'no-beepers-in-beeper-bag']
puntuation = [';']

types = {'primitive':primitive, 'instr_block':instr_block,
         'conditional':conditional, 'loops':loops,
         'new_instr':new_instr, 'propositions':propositions,
         'puntuation':puntuation}


# REGULAR EXPRESSIONS - Sintaxis

# Primitive Instructions
mv = r'^[\s]*move[\s]*$'
tl = r'^[\s]*turnleft[\s]*$'
pk = r'^[\s]*pickbeeper[\s]*$'
pt = r'^[\s]*putbeeper[\s]*$'
tf = r'^[\s]*turnoff[\s]*$'

# Instructions Block
BP = r'^BEGINNING-OF-PROGRAM[\s]*$'
BE = r'^[\s]*BEGINNING-OF-EXECUTION[\s]*$'
EE = r'^[\s]*END-OF-EXECUTION[\s]*$'
EP = r'^END-OF-EXECUTION[\s]*$'
B = r'^[\s]*BEGIN[\s]*$'
E = r'^[\s]*END[\s]*$'

# Conditional
IfTh = r'^[\s]*IF\s[^\d](.*)\sTHEN[\s]*$'
El = r'^[\s]*ELSE[\s]*$'

# Loops
InT = r'^[\s]*ITERATE\s[\d]+\sTIMES[\s]*$'
WhD = r'^[\s]*WHILE\s[^\d](.*)\sDO[\s]*$'

# New Instructions
DNI = r'^[\s]*DEFINE-NEW-INSTRUCTION\s[A-Za-z]([A-Za-z0-9]*)\sAS[\s]*$'
mobj = re.match(DNI, 'DEFINE-NEW-INSTRUCTION turnright AS')
print(mobj)

# Conditions - QUESTION
fic = r'^[\s]*front-is-clear[\s]*$'
# ......)



# READ PROGRAM
file = open('program.txt', 'r')
lines = file.readlines()
for i in lines:
    l = tokenize(i, types)
