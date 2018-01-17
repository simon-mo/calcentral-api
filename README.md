# calcentral-api
An unofficial tool for CalCentral Automation (UC Berkeley's Student Info System)

## Overview

This repo contains basic code to navigate through CalCentral. 

Here are few features:

- User Authentication
- Download "Course Capture" Links

Here are few limitations:

- It can be slow. So far I can't find a way to hack the authentication without actual let the agent to be a browser (which has javascript support). Thus, all I can do is use `selenium` and `ChromeWebDriver` to authenticate. 

## Get Started

1. `brew install selenium-server-standalone`
2. `pip install -U selenium`
3. Download Chrome Webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
