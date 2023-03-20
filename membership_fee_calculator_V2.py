import psycopg2

conn = psycopg2.connect(database="flatfair",
                        user= 'x', #usually postgres, please confirm the username for your local postgresql instance
                        password= 'x', #Kindly use the password for your local postgresql instance
                        port=5432)
cursor = conn.cursor()

def calculate_membership_fee(rent_amount, rent_period, organisation_unit):
    vat = 0.2
    min_mem_fee = 120
    min_week_rent = 25
    max_week_rent = 2000
    min_month_rent = 110
    max_month_rent = 8660


    cursor.execute("""SELECT has_fixed_membership, fixed_membership_fee 
                        FROM OrganisationUnit
                        where name = '%s'""" % (organisation_unit))
    config = cursor.fetchone()
    
    if config[0] == True:
        return config[1]
    elif config[0] == False:
        if rent_period == 'week':
            if rent_amount < min_week_rent or rent_amount > max_week_rent:
                raise ValueError('Rent Amount Limits Exceeded')
            else:
                if rent_amount > min_mem_fee:
                    membership_fee = rent_amount + (vat * rent_amount)
                    return int(membership_fee)
                elif rent_amount < min_mem_fee:
                    membership_fee = min_mem_fee + (vat * min_mem_fee)
                    return int(membership_fee)
        elif rent_period == 'month':
            if rent_amount < min_month_rent or rent_amount > max_month_rent:
                raise ValueError('Rent Amount Limits Exceeded')
            else:
                rent_amount = rent_amount/4
                if rent_amount > min_mem_fee:
                    membership_fee = rent_amount + (vat * rent_amount)
                    return int(membership_fee)
                elif rent_amount < min_mem_fee:
                    membership_fee = min_mem_fee + (vat * min_mem_fee)
                    return int(membership_fee)
        else: raise ValueError('Only month or week allowed')        
    elif config[0] == None:
        cursor.execute(""" WITH RECURSIVE OrganisationUnit_cte AS (
                        SELECT
                            has_fixed_membership,
                            fixed_membership_fee,
                            parent,
                            id
                        FROM OrganisationUnit
                        WHERE name = '%s'
                        UNION ALL
                            SELECT ci.has_fixed_membership, ci.fixed_membership_fee, ci.parent, ci.id
                            FROM OrganisationUnit ci
                            JOIN OrganisationUnit_cte p
                            ON p.parent = ci.id
                        )SELECT *
                        FROM OrganisationUnit_cte 
                        WHERE has_fixed_membership = True;""" %(organisation_unit))
        config = cursor.fetchone()

        if config[1]:
            return config[1]
        elif config[1] == None:
            if rent_period == 'week':
                if rent_amount < min_week_rent or rent_amount > max_week_rent:
                    raise ValueError('Rent Amount Limit Exceeded')
                else:
                    if rent_amount > min_mem_fee:
                        membership_fee = rent_amount + (vat * rent_amount)
                        return int(membership_fee)
                    elif rent_amount < min_mem_fee:
                        membership_fee = min_mem_fee + (vat * min_mem_fee)
                        return int(membership_fee)
            elif rent_period == 'month':
                if rent_amount < min_month_rent or rent_amount > max_month_rent:
                    raise ValueError('Rent Amount Limit Exceeded')
                else:
                    rent_amount = rent_amount/4
                    if rent_amount > min_mem_fee:
                        membership_fee = rent_amount + (vat * rent_amount)
                        return int(membership_fee)
                    elif rent_amount < min_mem_fee:
                        membership_fee = min_mem_fee + (vat * min_mem_fee)
                        return int(membership_fee)
            else: raise ValueError('Only month or week allowed') 



