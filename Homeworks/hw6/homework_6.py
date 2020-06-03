from lxml import etree


class ComposerPageQueryTool:

    def __init__(self, tree):
        self.tree = tree

    def run_query(self, query):
        return self.tree.xpath(query)

    #done
    """Return the number of pages with comments"""
    def count_comments(self):
        return self.run_query('count(page/revision[count(comment) > 0])')

    #done
    """"Return the number of pages for user id 5558"""
    def count_revisions_by_user(self):
        return self.run_query('count(page/revision/contributor[id="5558"])')
    #done
    """Return the timestamp for the 12th page revised by user 5558"""
    def contribution_timestamp(self):
        return self.run_query('(page/revision[contributor/id="5558"]/timestamp/text())[12]')

    #done
    """Return the number of pages with more than 1kb of content"""
    def count_larger_pages(self):
        return self.run_query('count(page/revision/text[@bytes>1000])')

    #done
    """Return the username for the contributor who edited page 150096"""
    def page_reviser(self):
        return self.run_query('page/revision/contributor/username[../../../id="150096"]/text()')
    #done
    """Return the title of the composition that was revised at 2015-02-07T22:58:31Z"""
    def title_timestamp(self):
        return self.run_query('page/title[../revision/timestamp="2015-02-07T22:58:31Z"]/text()')
    #done
    """Return the number of pages where the composition title starts with "Sonata" """
    def count_sonata(self):
        return self.run_query('count(page/title[starts-with(text(), "Sonata")])')

    """Return the tag name for the third sibling of the text element containing the file:
    PMLP137192-ariaperquestabel00moza.pdf"""
    def sibling_tag(self):
        return self.run_query('name(page/revision/text[contains(text(), "PMLP137192-ariaperquestabel00moza.pdf")]/parent::revision/node()[6])')
