from Tasks import Assignment

ASSIGNMENT = 'assign'

class Parser:

    @staticmethod
    def parse_assignments(course_data, cid):
        assignments = {}
        for data_dict in course_data:
            for module in data_dict['modules']:
                if module['modname'] == ASSIGNMENT:
                    assignment = Parser.extract_assignment(cid, module)
                    assignments[assignment.url] = assignment
        return assignments

    @staticmethod
    def extract_assignment(cid, module):
        due_date = None
        name, url = module['name'], module['url']
        for date in module['dates']:
            if 'Due' in date['label'] :
                due_date = date['timestamp']
                break
        return Assignment(name, due_date, url, cid)




