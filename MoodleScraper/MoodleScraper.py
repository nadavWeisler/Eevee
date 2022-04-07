import moodle_api
import KeyGenerator

class MoodleConnector:
    def __init__(self):
        with open("credentials", "r") as cred:
            self._username, self._pass = cred.readline().split(',')

    def get_course_contents_wrapper(self, courseid):
        token = KeyGenerator.get_token_from_credentials(username=self._username, password=self._pass)
        moodle_api.KEY = token
        return moodle_api.call('core_course_get_contents', courseid=courseid)

    def get_all_courses(self):
        token = KeyGenerator.get_token_from_credentials(username=self._username, password=self._pass)
        moodle_api.KEY = token
        return moodle_api.call('core_course_get_recent_courses')

if __name__ == '__main__':
    moodleConnector = MoodleConnector()
    courses_list = moodleConnector.get_all_courses()
    print("f")
    # course1 = moodleConnector.get_course_contents_wrapper(52307)
    # course2 = moodleConnector.get_course_contents_wrapper(52311)
    # course3 = moodleConnector.get_course_contents_wrapper(67506)
    # course1 = moodleConnector.get_course_contents_wrapper(52307)
    # course1 = moodleConnector.get_course_contents_wrapper(52307)
    # course1 = moodleConnector.get_course_contents_wrapper(52307)
    # course1 = moodleConnector.get_course_contents_wrapper(52307)






#
#     course6 = moodle_api.call('core_course_get_contents', courseid=52311)
#     course7 = moodle_api.call('core_course_get_contents', courseid=67506)
#     course = moodle_api.call('core_course_get_contents', courseid=52307)
#     print(token)
# # courses = moodle_api.CourseList()
# print(courses)


# course5