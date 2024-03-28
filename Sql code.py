pip install pyodbc
import pyodbc
def connect_to_sql_server():
    try:
        conn = pyodbc.connect(
            &#39;DRIVER={SQL Server};&#39;
            &#39;SERVER=mcruebs04.isad.isadroot.ex.ac.uk;&#39;
            &#39;DATABASE=BEMM459_GroupO;&#39;
            &#39;UID=GroupO;&#39;
            &#39;PWD=FozD417+Dx;&#39;
            &#39;Encrypt=yes;&#39;
        )
        return conn
except pyodbc.Error as e:
        print(&quot;Error connecting to SQL Server:&quot;, e)
        return None
def select_with_inner_join():
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            query = &#39;&#39;&#39;
                SELECT yield.area, crop.crop_name
                FROM yield
                INNER JOIN crop ON yield.crop_id = crop.crop_id
            &#39;&#39;&#39;
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print(&quot;Error executing SELECT query with INNER JOIN:&quot;, e)
        finally:
            conn.close()
# Function to execute a SELECT query with LEFT OUTER JOIN
def select_with_left_outer_join():
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            query = &#39;&#39;&#39;
                SELECT yield.area, crop.crop_name
                FROM yield
                LEFT OUTER JOIN crop ON yield.crop_id = crop.crop_id
            &#39;&#39;&#39;
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print(&quot;Error executing SELECT query with LEFT OUTER JOIN:&quot;, e)
        finally:
            conn.close()
def insert_order(customer_id, order_date):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            query = &#39;&#39;&#39;
                INSERT INTO yield (past_year, area)
                VALUES (2009, India)
            &#39;&#39;&#39;
            cursor.execute(query, (customer_id, order_date))
conn.commit()
            print(&quot;Order inserted successfully.&quot;)
        except pyodbc.Error as e:
            print(&quot;Error inserting order:&quot;, e)
        finally:
            conn.close()
def update_order(order_id, new_order_date):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            query = &#39;&#39;&#39;
                UPDATE yield
                SET past_year = 2004
                WHERE yield_id = 10
            &#39;&#39;&#39;
            cursor.execute(query, (new_order_date, order_id))
            conn.commit()
            print(&quot;Order updated successfully.&quot;)
        except pyodbc.Error as e:
            print(&quot;Error updating order:&quot;, e)
        finally:
            conn.close()
def delete_order(order_id):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            query = &#39;&#39;&#39;
                DELETE FROM yield
                WHERE yield_id = 7
            &#39;&#39;&#39;
            cursor.execute(query, (order_id,))
            conn.commit()
            print(&quot;Order deleted successfully.&quot;)
        except pyodbc.Error as e:
            print(&quot;Error deleting order:&quot;, e)
        finally:
            conn.close()
if __name__ == &quot;__main__&quot;:
    # Example of executing a SELECT query with INNER JOIN
    print(&quot;Results of SELECT query with INNER JOIN:&quot;)
    select_with_inner_join()
    # Example of executing a SELECT query with LEFT OUTER JOIN
    print(&quot;\nResults of SELECT query with LEFT OUTER JOIN:&quot;)
    select_with_left_outer_join()
    # Example of inserting an order
insert_order(1, &#39;2024-03-26&#39;)
    # Example of updating an order
    update_order(1, &#39;2024-03-27&#39;)
    # Example of deleting an order
    delete_order(1)
