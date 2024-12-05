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

    for journal_idx, key in enumerate(list(journals_dict.keys())):
        # data from journal part
        journal_name = key
        journal_id = journal_idx+1
        journal_dict = journals_dict[key]
        dates = parse.get_proper_date(journal_dict["months"].split(", "))

        # creating a journal sql
        create_sql.journal_sql(journal_name, journal_dict)

        # data from volume (volume dictionaries for journal)
        volumes = parse.cut_out_volumes(journal_dict)

        for vol in volumes:
            # data from volume issues
            issues = parse.cut_out_issues(vol[0])
            year = vol[0]["year"].strip()

            for issue_idx, issue in enumerate(issues):

                temp_dates = []
                if len(dates) < len(issues) and (len(issues) == 1 or len(issues) % 2 == 0):
                    temp_dates = parse.date_fix(len(issues))

                # creating issue sql
                if len(dates) == len(issues):
                    date = dates[issue_idx] + year
                elif len(dates) > len(issues):
                    if year != "2024":
                        date = dates[issue_idx+(len(dates)-len(issues))] + year
                    else:
                        while len(dates)>len(issues):
                            dates.pop(len(dates)-1)
                        date = dates[issue_idx] + year
                elif len(issues) % 2 != 0 and len(issues) != 1:
                    date = input(f"Please enter the date for {journal_name}, {vol[1]}, {issue[1]} [dd-mm-yyyy]:")
                else:
                    date = temp_dates[issue_idx] + year


                issue_id = create_sql.issue_sql(issue, vol, date, journal_id)

                # data from issue articles
                articles = parse.cut_out_articles(issue[0])

                for article in articles: # article = [article_dict, issue_name, title], ...]
                    # getting author data per article and adding it to the sql
                    authors = parse.cut_out_authors(article)

                    article_id = create_sql.article_sql(article, issue_id)

                    create_sql.author_sql(authors, article_id)

        print(f"Finished working on {journal_name}")

if __name__ == '__main__':
    program()
