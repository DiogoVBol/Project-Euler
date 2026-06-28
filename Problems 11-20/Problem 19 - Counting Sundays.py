# %%

inicial_year = 1901
final_year = 2000

def is_leap_year(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Dias da semana (Ref)
# 0 - Domingo
# 1 - Segunda
# 2 - Terça
# 3 - Quarta
# 4 - Quinta
# 5 - Sexta 
# 6 - Sábado

months = [31,28,31,30,31,30,31,31,30,31,30,31]
months_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

total_sundays = 0

start = 2 # Tuesday

for i in range(inicial_year, final_year+1):

    if not is_leap_year(i):

        for indice,days in enumerate(months):

            if start == 0:
                total_sundays += 1
        
            first_day_next_month = (start + days) % 7

            start = first_day_next_month
    
    else:

        for indice,days in enumerate(months_leap):

            if start == 0:
                total_sundays += 1
        
            first_day_next_month = (start + days) % 7

            start = first_day_next_month

      
total_sundays