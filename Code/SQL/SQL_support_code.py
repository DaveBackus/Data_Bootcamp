# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
import sqlite3
import xlrd as xl

# if this .sqlite db doesn't already exists, this will create it
# if the .sqlite db *does* already exist, this establishes the desired connection
con = sqlite3.connect("sql_sample_db.sqlite")

# create pandas dataframes from each .csv file:
sales_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/sales_table.csv')
car_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/car_table.csv')
salesman_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/salesman_table.csv')
cust_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/cust_table.csv')
dog_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/dog_table.csv')
cat_table = pd.read_csv('https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/Code/SQL/cat_table.csv')

#%%
# make a list of the tables (dataframes) and table names:
tables = [sales_table, car_table, salesman_table, cust_table, dog_table, cat_table]
table_names = ['sales_table', 'car_table', 'salesman_table', 'cust_table', 'dog_table', 'cat_table']

# drop each table name if it already exists to avoid error if you rerun this bit of code
# then add it back (or add it for the first time, if the table didn't already exist)
for i in range(len(tables)):
    table_name = table_names[i]
    table = tables[i]
    con.execute("DROP TABLE IF EXISTS {}".format(table_name))
    pd.io.sql.to_sql(table, "{}".format(table_name), con, index=False)
    
# Function to make it easy to run queries on this mini-database
def run(query):
    results = pd.read_sql("{}".format(query), con).fillna(' ')
    return results

# create some dataframes to act as keys to clarify differences between difference rdbms
rdbms_differences = pd.DataFrame()

# show describe options
describe_index = ['Reading a table']
describe_differences = pd.DataFrame({'SQLite' : pd.Series(['PRAGMA TABLE_INFO(table_name)'], index=describe_index), 
							'MySQL' : pd.Series(['DESCRIBE table_name'], index=describe_index),
							'Microsoft SQL Server' : pd.Series(['SP_HELP table_name'], index=describe_index),
							'Oracle' : pd.Series(['DESCRIBE table_table'], index=describe_index)})
rdbms_differences = rdbms_differences.append(describe_differences)

# show limit options
limit_df_index = ['LIMITING']
limit_differences = pd.DataFrame({'SQLite' : pd.Series(['LIMIT N'], index=limit_df_index),
                        'MySQL' : pd.Series(['LIMIT N'], index=limit_df_index),
                        'Microsoft SQL Server' : pd.Series(['SELECT TOP N column_a...'], index=limit_df_index),
                        'Oracle' : pd.Series(['WHERE ROWNUM <=N'], index=limit_df_index)})
rdbms_differences = rdbms_differences.append(limit_differences)  

# show compatibility with joins and different DBs 
join_df_index = ['JOIN or INNER JOIN', 'LEFT JOIN or LEFT OUTER JOIN', 'RIGHT JOIN or RIGHT OUTER JOIN', 'OUTER JOIN or FULL OUTER JOIN']
join_differences = pd.DataFrame({'SQLite' : pd.Series(['✓', '✓', 'not supported', 'not supported'], index=join_df_index),
                        'MySQL' : pd.Series(['✓', '✓', '✓', 'not supported'], index=join_df_index),
                        'Microsoft SQL Server' : pd.Series(['✓','✓','✓','✓'], index=join_df_index),
                        'Oracle' : pd.Series(['✓','✓','✓','✓'], index=join_df_index)})
rdbms_differences = rdbms_differences.append(join_differences)                     

# show concat options: 
concat_df_index = ['Concatenating']
concat_differences = pd.DataFrame({'SQLite' : pd.Series(['||'], index=concat_df_index),
                        'MySQL' : pd.Series(['CONCAT(column_a, column_b)'], index=concat_df_index),
                        'Microsoft SQL Server' : pd.Series(['CONCAT(column_a, column_b) or +'], index=concat_df_index),
                        'Oracle' : pd.Series(['CONCAT(column_a, column_b) or ||'], index=concat_df_index)})
rdbms_differences = rdbms_differences.append(concat_differences)   


# show options for IF and CASE WHEN statements                        
conditional_df_index = ['IF', 'CASE WHEN']
conditional_differences = pd.DataFrame({'SQLite' : pd.Series(['not supported', '✓'], index=conditional_df_index),
                        'MySQL' : pd.Series(['IF(condition, value_if_true, value_if_false)', '✓'], index=conditional_df_index),
                        'Microsoft SQL Server' : pd.Series(['IF condition PRINT value_if_true...','✓'], index=conditional_df_index),
                        'Oracle' : pd.Series(['IF condition THEN value_if_true ELSIF...END IF','✓'], index=conditional_df_index)})
rdbms_differences = rdbms_differences.append(conditional_differences)                                            


rollup_df_index = ['ROLLUP']
rollup_differences = pd.DataFrame({'SQLite' : pd.Series(['not supported'], index=rollup_df_index),
                        'MySQL' : pd.Series(['GROUP BY column_a WITH ROLLUP'], index=rollup_df_index),
                        'Microsoft SQL Server' : pd.Series(['GROUP BY column_a WITH ROLLUP'], index=rollup_df_index),
                        'Oracle' : pd.Series(['GROUP BY ROLLUP (column_a)'], index=rollup_df_index)})
rdbms_differences = rdbms_differences.append(rollup_differences)                                            


# Below are all the cheats to the challenges

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

operator_cheat = '''
    SELECT
        S.id,
        C.model, 
        S.revenue,
        C.cogs,
        (S.revenue - C.cogs)/(C.cogs) AS gross_profit
    FROM
        sales_table S 
        JOIN car_table C on S.model_id = C.model_id
    LIMIT 5 
	'''
	
concat_cheat = '''
	SELECT
        model|| ' (' || make || ')' AS 'Model (Make)'
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
    
    --bonus points (run separately)--
    
        SELECT 
       COUNT(*) Subarus
    FROM
        car_table
    WHERE
        make = 'Subaru'
    '''

avg_cheat2 = '''
    SELECT
        AVG(C.sticker_price - S.revenue) AS Avg_Difference
    FROM
        sales_table S 
        JOIN car_table C on C.model_id = S.model_id
        JOIN cust_table CUST on CUST.customer_id = S.customer_id
    WHERE
        CUST.age > 35
    '''

concat_cheat = '''
    SELECT
        GROUP_CONCAT(last_name, ', ') AS Last_Names
    FROM
        salesman_table
    '''

group_cheat = '''
    SELECT 
        C.make,
        AVG(S.revenue - C.cogs)
    FROM
        sales_table S
        JOIN car_table C on S.model_id = C.model_id
    GROUP BY
        C.make
    
    --bonus points--
    
    SELECT 
        C.make as Car_Maker,
        ROUND(AVG(S.revenue - C.cogs), 2) AS Avg_Gross_Profit
    FROM
        sales_table S
        JOIN car_table C on S.model_id = C.model_id
        JOIN salesman_table SM on S.salesman_id = SM.id
    WHERE
        SM.first_name = 'Michael'
    GROUP BY
        Car_Maker
    ORDER BY
        Avg_Gross_Profit DESC
        
    --solutions to WHERE problem--
    
    SELECT
    	SM.first_name as Salesman,
        C.make as Car_Maker,
        ROUND(AVG(S.revenue - C.cogs), 2) AS Avg_Gross_Profit
    FROM
        sales_table S
        JOIN car_table C on S.model_id = C.model_id
        JOIN salesman_table SM on S.salesman_id = SM.id
    WHERE
        SM.first_name = 'Michael'
    GROUP BY
        Car_Maker
    ORDER BY
        Avg_Gross_Profit DESC
    '''

group_cheat1 = '''    
	SELECT 
        make as Maker,
        GROUP_CONCAT(model) as Car_Models
    FROM
        car_table
    GROUP BY
        Maker
        '''

group_cheat2 = '''
	SELECT
		SM.first_name || ' ' || SM.last_name AS Salesperson,
        CUST.gender AS Gender, 
        SUM(S.revenue) AS Total_Revenue,
        COUNT(S.id) AS Cars_Sold
    FROM
        sales_table S
        JOIN salesman_table SM ON S.salesman_id = SM.id
        JOIN cust_table CUST ON S.customer_id = CUST.customer_id
    GROUP BY
        Salesperson,
        Gender
    '''

having_cheat = '''
	SELECT
        C.model as Car_Model,
        AVG(S.revenue) as Avg_Revenue
    FROM
        sales_table S
        JOIN car_table C on S.model_id = C.model_id
    GROUP BY
        Car_Model HAVING Avg_Revenue < 18000
    '''

having_where_cheat = '''
	SELECT
        SM.last_name as Salesperson,
        ROUND(AVG(S.revenue), 2) as Avg_Revenue
    FROM
        sales_table S
        JOIN salesman_table SM ON S.salesman_id = SM.id
        JOIN cust_table CUST ON S.customer_id = CUST.customer_id
    WHERE
        CUST.gender = 'female'
    GROUP BY
        Salesperson HAVING Avg_Revenue > 20000
    '''
    
case_cheat = '''
    SELECT 
        C.model as Car_Model,
        SUM(CASE WHEN CUST.gender = 'female' THEN S.revenue END) Female_Customer_Revenue,
        SUM(CASE WHEN CUST.gender = 'male' THEN S.revenue END) Male_Customer_Revenue
    FROM
        sales_table S
            JOIN car_table C ON S.model_id = C.model_id
            JOIN cust_table CUST ON CUST.customer_id = S.customer_id
    GROUP BY
        Car_Model
    '''

case_cheat2 = '''
	SELECT
        CASE WHEN age BETWEEN 18 AND 24 THEN '18-24 years'
             WHEN age BETWEEN 25 AND 34 THEN '25-34 years'
             WHEN age BETWEEN 35 AND 44 THEN '35-45 years'
             WHEN age BETWEEN 45 AND 54 THEN '45-54 years'
             WHEN age BETWEEN 55 AND 64 THEN '55-64 years'
             END Age_Group,
        SUM(CASE WHEN gender = 'female' THEN 1 END) Female_Customers,
        SUM(CASE WHEN gender = 'male' THEN 1 END) Male_Customers
    FROM
        cust_table
    GROUP BY
        Age_Group
    
    --bonus points--
    
    SELECT
        CASE WHEN age BETWEEN 18 AND 24 THEN '18-24 years'
             WHEN age BETWEEN 25 AND 34 THEN '25-34 years'
             WHEN age BETWEEN 35 AND 44 THEN '35-45 years'
             WHEN age BETWEEN 45 AND 54 THEN '45-54 years'
             WHEN age BETWEEN 55 AND 64 THEN '55-64 years'
             END Age_Group,
        ROUND(SUM(CASE WHEN gender = 'female' THEN 1. END)/COUNT(*), 2) Female_Customers,
        ROUND(SUM(CASE WHEN gender = 'male' THEN 1. END)/COUNT(*), 2) Male_Customers
    FROM
        cust_table
    GROUP BY
        Age_Group
    '''
    
nest_cheat1 = '''
	SELECT
        model AS Car_Model,
        cogs AS COGs, 
        (SELECT AVG(cogs) from car_table) AS Average_COGs
    FROM
        car_table
        
    --bonus points--
    
    SELECT
        model AS Car_Model,
        cogs AS COGs, 
        (SELECT AVG(cogs) from car_table) AS Average_COGs,
        cogs - (SELECT AVG(cogs) from car_table) AS Difference
    FROM
        car_table
    '''

nest_cheat2 = '''
	SELECT
        SUM(revenue) as Female_Revenue
    FROM 
        sales_table
    WHERE
        customer_id in (SELECT customer_id FROM cust_table WHERE gender = 'female')
    '''

union_cheat1 = '''
    SELECT
        model, 
        cogs
    FROM 
        car_table
    
    UNION ALL
    
    SELECT
        'Combined_Average',
        ROUND(AVG(cogs), 2)
    FROM
        car_table
    '''