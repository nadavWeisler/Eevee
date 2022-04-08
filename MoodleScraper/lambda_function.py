from Parser import Parser
from MoodleScraper import MoodleConnector


def zibi():
    username, password = "zohar.s", "zs1qaz" ##todo
    moodleConnector = MoodleConnector(username, password)
    courses_list = moodleConnector.get_all_courses()
    courses_ids = [course['id'] for course in courses_list]
    courses_dict = {} #todo output
    for course_id in courses_ids:
        try:
            course_data = moodleConnector.get_course_contents_wrapper(course_id)
            courses_dict[course_id] = Parser.parse_tasks(course_data, course_id)
        except:
            continue
    return courses_dict


zibi()