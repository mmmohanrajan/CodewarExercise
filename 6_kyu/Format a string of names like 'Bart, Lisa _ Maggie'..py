__author__ = 'mohan'

'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

'''


def namelist(names):
    s = ", ".join(d['name'] for d in names)
    if ',' in s:
        index = s.rindex(',')
        s = s[:index] + ' &' + s[index+1:]
    return s


def namelist_1(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


# 196

def namelist_6(names):
    return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]


# 84

def namelist_2(names):
    if len(names) == 0: return ''
    if len(names) == 1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


# 67

def namelist_10(names):
    names = [name['name'] for name in names]
    return ', '.join(names) if len(names) < 2 else ', '.join(names[:-1]) + ' & {}'.format(names[-1])


# 13

def namelist_4(names):
    return " ".join([names[i]["name"] + (" &" if i == len(names) - 2 else "" if i == len(names) - 1 else ",") for i in
                     range(len(names))])


# 12

def namelist_3(names):
    l = []
    if len(names) == 0:
        return ''
    else:
        for name in names:
            l.append(''.join(name.values()))
        str = ', '
        if len(l) == 1:
            return l[0]
        else:
            return str.join(l[:-1]) + ' & ' + l[-1]


# 8

def namelist_5(names):
    return ((", ".join(n['name'] for n in names[:-1]) + " & ") if len(names) > 1 else '') + (
    names[-1]['name'] if len(names) > 0 else '')


# 6

def namelist_12(names):
    return ", ".join(person["name"] for person in (names if len(names) < 2 else names[:-1])) + (
    " & " + names[-1]["name"] if len(names) > 1 else "")


# 5

def namelist_7(names):
    names_lst = []
    for i in range(len(names)):
        names_lst.append(names[i]['name'])
    names_str = ''
    for i in range(len(names_lst)):
        names_str += names_lst[i]
        if i < len(names_lst) - 2:
            names_str += ', '
        elif i == len(names_lst) - 2:
            names_str += ' & '
    return names_str


# 3

def namelist_9(names):
    name_str = ''
    if (len(names) > 0):
        for i in xrange(0, len(names)):
            if (i == len(names) - 1 and i > 0):
                name_str += " & "
            elif (i > 0):
                name_str += ", "
            name_str += names[i]['name']
    return name_str


# 3

def namelist_8(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    return ', '.join(y for y in (x['name'] for x in names[:-1])) + " & " + names[-1]['name']


# 2

def namelist_11(names):
    str = ''
    num_names = len(names)
    for i, x in enumerate(names):
        if i < num_names - 2:
            str += '{}, '.format(x['name'])
        elif i == num_names - 2:
            str += '{} & '.format(x['name'])
        else:
            str += x['name']
    return str


# 1

def namelist_13(names):
    names = [d['name'] for d in names]
    return '' if not names else ', '.join(names[:-2]) + ', ' * (len(names) > 2) + ' & '.join(names[-2:])

    # 1


def namelist_16(names):
    ans = ""
    # print names, len(names)
    l = len(names)
    if l == 0:
        return ""
    elif l == 1:
        return names[0].values()[0]
    else:
        for i in range(l - 2):
            # print i, names[i], type(i), type(names[i]), names[i].values()
            ans = ans + str(names[i].values()[0]) + ', '
            # return names[0].values()[0]
        ans = ans + names[l - 2].values()[0] + ' & '
        ans = ans + names[l - 1].values()[0]
        return ans

        # 1


def namelist_17(names):
    if names == None or len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    else:
        namelist = ''
        for i in range(0, len(names)):
            if i != len(names) - 2 and i != len(names) - 1:
                add = names[i]['name'] + ', '
                namelist += add
            elif i == len(names) - 2:
                add = names[i]['name'] + ' '
                namelist += add
            else:
                add = '& ' + names[i]['name']
                namelist += add
        return namelist


# 1

def namelist_18(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))


# 1

def namelist_19(names):
    phrase = ''
    if (len(names) == 0):
        return ''
    for person in names:
        phrase += person['name']
        if (len(names) == 1):
            return phrase
        if (person['name'] == names[-2]['name']):
            phrase += ' & '
        elif (person['name'] != names[-1]['name']):
            phrase += ', '
    return phrase


# 1

def namelist_20(names):
    dictValue = []
    list = ""
    a = 0

    if len(names) > 1:
        for x in names:
            for x in names[a].values():
                dictValue.append(x)
            a += 1

        list = " & ".join(str(e) for e in dictValue)
        list = list.replace(" & ", ", ", (a - 2))

    elif len(names) == 0:
        list = ''

    else:
        dictValue = names[0].values()
        list = list.join(dictValue)
    return list


# 1
input = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
print namelist_1(input)
print namelist_2(input)
print namelist_3(input)
print namelist_4(input)
print namelist_5(input)
print namelist_6(input)
print namelist_7(input)
print namelist_8(input)
print namelist_9(input)
print namelist_10(input)
print namelist_11(input)
print namelist_12(input)
print namelist_13(input)
print namelist_16(input)
print namelist_17(input)
print namelist_18(input)
print namelist_19(input)
print namelist_20(input)

