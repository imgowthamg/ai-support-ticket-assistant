from app.database.db import get_connection


def get_solution_by_category(category: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT solution, team
        FROM support_solutions
        WHERE LOWER(category) = LOWER(?)
        LIMIT 1
        """,
        (category,)
    )

    result = cursor.fetchone()

    conn.close()

    return result