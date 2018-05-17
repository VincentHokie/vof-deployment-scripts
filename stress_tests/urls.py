import random
import string


'''
    This file contains routes that are not prefixed
    with /program or /learner in the VOF routes.

    You will notice a lot of "random.choice([1, 4])"
    This is to ensure if a program_id is needed in the url
    it is as dynamic as possible. This can being up unforseen
    bugs when different combinations of parameters are used.
'''


def index(l):
    l.client.get("/login")


def get_sheet(l):
    l.client.get("/sheet")


# this route requires a file upload/download, there's
# a similar issue faced on the learners file
# please fix and hit endpoint
def get_holistic_csv(l):
    l.client.post(
        "/notifications",
        headers={'content-type': 'application/json'},
        data='{"content": "You have been assigned a new Learner: \
        <a class=\'notification-link\' href=\'/learners/-LBUxNv2rO7RKaMdK8Pd\
        /1298/scores\'>Uhuru Kenyatta</a>", "recipient_emails": \
        "edward.karanja@example.com", "priority": "Normal"}')
    # l.client.get("/holistic-csv/" + str(random.randint(1, 1241)))


def get_assessments_metrics(l):
    l.client.get(
        "/metrics/" + str(random.choice([9, 8, 35, 23, 39, 4, 12, 11, 15, 2])))


def post_notifications(l):
    l.client.post(
        "/notifications",
        headers={'content-type': 'application/json'},
        data='{"content": "You have been assigned a new Learner: \
        <a class=\'notification-link\' href=\'/learners/-LBUxNv2rO7RKaMdK8Pd\
        /1298/scores\'>Uhuru Kenyatta</a>", "recipient_emails": \
        "edward.karanja@example.com", "priority": "Normal"}')


# this delete notification route uses a notification id/ids
# retrieving this id/ids is the key to having this route tested
def delete_notifications(l):
    l.client.post(
        "/notifications",
        headers={'content-type': 'application/json'},
        data='{"content": "You have been assigned a new Learner: \
        <a class=\'notification-link\' href=\'/learners/-LBUxNv2rO7RKaMdK8Pd\
        /1298/scores\'>Uhuru Kenyatta</a>", "recipient_emails": \
        "edward.karanja@example.com", "priority": "Normal"}')
    # l.client.delete(
    #     "/notifications",
    #     headers={'content-type': 'application/json'},
    #     data='')


def get_learners_one(l):
    l.client.get("/learners?program_id=1")


def get_learners_four(l):
    l.client.get("/learners?program_id=4")


def get_dashboard(l):
    l.client.get('/dashboard')


def get_support(l):
    l.client.get("/support")


def get_curriculum(l):
    l.client.get("/curriculum")


def get_criteria(l):
    l.client.post(
        "/criteria",
        headers={'content-type': 'application/json; charset=utf-8'},
        data='{"criterium": {"name": "' + ''.join(random.choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(5)) + '", "description": "Just be awesome yo "}\
        , "frameworks": ["1"]}')


def get_learner(l):
    # l.client.get("/learner")
    l.client.get("/curriculum")


def get_feedback(l):
    # l.client.get("/feedback")
    l.client.get("/curriculum")


def get_programs(l):
    l.client.post(
        "/programs",
        headers={'content-type': 'application/json'},
        data='{"program": {"name": "' + ''.join(
            random.choice(string.ascii_uppercase + string.digits)
             for _ in range(5)) + '", "description": "vince awesomeness scale",\
         "phases": ["head down", "work hard", "work smart", "help", \
         "be helped", "grow", "learn"], "holistic_evaluation": "false",\
          "cadence_id": ""}}')


def get_cadences(l):
    l.client.get("/cadences")


def get_admins(l):
    l.client.get("/admins")


def get_phase_assessment(l):
    l.client.get("/phases/" + str(random.randint(23, 29)) + "/assessment")


def get_desicion_reason(l):
    # l.client.get("/decision/reason/:status")
    l.client.get('/dashboard')


def add_decision(l):
    program_id = random.randint(1, 1241)
    l.client.post(
        "/decision/add",
        headers={'content-type': 'application/json'},
        data='{"decisions": {"stage": "2", "learner_program_id": "' + 
        str(program_id) + '", "reasons": ["Output Quality - Technical Skills"]\
        , "comment": "dghdf"}}')


def get_feedback_details(l):
    # l.client.get("/feedback/feedback_details")
    l.client.get('/dashboard')


def get_learner_feedback(l):
    # l.client.get("/feedback/get-learner-feedback")
    l.client.get('/dashboard')


def save_feedback(l):
    l.client.post(
        "/feedback/save",
        headers={'content-type': 'application/json'},
        data='{"details": {"learner_program_id": "1141", "phase_id": "23",\
         "assessment_id": "1", "impression_id": "2", "comment": "adasda"}}')


def get_phase_assessments(l):
    l.client.get("/phases/" + str(random.randint(23, 29)) + "/assessments")


def update_phase_assessments(l):
    l.client.post(
        "/feedback/save",
        headers={'content-type': 'application/json'},
        data='{"details": {"learner_program_id": "1141", "phase_id": "23",\
         "assessment_id": "1", "impression_id": "2", "comment": "adasda"}}')
    # l.client.put(
    #     "/programs/" + str(random.choice([1, 4])) + "/phases/"
    #     + str(random.randint(23, 29)) + "/assessments",
    #     headers={'content-type': 'application/json'},
    #     data='')


def get_curriculum_details(l):
    l.client.get("/curriculum/details")


def get_output_details(l):
    l.client.get("/output/details")


def get_framework_criteria(l):
    l.client.get("/framework/" + str(random.choice([1, 2, 3])) + "/criteria")


def get_framework_description(l):
    framework = random.choice([1, 2, 3])
    l.client.put(
        "/framework/" + str(framework) + "/description",
        headers={'content-type': 'application/json'},
        data='{"framework": {"description": "Values Alignment descriptions"},\
         "id": "' + str(framework) + '"}')


def get_framework_criterias(l):
    l.client.get(
        "/framework-criteria/1/" + str(random.randint(8, 10)))
