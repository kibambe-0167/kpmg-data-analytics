# func
def freq_dis( column ):
    '''returns a frequency distribution of a column.'''
    d = {}
    for i in list(column):
        if i in d.keys(): d[i] += 1
        else: d[i] = 1
    # sort by value.
    d = dict( sorted(d.items(), key=lambda x: x[1] ))
    return d

def validate_date_year(d):
    '''validate date for analysis. check for dates that are more than 100 year old and to find outlines.'''
    current_year = 2023
    invalide_dates = {}
    for i in list(d):
        if i and len(i) > 0:
            if (current_year - int(i.split('-')[0])) > 100:
                if i in invalide_dates.keys():
                    invalide_dates[i] += 1
                else:
                    invalide_dates[i] = 1
    return invalide_dates

def validate_date_month_day(d):
    '''validate the month and day of the month from the data.'''
    invalide_dates = {}
    for i in list(d):
        if i and len(i) > 0:
            if not(int(i.split('-')[1]) > 0 and int(i.split('-')[1]) < 13) or not(int(i.split('-')[2]) > 0 and int(i.split('-')[2]) < 32):
                if i in invalide_dates.keys():
                    invalide_dates[i] += 1
                else:
                    invalide_dates[i] = 1
    return invalide_dates