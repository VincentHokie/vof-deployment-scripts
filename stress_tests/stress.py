from locust import HttpLocust, TaskSet
import learners_urls, program_urls, urls
import urllib3
urllib3.disable_warnings()

'''
    This script is used to continuously hit
    all VOF endpoints where users are hitting
    endpoints between 1 and 2 seconds.

    Endpoints have been divided between different
    files to improve maintainability.
'''


class UserBehavior(TaskSet):

    def on_start(self):
        self.client.verify = False

    tasks = {
        urls.index: 1,
        urls.get_sheet: 2,
        urls.get_holistic_csv: 3,
        urls.get_assessments_metrics: 4,
        urls.post_notifications: 5,
        urls.delete_notifications: 6,
        urls.get_learners_one: 7,
        urls.get_learners_four: 8,
        urls.get_dashboard: 9,
        urls.get_support: 10,
        urls.get_curriculum: 11,
        urls.get_criteria: 12,
        urls.get_learner: 13,
        urls.get_feedback: 14,
        urls.get_programs: 15,
        urls.get_cadences: 16,
        urls.get_admins: 17,
        urls.get_phase_assessment: 18,
        urls.get_desicion_reason: 19,
        urls.add_decision: 20,
        urls.get_feedback_details: 21,
        urls.get_learner_feedback: 22,
        urls.save_feedback: 23,
        urls.get_phase_assessments: 24,
        urls.update_phase_assessments: 25,
        urls.get_curriculum_details: 26,
        urls.get_output_details: 27,
        urls.get_framework_criteria: 28,
        urls.get_framework_description: 29,
        urls.get_framework_criterias: 30,
        learners_urls.post_add_holistic_evaluations: 31,
        learners_urls.post_add_colistic_feedback: 32,
        learners_urls.get_holistic_evaluation_eligibility: 33,
        learners_urls.get_holistic_average: 34,
        learners_urls.get_holistic_criteria_average: 35,
        learners_urls.get_decision_history: 36,
        learners_urls.get_scores: 37,
        learners_urls.post_add_scores: 38,
        learners_urls.get_learner_city: 39,
        learners_urls.update_learner: 40,
        learners_urls.get_completed_assessments: 41,
        learners_urls.update_learner_decision_status: 41,
        learners_urls.update_learner_lfa: 43,
        learners_urls.post_add_learners: 44,
        program_urls.get_program_status: 45,
        program_urls.get_program_dlc_stack: 46,
        program_urls.get_program: 47,
        program_urls.get_program_size: 48,
        program_urls.get_program_center_cycles: 49,
        program_urls.get_program_assessments: 50,
    }


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
