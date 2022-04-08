# from MoodleScraper import Tasks
from trello import TrelloClient
# from MoodleScraper import lambda_function
from datetime import datetime

class TrelloConnector:
    def _get_or_create_board(self):
        all_boards = self.client.list_boards()
        eevee_board = None
        self.type_to_color = {'assign': 'red', 'quiz': 'blue'}

        for board in all_boards:
            if board.name == "Eevee":
                eevee_board = board
                break

        if eevee_board:
            return eevee_board

        return self.client.add_board("Eevee")


    def __init__(self, trello_api_key, trello_api_secret, trello_token):
        self.client = TrelloClient(api_key=trello_api_key, api_secret=trello_api_secret, token=trello_token)
        self.eevee_board = self._get_or_create_board()


    def get_board(self):
        return self.eevee_board






    def get_or_create_course_list(self, course_id):
        """
        creates a list  with the given course id if its not already configured.
        :param course_id:
        :return: the list of
        """

        current_lists = self.eevee_board.all_lists()
        lists_names = [ls.name for ls in current_lists]
        if course_id not in lists_names:
            return self.eevee_board.add_list(str(course_id))
        return current_lists[lists_names.index(course_id)]


    def is_task_in_board(self, task_name):
        """

        :param task_name:
        :return: true if taskname is in the board
        """
        return task_name in {card.name for card in self.eevee_board.all_cards()}


    def post_courses_tasks(self, payload):
        """
        :param payload: Dictionary of {#course_num : [list of Tasks]}
        :return:
        """
        updated = False
        for course_num in payload:
            trello_course_list = self.get_or_create_course_list(course_num)
            course_tasks_list = payload[course_num]
            for task in course_tasks_list:
                task_name = task.name
                if not self.is_task_in_board(task_name):
                    updated = True
                    due_date = datetime.fromtimestamp(task.due_date).strftime("%d %b, %Y") if task.due_date else 'null'
                    # label = [self.type_to_color[task.type] if task.type else None]
                    desc = task.url if task.url else None
                    trello_course_list.add_card(name=task_name, due=due_date, desc=desc)
        return updated

# if __name__ == '__main__':
    # test_dict = lambda_function.zibi()
    # short_dict = {list(test_dict.keys())[0] : test_dict[list(test_dict.keys()[0])]}
    #
    # print(test_dict)
    # connector = TrelloConnector("c32bd037befedb2ba4d1563d0c98c9fa","40f8b539dc29ebd8c02b1712238a23a6e5c5066b09bea95976a384e3a435cfb6","b4a7f2483e82c020f262abcaf4e710c4ddf147ea66377bec28f8bf6011dbdcf6")
    # connector.post_courses_tasks(test_dict)
    # g = connector.get_or_create_course_list(123)
    # g2 = connector.get_or_create_course_list(123)
    # g2.add_card("ex21")
    # print(connector.is_task_in_board("ex21"))
    # print(connector.is_task_in_board("ex22"))
    # print(g2.name)
    # print(connector.get_board().name)
