import database_common


@database_common.connection_handler
def get_questions_for_index(cursor):
    cursor.execute("SELECT id, submission_time, view_number, vote_number, title FROM question")
    questions = cursor.fetchall()
    return questions
