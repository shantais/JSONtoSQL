import rw_file


def journal_sql(journal_name, journal_dict):

    sql_journal_line = (f"INSERT INTO JOURNAL(JOURNAL_NAME, ABBREVIATION, FREQUENCY, MONTHS, ISSN, DOI, COVER_PATH) "
                f"VALUES (\'{journal_name}\', \'{journal_dict["abbr"]}\', \'{journal_dict["freq"]}\', \'{journal_dict["months"]}\', "
                f"\'{journal_dict["issn"]}\', \'{journal_dict["doi"]}\', \'-\');")

    file_name = "journals.txt"
    rw_file.add(sql_journal_line, file_name)


def author_sql(authors):
    for idx, auth in enumerate(authors):
        for key in list(auth.keys()):
            sql_author_line = (f"INSERT INTO AUTHOR(AUTHOR_NAME, E-MAIL, INSTITUTION, ORCID) "
                               f"VALUES (\'{key}\', \'{auth[key]["e-mail"]}\', \'{auth[key]["institution"]}\', \'{auth[key]["orcid"]}\')")

            file_name = "authors.txt"
            author_id, line_number = rw_file.read(file_name, sql_author_line)

            if author_id == 0:
                rw_file.add(sql_author_line, file_name)
                authors[idx] = [auth, line_number]
            else:
                authors[idx] = [auth, author_id]
