import random

'''
    This file contains routes that are prefixed
    with /program in the VOF routes.

    You will notice a lot of "random.choice([1, 4])"
    This is to ensure if a program_id is needed in the url
    it is as dynamic as possible. This can being up unforseen
    bugs when different combinations of parameters are used.
'''


def get_program_status(l):
    l.client.get("/program/" + str(random.choice([1, 4])) + "/program-status")


def get_program_dlc_stack(l):
    l.client.get("/program/" + str(random.choice([1, 4])) + "/dlc-stack")


def get_program(l):
    l.client.get("/program/" + str(random.choice([1, 4])))


'''
    This particular url has ambigiuos parameters
    find out if this url is used and how we can test it
    thoroughly.
'''


def get_program_size(l):
    # l.client.get("/programs/:size/:page")
    l.client.get("/program/" + str(random.choice([1, 4])))


def get_program_center_cycles(l):
    l.client.get(
        "/programs/" + str(random.choice([1, 4])) + "/centers/"
        + str(random.choice(["Kampala", "Nairobi", "Lagos"])) + "/cycles")


def get_program_assessments(l):
    l.client.get("/program/" + str(random.choice([1, 4])) + "/assessments")
