import json
import psycopg2

def lambda_handler(event, context):
    # get query string param inputs
    x = event['queryStringParameters']['x']
    y = event['queryStringParameters']['y']

    # Log inputs
    print(f"x:{x}, y:{y}")

    insert_record_agent_target(x, y)

    # Return a success message
    return {
        'statusCode': 200,
        'body': 'Values inserted successfully'
    }
    # prepare the response_body
    # res_body = {}
    # res_body['x'] = int(x)
    # res_body['y'] = int(y)
    # res_body['ans'] = add(x, y)
    #
    # # prepare http response
    # http_res = {}
    # http_res['statusCode'] = 200
    # http_res['headers'] = {}
    # http_res['headers']['Content-Type'] = 'application/json'
    # http_res['body'] = json.dumps(res_body)
    #
    # print(http_res['headers'])
    # print(http_res['body'])

    # return http_res

def insert_record_agent_target(x, y):
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="devpostgres01.cphbkxf9hicq.us-east-1.rds.amazonaws.com",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    # Define insert query (to factorization later)
    postgres_insert_query = """ INSERT INTO public.powerapps_data (value_1, 
                                                                value_2) VALUES (%s,%s)"""

    record_to_insert = (x, y)

    # Commit query
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
# def insert_record_agent_target(x, y):
#     # Replace the connection variables with your own
#     conn = psycopg2.connect(
#         host='redshift-cluster-1.cqbdyi9dryca.us-east-1.redshift.amazonaws.com',
#         port=5439,
#         dbname='dev',
#         user='awsuser',
#         password='Awsuser1234!'
#     )
#
#     cur = conn.cursor()
#
#     # Replace the table and column names with your own
#     table_name = 't2'
#     column_names = ['c1', 'c2']
#
#     # Replace the values with the data you want to insert
#     values = [
#         (x, y)
#     ]
#
#     # Construct the SQL statement
#     sql = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES %s"
#
#     # Use the executemany method to insert multiple rows at once
#     cur.executemany(sql, values)
#
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

# lambda_handler(None, None)