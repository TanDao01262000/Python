

# Convert the tone notes to harmonica tab
def tab_converting(note_list):
    tab_converted = []
    for note in note_list:
        if note.upper() == 'SOL-1' or note.upper() == 'SOL-1\n':
            tab_converted.append('1')
        if note.upper() == 'RE0':
            tab_converted.append('2')
        if note.upper() == 'DO0':
            tab_converted.append('3')
        if note.upper() == 'FA0':
            tab_converted.append('4')
        if note.upper() == 'MI0':
            tab_converted.append('5')
        if note.upper() == 'LA0':
            tab_converted.append('6')
        if note.upper() == 'SOL0':
            tab_converted.append('7')
        if note.upper() == 'SI0':
            tab_converted.append('8')
        if note.upper() == 'DO':
            tab_converted.append('9')
        elif note.upper() == 'RE':
            tab_converted.append('10')
        elif note.upper() == 'MI':
            tab_converted.append('11')
        elif note.upper() == 'FA':
            tab_converted.append('12')
        elif note.upper() == 'SOL':
            tab_converted.append('13')
        elif note.upper() == 'LA' :
            tab_converted.append('14')
        elif note.upper() == 'DO2':
            tab_converted.append('15')
        elif note.upper() == 'SI' or note.upper() == 'SIB':
            tab_converted.append('16')
        elif note.upper() == 'MI2':
            tab_converted.append('17')
        elif note.upper() == 'RE2':
            tab_converted.append('18')
        elif note.upper() == 'SOL2':
            tab_converted.append('19')
        elif note.upper() == 'FA2':
            tab_converted.append('20')
        elif note.upper() == 'DO3':
            tab_converted.append('21')
        elif note.upper() == 'LA2':
            tab_converted.append('22')
        elif note.upper() == 'MI3':
            tab_converted.append('23')
        elif note.upper() == 'SI2' or note.upper() == 'SIB2':
            tab_converted.append('24')
        elif note.upper() == 'DO,':
            tab_converted.append('9,')
        elif note.upper() == 'RE,':
            tab_converted.append('10,')
        elif note.upper() == 'MI,':
            tab_converted.append('11,')
        elif note.upper() == 'FA,':
            tab_converted.append('12,')
        elif note.upper() == 'SOL,':
            tab_converted.append('13,')
        elif note.upper() == 'LA,':
            tab_converted.append('14,')
        elif note.upper() == 'DO2,':
            tab_converted.append('15,')
        elif note.upper() == 'SI,'or note.upper() == 'SIB,':
            tab_converted.append('16,')
        elif note.upper() == 'MI2,':
            tab_converted.append('17,')
        elif note.upper() == 'RE2,':
            tab_converted.append('18,')
        elif note.upper() == 'SOL2,':
            tab_converted.append('19,')
        elif note.upper() == 'FA2,':
            tab_converted.append('20,')
        elif note.upper() == 'DO3,':
            tab_converted.append('21,')
        elif note.upper() == 'LA2,':
            tab_converted.append('22,')
        elif note.upper() == 'MI3,':
            tab_converted.append('23,')
        elif note.upper() == 'SI2,' or note.upper() == 'SIB2,':
            tab_converted.append('24,')
        elif note.upper() == 'NONE':
            tab_converted.append('')
        elif note.upper() == ",":
            tab_converted.append(',')
        elif note.upper() == "-":
            tab_converted.append('-')
    return tab_converted