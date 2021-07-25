""" fixtures that return an sql statement with a list of values to be inserted."""

def load_verb():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Verb 
          (
              `tense`, `word_id`, `yo`, `tu`, 
              `usted`, `nosotros`, `vosotros`, `ustedes`
          ) 
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    values = [
        (
            'simple present', 1, 'voy', 'vas', 'va', 'vamos', 'vais', 'van'
        ),
    ]

    return {
        'sql': sql, 
        'values': values
    }
