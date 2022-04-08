from Tasks import Task
import re
import time

TASK = 'assign|quiz'
DUE_DATE = 'Due|Closed'


class Parser:

    @staticmethod
    def parse_tasks(course_data, cid):
        tasks = []
        current_time = time.time()
        for data_dict in course_data:
            for module in data_dict['modules']:
                if re.match(TASK, module['modname']):
                    task = Parser.extract_task(cid, module, module['modname'])
                    if task.due_date > current_time:
                        tasks.append(task)
        return tasks

    @staticmethod
    def extract_task(cid, module, task_type):
        due_date = None
        name = "{0}_{1}".format(cid, module['name'])
        url = module['url']
        for date in module['dates']:
            if re.match(DUE_DATE, date['label']):
                due_date = date['timestamp']
                break
        return Task(name, due_date, url, cid, task_type)




