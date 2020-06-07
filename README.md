# Deviget: SDET--SG

``Deviget`` exercise for ``SDET`` position.

##### Table of Contents
- [About this repository](#about-this-repository)
- [Technical decisions](#technical-decisions)
- [Testing environment](#testing-environment)
- [How to run tests](#how-to-run-tests)



## About this repository

This repository contains the solution for **``Deviget``** exercise for **``SDET``** position.

**Exercise description**: *As a Customer we want to see if the second Iphone related ad from the second results page 
from www.aliexpress.com has at least 1 item to be bought.*


The ``test case`` related to the exercise description is defined in the following feature file:

* [Feature: Product availability](tests/ui/aliexpress/features/product_availability.feature)

Actually, there are 2 scenarios defined in that feature file, both follow the test description.

Each test case can be executed using **``Chrome``** or **``Firefox``** browsers.


## Technical decisions

The framework selected for the implementation of the test cases is [**Behave**](https://behave.readthedocs.io/en/latest/).

`Behave` is behaviour-driven development, `Python` style. It is based on tests written in a natural language style, 
backed up by Python code.

Behavior-driven development (or `BDD`) is an agile software development technique that encourages collaboration 
between developers, QA and non-technical or business participants in a software project.

The language used to describe the different application functionalities is `Gherkin`. It handles two purposes: 
serving as your project's documentation and automated tests.

For automate real user interactions with browsers, it is chosen `Selenium Webdriver` framework (see 
[selenium-python](https://selenium-python.readthedocs.io/) documentation)

Regarding the design pattern, AliExpress web pages are modeled using `Page objects`. Each class defined in 
[page_objects](tests/ui/aliexpress/page_objects/) acts as interfaces for page interaction.

For test report generation [cucumber-html-reporter](https://www.npmjs.com/package/cucumber-html-reporter) is used.

Testing environment is [**dockerized**](https://www.docker.com/) making it easier to be integrated in any CI/CD 
pipeline, and also to run in different OS host machines.


## Testing environment

It is only necessary to have `docker` installed and running in the host machine to execute the test suit 
(with chrome or firefox browser).

The test environment is a `docker-compose` environment defined in [ui_tests.yml](ui_tests.yml).

It has 3 main components:

* A `selenium/standalone-chrome` service (based on a specific docker image),
* A `selenium/standalone-firefox` service (based on a specific docker image), and
* A `test_runner` service, that is built based on [test_runner/Dockerfile](test_runner/Dockerfile) definition.

The test runner is basically a `python` docker container which has also installed `npm` for generating 
test suit `html` reports.


### How to run tests

You can simply run **``./script/ui_test``** 😄 (Source: [script/ui_test](script/ui_test))

If you manually want to run or edit UI tests, start the [ui_tests.yml](ui_tests.yml) docker-compose 
environment by running:

```bash
docker-compose -f ui_tests.yml up &
```

To check running services in the docker-compose environment then execute:
```bash
docker-compose -f ui_tests.yml ps
```

To run all defined UI tests, execute:

```bash
docker-compose -f ui_tests.yml exec test_runner tests/ui/run
```

The default browser is ``chrome``, but you can also run test using firefox by setting ``BROWSER=firefox`` 
environment variable:

```bash
docker-compose -f ui_tests.yml exec -e BROWSER=firefox test_runner tests/ui/run
```

If you want to edit or add new UI tests, then run the following command and work on your any editor locally:
```bash
docker-compose -f ui_tests.yml exec test_runner /bin/bash
```

To see what is happening in the browser while running tests, it is possible to use `VNC Viewer` and configure 
`chrome` or `firefox` connections (`localhost:9000` or `localhost:9001` respectively, 
according to current yml definition).

After everything is done, down the docker-compose environment:

```bash
docker-compose -f ui_tests.yml down -v
