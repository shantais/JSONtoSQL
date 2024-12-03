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
            volumes.append(journal_dict[key])
    return volumes


def cut_out_issues(volumes):
    issues = []
    for vol in volumes:
        for key in list(vol.keys()):
            if key == "year":
                pass
            else:
                issues.append([vol[key], key])
    return issues


def cut_out_articles(issues):
    articles = []
    for iss in issues:
        for key in list(iss[0].keys()):
            if key == "doi":
                pass
            else:
                articles.append([iss[0][key], iss[1], key])
    return articles


def cut_out_authors(articles):
    authors = []
    for art in articles:
        for key in list(art[0].keys()):
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
                authors.append(art[0][key])
    return authors