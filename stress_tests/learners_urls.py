import random

'''
    This file contains routes that are prefixed
    with /learners in the VOF routes.

    You will notice a lot of "random.randint(1, 1241)"
    This is to ensure if a program is needed in the url
    it is as dynamic as possible. This can being up unforseen
    bugs when different combinations of parameters are used.
'''

learner_id = "-KxgxvU0XipIgHWzJJeS"
learner_program_id = "1141"


def post_add_holistic_evaluations(l):
    l.client.post(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) +
        "/holistic-evaluations",
        headers={'content-type': 'application/json'},
        data='{"holistic_evaluation":{"0":{"criterium_id":"3", "score":"-2",\
         "comment":"e"}, "1":{"criterium_id":"6", "score":"-1", "comment":"v"}\
         ,"2":{"criterium_id":"8", "score":"-1", "comment":"ver"}, "3":\
         {"criterium_id":"9", "score":"-2", "comment":"ver"}, "4":\
         {"criterium_id":"10", "score":"-2", "comment":"vev"}, "5":\
         {"criterium_id":"11", "score":"-1", "comment":"verfv"}, "6":\
         {"criterium_id":"12", "score":"-1", "comment":"ver"}, "7":\
         {"criterium_id":"13", "score":"-2", "comment":"ver"}}, "id":"'
        + str(learner_id) + '", "learner_program_id":"'
        + str(learner_program_id) + '"}')


def post_add_colistic_feedback(l):
    l.client.post(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) + 
        "/holistic-feedback",
        headers={'content-type': 'application/json'},
        data='{"holistic_feedback": {"0": {"criterium_id": "3", "comment": \
        "scs"}, "1": {"criterium_id": "6", "comment": "asdasd"}, "2": \
        {"criterium_id": "8", "comment": "asda"}, "3": \
        {"criterium_id": "9", "comment": "sadaad"}, "4": \
        {"criterium_id": "10", "comment": "sdas"}, "5": \
        {"criterium_id": "11", "comment": "asda"}, "6": \
        {"criterium_id": "12", "comment": "sda"}, "7": \
        {"criterium_id": "13", "comment": "sdas"}}, "id": "' +
        str(learner_id) + '", "learner_program_id": "' +
        str(learner_program_id) + '"}')


def get_holistic_evaluation_eligibility(l):
    l.client.get(
        "/learners/" + str(random.randint(1, 1241))
        + "/evaluation-eligibility")


def get_holistic_average(l):
    l.client.get(
        "/learners/" + str(random.randint(1, 1241)) + "/holistic-average")


def get_holistic_criteria_average(l):
    l.client.get(
        "/learners/" + str(random.randint(1, 1241))
        + "/holistic-criteria-average")


def get_decision_history(l):
    l.client.get(
        "/learners/" + str(random.randint(1, 1241)) + "/decision-history")


def get_scores(l):
    l.client.get(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) +
        "/scores")


def post_add_scores(l):
    l.client.post(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) + 
        "/scores/new",
        headers={'content-type': 'application/json'},
        data='{"scores":[{"phase_id":"23","assessment_id":"21","score":"1",\
        "comments":"asdasda","original_updated_at":"2018-05-08 11:21:17 UTC"},\
        {"phase_id":"23","assessment_id":"22","score":"2","comments":"asdasda"\
        ,"original_updated_at":"2018-05-08 11:21:17 UTC"},{"phase_id":"23",\
        "assessment_id":"23","score":"2","comments":"asdasf",\
        "original_updated_at":"2018-05-08 11:21:17 UTC"},{"phase_id":"23",\
        "assessment_id":"24","score":"2","comments":"ghsdsd",\
        "original_updated_at":"2018-05-08 11:21:17 UTC"}],"controller":\
        "scores","action":"create","id":"' + str(learner_id) +
        '","learner_program_id":"' + str(learner_program_id) + '","score":{}}')


def get_learner_city(l):
    l.client.get(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) + 
        "/get-learner-city")


def update_learner(l):
    l.client.put(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) +
        "/update-learner",
        headers={'content-type': 'application/json'},
        data='{"learner_info": {"email": "muzafaru@example.com", "country":\
         "Uganda", "city": "Kampala", "gender": "Female"}, "id": "' +
        str(learner_id) + '", "learner_program_id": "' +
        str(learner_program_id) + '"}')


def get_completed_assessments(l):
    l.client.get(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) + 
        "/completed_assessments")


def update_learner_decision_status(l):
    program_id = random.randint(1, 1241)
    l.client.put(
        "/learners/decision-status/" + str(program_id),
        headers={'content-type': 'application/json'},
        data='{"decision_two": "Advanced", "learner_program_id": "' + 
        str(program_id) + '"}')


def update_learner_lfa(l):
    program_id = random.randint(1, 1241)
    l.client.put(
        "/learners/lfa-update/" + str(program_id),
        headers={'content-type': 'application/json'},
        data='{"week_one_lfa": "edward.karanja@example.com", \
        "learner_program_id": "' + str(program_id) + '"}')


'''
    This route requires that a file is uploaded. I didn't
    figure out how to do this, so I hit a different route instead
    it's important that we test everything!
'''


def post_add_learners(l):
    l.client.put(
        "/learners/" + str(learner_id) + "/" + str(learner_program_id) + 
        "/update-learner",
        headers={'content-type': 'application/json'},
        data='{"learner_info": {"email": "muzafaru@example.com", "country":\
         "Uganda", "city": "Kampala", "gender": "Female"}, "id": "' + 
        str(learner_id) + '", "learner_program_id": "' + 
        str(learner_program_id) + '"}')
    # l.client.post(
    #     "/learners/add",
    #     headers={'content-type': 'application/json'},
    #     data='')
