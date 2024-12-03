import create_sql
import identifier
import parse
import prompts
import rw_file


def program():
    identifier.header()

    # load the dictionary
    journals_dict = rw_file.load_journals()

    # check if file was there to begin with and if not exit (nothing to work on)
    prompts.check_if_file_exists(journals_dict)

    for idx, key in enumerate(list(journals_dict.keys())):
        journal_name = key
        journal_dict = journals_dict[key]
        volumes = parse.cut_out_volumes(journal_dict)
        issues = parse.cut_out_issues(volumes)
        articles = parse.cut_out_articles(issues)
        authors = parse.cut_out_authors(articles)

        create_sql.journal_sql(journal_name, journal_dict)
        create_sql.author_sql(authors)
        # create_sql.issue_sql(idx, issues)


if __name__ == '__main__':
    program()
