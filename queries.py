import database_common


@database_common.connection_handler
def mentors_with_schools(cursor):
    cursor.execute('''SELECT mentors.first_name, mentors.last_name, schools.name, schools.country 
                      FROM schools
                      JOIN mentors
                      ON schools.contact_person = mentors.id
                      ORDER BY mentors.id''')
    query_result = cursor.fetchall()
    print(query_result)
    return query_result


@database_common.connection_handler
def mentors_with_allschool(cursor):
    cursor.execute('''SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                      FROM schools
                      LEFT JOIN mentors
                      ON schools.contact_person = mentors.id
                      ORDER BY mentors.id''')
    query_result = cursor.fetchall()
    return query_result


@database_common.connection_handler
def count_mentors_by_schools(cursor):
    cursor.execute('''SELECT country, COUNT (contact_person) 
                      FROM schools 
                      GROUP BY country''')
    query_result = cursor.fetchall()
    return query_result

