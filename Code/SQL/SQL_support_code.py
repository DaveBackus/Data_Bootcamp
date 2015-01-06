import pandas as pd
import sqlite3
import xlrd as xl


# Set up a SQLite database using several .csv files:

# if this .sqlite db doesn't already exists, this will create it
# if the .sqlite db *does* already exist, this establishes the desired connection
con = sqlite3.connect("sqlite_cars.sqlite")

# create dataframes from each .csv file:
sales_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/sales_table.csv')
car_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/car_table.csv')
salesman_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/salesman_table.csv')
cust_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/cust_table.csv')
# make a list of the tables (dataframes) and table names:
tables = [sales_table, car_table, salesman_table, cust_table]
table_names = ['sales_table', 'car_table', 'salesman_table', 'cust_table']
# drop each table name if it already exists to avoid error if you rerun this bit of code
# then add it back (or for the first time, if the table didn't already exist)
for i in range(len(tables)):
    table_name = table_names[i]
    table = tables[i]
    con.execute("DROP TABLE IF EXISTS {}".format(table_name))
    pd.io.sql.to_sql(table, "{}".format(table_name), con, index=False)



# Function to make it easy to run queries on this mini-database
def run(query):
    results = pd.read_sql("{}".format(query), con)
    return results


# setup join lesson DB
path = ('../SQL/join_examples.xlsx')
table_names = xl.open_workbook(path).sheet_names()
for table in table_names:
    df = pd.read_excel(path, sheetname='{}'.format(table))
    con.execute("DROP TABLE IF EXISTS {}".format(table))
    pd.io.sql.to_sql(df, "{}".format(table), con, index=False)

# show compatibility with joins and different DBs 
join_df_index = ['JOIN or INNER JOIN', 'LEFT JOIN or LEFT OUTER JOIN', 'RIGHT JOIN or RIGHT OUTER JOIN', 'OUTER JOIN or FULL OUTER JOIN']
join_df = pd.DataFrame({'SQLite' : pd.Series(['✓', '✓', 'not supported', 'not supported'], index=join_df_index),
                        'MySQL' : pd.Series(['✓', '✓', '✓', 'not supported'], index=join_df_index),
                        'Microsoft SQL Server' : pd.Series(['✓','✓','✓','✓'], index=join_df_index),
                        'Oracle' : pd.Series(['✓','✓','✓','✓'], index=join_df_index)})

# show concat options: 
concat_df_index = ['Concatenating']
concat_df = pd.DataFrame({'SQLite' : pd.Series(['||'], index=concat_df_index),
                        'MySQL' : pd.Series(['CONCAT(column_a, column_b)'], index=concat_df_index),
                        'Microsoft SQL Server' : pd.Series(['CONCAT(column_a, column_b) or +'], index=concat_df_index),
                        'Oracle' : pd.Series(['CONCAT(column_a, column_b) or ||'], index=concat_df_index)})
# show limit options
limit_df_index = ['LIMITING']
limit_df = pd.DataFrame({'SQLite' : pd.Series(['LIMIT N'], index=limit_df_index),
                        'MySQL' : pd.Series(['LIMIT N'], index=limit_df_index),
                        'Microsoft SQL Server' : pd.Series(['SELECT TOP N column_a...'], index=limit_df_index),
                        'Oracle' : pd.Series(['WHERE ROWNUM <=N'], index=limit_df_index)})

# show describe options
describe_index = ['Reading a table']
describe_df = pd.DataFrame({'SQLite' : pd.Series(['PRAGMA TABLE_INFO(table_name)'], index=describe_index), 
							'MySQL' : pd.Series(['DESCRIBE table_name'], index=describe_index),
							'Microsoft SQL Server' : pd.Series(['SP_HELP table_name'], index=describe_index),
							'Oracle' : pd.Series(['DESCRIBE table_table'], index=describe_index)})

describe_cheat = '''PRAGMA TABLE_INFO(car_table)'''

select_cheat1 = '''
    SELECT 
        *
    FROM 
        car_table
    '''

select_cheat2 = '''
    SELECT
        model_id, 
        model
    FROM
        car_table
'''

select_cheat3 = '''
    SELECT 
        DISTINCT salesman_id
    FROM
        sales_table
'''

where_cheat1 = '''
    SELECT
        *
    FROM
        sales_table
    WHERE
        payment_type != 'cash'
        AND model_id IN (31,36)     
    '''

where_cheat2 = '''
    SELECT
        *
    FROM
        sales_table
    WHERE
        revenue BETWEEN 24000 AND 25000
    '''

where_cheat3 = '''
    SELECT 
        *
    FROM
        car_table
    WHERE
        model LIKE 'out%'
    '''

order_cheat = '''
    SELECT
        *
    FROM
        car_table
    ORDER BY
        sticker_price DESC
    '''


alias_cheat = '''
    SELECT
        model_id AS Model,
        revenue AS Rev
    FROM
        sales_table
    WHERE
        Model = 36
    ORDER BY
        Rev DESC
    '''

join_cheat1 = '''
    SELECT
        *
    FROM
        sales_table
        JOIN cust_table on sales_table.customer_id = cust_table.customer_id
    '''

join_cheat2 = '''
    SELECT
        gender,
        revenue
    FROM
        sales_table
        JOIN cust_table on sales_table.customer_id = cust_table.customer_id
    '''

join_cheat3 = '''
    SELECT
        sales_table.customer_id,
        gender,
        revenue
    FROM
        sales_table
        JOIN cust_table on sales_table.customer_id = cust_table.customer_id
    
    **OR**
    
    SELECT
        cust_table.customer_id,
        gender,
        revenue
    FROM
        sales_table
        JOIN cust_table on sales_table.customer_id = cust_table.customer_id
    '''

join_cheat4 = '''
    SELECT
        *
    FROM
        sales_table
        JOIN salesman_table ON sales_table.salesman_id = salesman_table.id
    '''


join_cheat5 = '''
    SELECT
        S.id AS transaction_id,
        S.salesman_id as sales_table_salesman_id,
        SM.id as salesman_table_id
    FROM
        sales_table AS S
        JOIN salesman_table AS SM ON S.salesman_id = SM.id
    '''

inner_join_cheat = '''    
	SELECT
        *
    FROM
        Dog_Table D
        JOIN Cat_Table C ON D.Owner_Name = C.Owner_Name
    
    -- OR, to make it cleaner --
    
    SELECT
    	D.Owner_Name, Dog_Name, Cat_Name
    FROM
        Dog_Table D
        JOIN Cat_Table C ON D.Owner_Name = C.Owner_Name
    '''

left_join_cheat = '''
    SELECT
        *
    FROM
        Dog_Table D
        LEFT JOIN Cat_Table C ON D.Owner_Name = C.Owner_Name
	
	-- OR, to make it cleaner --
	
	SELECT
    	C.Owner_Name, Cat_Name, Dog_Name
    FROM
        Dog_Table D
        LEFT JOIN Cat_Table C ON D.Owner_Name = C.Owner_Name
    '''

# this one is almost unfair. Since SQLite is using integers you have to convert it to a floating point instead of an integer
operator_cheat = '''
    SELECT
        S.id,
        C.model, 
        S.revenue,
        C.cogs,
        (S.revenue - C.cogs)*1.0/(C.cogs) AS gross_profit
    FROM
        sales_table S 
        JOIN car_table C on S.model_id = C.model_id
    LIMIT 5 
	'''
	
concat_cheat = '''
	SELECT
        model|| ' (' || make || ')' AS "Model (Make)"
    FROM
        car_table
    '''

avg_cheat = '''
    SELECT 
        ROUND(AVG(cogs), 2) AS AVG_COGS
    FROM
        car_table
    '''
count_cheat = '''
	SELECT 
        COUNT(*) cars
    FROM
        car_table
    '''
