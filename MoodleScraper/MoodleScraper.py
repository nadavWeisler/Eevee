import moodle_api

# courses = moodle_api.CourseList()
course5 = moodle_api.call('core_course_get_contents', courseid=52307)
course5