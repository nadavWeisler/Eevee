import moodle_api
import KeyGenerator


class MoodleConnector:
    def __init__(self, username, password):
        self._username, self._pass = username, password
        # with open("credentials", "r") as cred:
        #     self._username, self._pass = cred.readline().split(',')

    def get_course_contents_wrapper(self, course_id):
        token = KeyGenerator.get_token_from_credentials(username=self._username, password=self._pass)
        moodle_api.KEY = token
        return moodle_api.call('core_course_get_contents', courseid=course_id)

    def get_all_courses(self):
        token = KeyGenerator.get_token_from_credentials(username=self._username, password=self._pass)
        moodle_api.KEY = token
        return moodle_api.call('core_course_get_recent_courses')
