# Stress Testing

## Setting Up VOF for stress testing

1. Checkout the `vof-stress-testing` branch on VOF and deploy that branch to the `learning` Google Cloud project.

**NOTE: The `vof-stress-testing` branch has no authentication enabled. This is because it was terribly hard, with locust, to authenticate users with gmail and exchange cookies with the application. This should be able to be bypassed with introduction of email:password combination for login. That said, ensure you set up a firewall rule to only allow the locust server IP (and probably your own) to access the server over HTTP & HTTPS**

## Setup locust server

2. There should be an instance called `locust-io-stress-testing` on the `learning` Google Cloud project, start that server. It already has locust setup
3. However, if the server does not exist follow the steps on [setting up a locust server](https://docs.locust.io/en/stable/installation.html)
4. Clone the deployment scrips repo into the locust server to access the stress test scripts

## Test

5. [Start locust](https://docs.locust.io/en/stable/quickstart.html#start-locust) and enter the number of users you'd like to test with in the UI that is shown when you visit the [locust dashboard](https://docs.locust.io/en/stable/quickstart.html#open-up-locust-s-web-interface)

## HAPPY TESTING!
