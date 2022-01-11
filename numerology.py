# Numerology from Pythagoras 

#################################### Functions ####################################
def lessthan9 (x):
    if (x>9):
        y1 = int(str(x)[0])
        y2 = int(str(x)[1])

        return (y1+y2)

    return (x)


def lessthan11 (x):
    if (x>11):
        y1 = int(str(x)[0])
        y2 = int(str(x)[1])

        return (y1+y2)
    return (x)

def lessthan9year(x):
    if (x>9):
        y1 = int(str(x)[0])
        y2 = int(str(x)[1])
        y3 = int(str(x)[2])
        y4 = int(str(x)[3])
        
        return (y1+y2+y3+y4)

    return (x)    

# Double check why this doesn't work
def age_checker (x):
    if (str(x)[0] == '0'):
        return (str(x)[1])

    return (x)


#################################### MAIN ####################################

print ('------------------------------------------')

d = age_checker (input ('Day of Birth?\n'))
m = age_checker (input ('Month of Birth?\n'))
y = input ('Year of Birth?\n')

# d  = 21
# m = 9
# y = 1997

# B1 - Birthdate organization
b1a = lessthan9(d)
b1b = lessthan9(m)
b1c = lessthan9 (lessthan9year(y))

# B2 - Pyramid Scheme
b2a = lessthan9 (b1b + b1a)
b2b = lessthan9 (b1a + b1c)
b2c = lessthan11 (b2a + b2b)

# B3 - Big triangle around
b3a = lessthan11 (b1b + b1c)


# B4 - Adding all of the numbers indvidually 
b4_str =  str (d) + str(m) + str(y)
b4_hold = 0

for i in range (len (b4_str)):
    b4_hold += int (b4_str [i])

b4 = lessthan9(b4_hold)

print ('------------------------------------------')

print ('Big Number %d' %b4)


# Analysis 
peak_ages = [0,0,0,0]
peak_ages [0]= 36 - b4
for i in range (1,4):
    peak_ages [i] = peak_ages [i-1] + 9

print ('------------------------------------------')
print ('First peak year age: %d' %peak_ages[0])
print ('First peak year theme: %d' %b2a)
print ('------------------------------------------')
print ('Second peak year age: %d' %peak_ages[1])
print ('Second peak year theme: %d' %b2b)
print ('------------------------------------------')
print ('Third peak year age: %d' %peak_ages[2])
print ('Third peak year theme: %d' %b2c)
print ('------------------------------------------')
print ('Fourth peak year age: %d' %peak_ages[3])
print ('Fourth peak year theme: %d' %b3a)
print ('------------------------------------------')