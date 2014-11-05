#!/usr/env python

##########################################################################################
def find_last(field):  #returns last populated position in field
    pos = 0
    last = 0
    for e in field:
        if e != ' ':
            last = pos
            pos = pos + 1
        else:
            pos = pos + 1
    return last


def all_blank(field):  #returns True if empty field
    test = True
    for e in field:
        if e != ' ':
            test = False
    return test

def make_csv(input_file,out_file):
    delim = ','
    fields = [30, 20, 1, 10, 10, 60, 60, 30, 2, 5, 4, 6, 3, 4, 5, 50, 30, 
              1, 12, 1, 2, 5, 12, 2, 12, 20, 1, 1, 10, 2, 1, 38]
    end = len(fields)
    headers_list = ['LAST NAME','FIRST NAME','MI','TITLE','SUFFIX','PRIMARY ADDRESS','SECONDARY ADDRESS',
                    'CITY','ST','ZIP','PLUS4','FILLER','DPV','CRRT','LOT','COMPANY','PROF TITLE','GENDER',
                    'VERSION','INTERNAL','INTERNAL','INTERNAL','INTERNAL','PANEL','KEYCODE','FINDER NUM',
                    'INTERNAL','INTERNAL','INTERNAL','INTERNAL','INTERNAL','MAIL DATE']
    headers = ','.join(headers_list)
    fields_list = [[0, 30], [30, 50], [50, 51], [51, 61], [61, 71], [71, 131], 
                    [131, 191], [191, 221], [221, 223], [223, 228], [228, 232], 
                    [232, 238], [238, 241], [241, 245], [245, 250], [250, 300], 
                    [300, 330], [330, 331], [331, 343], [343, 344], [344, 346], 
                    [346, 351], [351, 363], [363, 365], [365, 377], [377, 397], 
                    [397, 398], [398, 399], [399, 409], [409, 411], [411, 412], 
                    [412, 450]]
    out_file.write(headers + '\n')  #write headers as first line in fname
    for line in input_file:
        count = 0    
        for field in fields_list:
            count = count + 1
            if all_blank(line[field[0]:field[1]]):  #check for empty field
                if count == end:
                    out_file.write('\n') #carrage return if last field
                else:
                    out_file.write(delim)  #write delimiter if empty field
            else:
                last = find_last(line[field[0]:field[1]]) + 1  #find last populated position in field
                if count == end:
                    out_file.write(line[field[0]:field[0] + last] + '\n') #carrage return if last field
                else:
                    out_file.write(line[field[0]:field[0] + last] + delim) #delimiter if not last field


def make_csv_email(input_file,out_file):
    delim = ','
    fields = [30, 20, 1, 10, 10, 60, 60, 30, 2, 5, 4, 6, 3, 4, 5, 50, 30, 
              1, 12, 1, 2, 5, 12, 2, 12, 20, 1, 1, 10, 2, 1, 38, 90]
    end = len(fields)
    headers_list = ['LAST NAME','FIRST NAME','MI','TITLE','SUFFIX','PRIMARY ADDRESS','SECONDARY ADDRESS',
                    'CITY','ST','ZIP','PLUS4','FILLER','DPV','CRRT','LOT','COMPANY','PROF TITLE','GENDER',
                    'VERSION','INTERNAL','INTERNAL','INTERNAL','INTERNAL','PANEL','KEYCODE','FINDER NUM',
                    'INTERNAL','INTERNAL','INTERNAL','INTERNAL','INTERNAL','MAIL DATE','EMAIL']
    headers = ','.join(headers_list)
    fields_list = [[0, 30], [30, 50], [50, 51], [51, 61], [61, 71], [71, 131], 
                    [131, 191], [191, 221], [221, 223], [223, 228], [228, 232], 
                    [232, 238], [238, 241], [241, 245], [245, 250], [250, 300], 
                    [300, 330], [330, 331], [331, 343], [343, 344], [344, 346], 
                    [346, 351], [351, 363], [363, 365], [365, 377], [377, 397], 
                    [397, 398], [398, 399], [399, 409], [409, 411], [411, 412], 
                    [412, 450],[450, 540]]
    out_file.write(headers + '\n')  #write headers as first line in fname
    for line in input_file:
        count = 0    
        for field in fields_list:
            count = count + 1
            if all_blank(line[field[0]:field[1]]):  #check for empty field
                if count == end:
                    out_file.write('\n') #carrage return if last field
                else:
                    out_file.write(delim)  #write delimiter if empty field
            else:
                last = find_last(line[field[0]:field[1]]) + 1  #find last populated position in field
                if count == end:
                    out_file.write(line[field[0]:field[0] + last] + '\n') #carrage return if last field
                else:
                    out_file.write(line[field[0]:field[0] + last] + delim) #delimiter if not last field


