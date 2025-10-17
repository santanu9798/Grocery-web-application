
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for row in cursor:
        response.append({
            'uom_id': row['uom_id'],
            'uom_name': row['uom_name']
        })
    return response


if __name__ == '__main__':
    from sql_connection_sqlite import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))