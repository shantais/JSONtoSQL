import rw_file


def journal_sql(journal_name, journal_dict):

    sql_journal_line = (f"INSERT INTO JOURNAL(JOURNAL_NAME, ABBREVIATION, FREQUENCY, MONTHS, ISSN, DOI, COVER_PATH) "
                f"VALUES (\'{journal_name}\', \'{journal_dict["abbr"]}\', \'{journal_dict["freq"]}\', \'{journal_dict["months"]}\', "
                f"\'{journal_dict["issn"]}\', \'{journal_dict["doi"]}\', \'-\');")

    file_name = "journals.txt"
    rw_file.add(sql_journal_line, file_name)


def issue_sql(issue, vol, date, journal_id):
    sql_issue_line = (f"INSERT INTO ISSUE(VOLUME_NAME, ISSUE_NAME, ISSUE_DOI, ISSUE_DATE, JOURNAL_ID) "
                      f"VALUES (\'{vol[1]}\', \'{issue[1]}\', \'{issue[0]["doi"]}\', \'{date}\', \'{journal_id}\')")
    file_name = "issues.txt"
    rw_file.add(sql_issue_line, file_name)

    return rw_file.find_line(file_name, sql_issue_line)

def article_sql(article, issue_id):
    titles = ""
    for title in article["titles"]:
        if title not in titles:
            titles += "</-/>xx</-/>" + title

    abstracts = ""
    for abstract in article["abstracts"]:
        abstracts += "</-/>xx</-/>" + abstract

    keywords = ""
    for keyword in article["keywords"]:
        keywords += "</-/>xx</-/>" + keyword

    references = ""
    for ref in article["references"]:
        references += "</-/>" + ref
    references = references.replace("</-/>", "", 1)

    pages = article["pages"][0] + "-" + article["pages"][1]

    sql_article_line = (f"INSERT INTO ARTICLE(TITLES, ABSTRACTS, KEYWORDS, REFERENCES, PAGES, ARTICLE_DOI, ISSUE_ID) "
                        f"VALUES (\'{titles}\', \'{abstracts}\', \'{keywords}\', "
                        f"\'{references}\', \'{pages}\', \'{article["doi"]}\', \'{issue_id}\')")
    file_name = "articles.txt"
    rw_file.add(sql_article_line, file_name)

    return rw_file.find_line(file_name, sql_article_line)


def author_sql(authors, article_id):
    for author in authors:
        for key in list(author.keys()):
            sql_author_line = (f"INSERT INTO AUTHOR(AUTHOR_NAME, E-MAIL, INSTITUTION, ORCID, ARTICLE_ID) "
                               f"VALUES (\'{author[key]}\', \'{author[key]["e-mail"]}\', \'{author[key]["institution"]}\', "
                               f"\'{author[key]["orcid"]}\', \'{article_id}\')")

            file_name = "authors.txt"
            rw_file.add(sql_author_line, file_name)