
import pymysql


data =[]
data_stable =[]
schema_name='db'

def get_elligible_clusters_for_patching(dbproduct=None, env="lab", clustername=None , accountid=None):
    connection = pymysql.connect('host',
        'id',
        "pass", 'table')

    select_clause = "SELECT DISTINCT  accountid, clustername, region"

    where_clause = ""
    where_list = []
    if dbproduct is not None:
        where_list.append(" dbproduct = '{}' ".format(dbproduct))

    if clustername is not None:
        where_list.append(" clustername = '{}' ".format(clustername))

    if env is not None:
        where_list.append(" env = '{}' ".format(env))

    if accountid is not None:
        where_list.append(" accountid = '{}' ".format(accountid))

    if len(where_list) != 0:
        where_clause = " where "
        where_clause += " and ".join(where_list)


    sql_table = select_clause + " FROM `{}`.Inventory ".format(schema_name) +where_clause +" ORDER BY accountid DESC"
    sql_stable_view = select_clause + " FROM `{}`.stale_status_nodes ".format(schema_name) +where_clause +" ORDER BY accountid DESC"

    print()
    print("====  Query to fetch Inventory table is  ==== ")
    print("final data", sql_table)
    print("======================================== ")

    print()
    print("====  Query to fetch Inventory table is  ==== ")
    print("final data", sql_stable_view)
    print("======================================== ")
    print()

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_table)
            for row in cursor:
                data.append(row)

            cursor.execute(sql_stable_view)
            for row in cursor:
                data_stable.append(row)

    except Exception as e :
        print("error occurred ", e)
    finally:
        connection.close()


get_elligible_clusters_for_patching(env="lab", dbproduct="elasticsearch")
# get_elligible_clusters_for_patching(clustername='test-elasticsearch-egtiger-singatest')
#print("table data is ", data)
#print("stable data is", data_stable)

final_data = [row for row in data if row not in data_stable]

print()
print("====  List of resources under impact are  ==== ")
for r in final_data:
    print(r)
print("======================================== ")

