def cut_out_volumes(journal_dict):
    volumes = []
    for key in list(journal_dict.keys()):
        if key == "abbr":
            pass
        elif key == "freq":
            pass
        elif key == "months":
            pass
        elif key == "issn":
            pass
        elif key == "discipline_pl":
            pass
        elif key == "discipline_en":
            pass
        elif key == "doi":
            pass
        else:
            volumes.append([journal_dict[key], key])
    return volumes


def cut_out_issues(volume):
    issues = []
    for key in list(volume.keys()):
        if key == "year":
            pass
        else:
            issues.append([volume[key], key])
    return issues


def cut_out_articles(issue):
    articles = []
    for key in list(issue.keys()):
        if key == "doi":
            pass
        else:
            articles.append(issue[key])
    return articles


def cut_out_authors(article):
    authors = []
    for key in list(article.keys()):
        if key == "titles":
            pass
        elif key == "abstracts":
            pass
        elif key == "keywords":
            pass
        elif key == "references":
            pass
        elif key == "doi":
            pass
        elif key == "pages":
            pass
        else:
            # authors.append([art[0][key], art[1], art[2]])
            authors.append(article[key])
    return authors

def get_proper_date(months):
    date = []
    for month in months:
        if month == "II":
            date.append("28-02-")
        elif month == "III":
            date.append("31-03-")
        elif month == "IV":
            date.append("30-04-")
        elif month == "VI":
            date.append("30-06-")
        elif month == "VIII":
            date.append("31-08-")
        elif month == "IX":
            date.append("30-09-")
        elif month == "X":
            date.append("31-10-")
        elif month == "XII":
            date.append("31-12-")
    return date


def date_fix(amount_of_months):
    if amount_of_months == 1:
        month = "XII"
    elif amount_of_months == 2:
        month = "VI, XII"
    elif amount_of_months == 4:
        month = "III, VI, IX, XII"
    else:
        month = "II, IV, VI, VIII, X, XII"

    return get_proper_date(month.split(", "))