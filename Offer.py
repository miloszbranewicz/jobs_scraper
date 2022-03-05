class Offer:
    def __init__(self, title=None, company=None, working_place=None, requirements=None, salary=None,
                 link_to_offer=None, seniority=None):
        """
        :rtype: object
        :type title: str
        :type company: str
        :type working_place: str
        :type requirements: list
        :type salary: str
        :type link_to_offer: str
        :type seniority: str
        """
        self.title = title
        self.company = company
        self.working_place = working_place
        self.requirements = requirements
        self.salary = salary
        self.link_to_offer = link_to_offer
        self.seniority = seniority
