# Skills Framework for the Information Age (SFIA) - Project 2
:---:
# TBA

This is a project, worked on independently of others, in reference to the QA Learning Academy training base project specification; Practical Project Specification - DevOps Core. The purpose of this project is to fulfill the specification defined for the assignment due Tuesday 14th April 2020, 09:00.


## Contents
1. [Brief](#brief)
    1. [Minimal Viable Product (MVP)](#mvp)
    2. [Tech Stack Requirements](#tech_stack)
    3. [Project Architecture](#project_architecture)
        1. [Service #1](#service1_architecture)
        2. [Service #2 and #3](#service2&3_architecture)
        3. [Service #4](#service4_architecture)
2. [Project Management](#project_management)
    1. [Agile Methodology](#agile)
    2. [Kanban Board](#kanban_board)
        1. [First Sprint](#sprint1)
4. [Risk Assessment](#risk_assessment)
5. [Improvements for the Future](#improvements_for_the_future)
6. [Authors](#authors)
7. [Acknowledgements](#acknowledgements)

## Brief <a name="brief"></a>
The purpose of this project is to create an application that involves the concepts that build on from the SFIA Fundamental Project; more specifically, this will involve:
+ Software Development with Python
+ Continuous Integration (CI)
+ Cloud Fundamentals

The resulting aim of the project is to create an application that generates "Objects" upon a set of predefined rules and a CI Pipeline with full documentation around utilisation of supporting tools. The CI Pipeline needs to be able to successfully deploy the application as per the requirements.

### Minimum Viable Product (MVP) <a name="mvp"></a>
The Minimum Viable Product (MVP) for the project has the following requirements:
+ A Kanban board with full expansion on user stories, use cases and tasks needed to complete the project.
+ An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine. 
+ The project must follow the Micro Services architecture as per the requirements. 
+ The project must be deployed using containerisation and an orchestration tool.
+ Create an Ansible Playbook that will provision the environment that the application needs to run.

### Tech Stack Requirements <a name="tech_stack"></a>
The Tech Stack requirements are the following:
|Technology Required|Used in this project|
|:---:|:---:|
|Kanban Board|Trello|
|Version Control System (VCS)|Git|
|CI Server|Jenkins|
|Cloud server|GCP virtual machines|
|Containerisation|Docker|
|Configuration Management|Ansible|
|Orchestration Tool|Docker Swarm|

|Additional Technology|Used in this project|
|:---:|:---:|
|Database|Google Cloud Platform (GCP) SQL Server|
|Programming language|Python (including MySQL)|
|Unit Testing with Python|Pytest|
|Integration Testing with Python|Coverage|
|Acceptance Testing with Python|Selenium|
|Front-end|Flask (including Jinja2) and HTML (including CSS and Bootstrap)|

### Project Architecture <a name="project_architecture"></a>
The application must use a micro-service orientated architecture composed of at least 4 services that work together. Services #2, #3 and #4 each need to create 2 different implementations, and must be able to demonstrate swapping these implementations out for each other seamlessly, without disrupting the user experience. 

#### Service #1 <a name="service1_architecture"></a>
Service #1 will act as the core service. Service 1 will render the Jinja2 templates needed to interact with the application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

#### Service #2 and #3 <a name="service2&3_architecture"></a>
Services #2 and #3 will both generate a random “Object”.

#### Service #4 <a name="service4_architecture"></a>
Service #4 will also create an “Object” however this “Object” must be based upon the results of service #2 and #3 using some pre-defined rules.

## Project Management <a name="project_management"></a>
This section will detail the project management tools and techniques used to plan the project, and how they were utilised and adapted throughout the project.

### Agile Methodology <a name="agile"></a>
Similar to the SFIA foundation project, I implemented an Agile methodology over the Waterfall methodology due to Agile's values and principles allowing for testing to be completed in the same iteration as programming, dynamic project aims and working code over comprehensive documentation.
Due to the nature of my project, some of the values and principles of Agile had to be adapted:
+ **Individuals and Interactions over processes and tools:**
The project was an individual project, so there was no need for team interactions such as daily scrums.
Instead, I provided plenty feedback to my trainer and documentation.
+ **Working Software over comprehensive documentation:**
The purpose of this project is to show my understanding of the content taught in the from weeks five to eight.
So comprehensive documentation is important, however, I took adapted this value to mean that the application must be functional over beautiful.
+ **Customer Collaboration over contract negotiation:**
This project had no customer, other than users and the trainers at QA. So, I imagined virtual users and treated my trainer as a customer.
+ **Responding to Change over following a plan:**
All my project management allowed additional time for change.

### Kanban Board <a name="kanban_board"></a>
As stated for the MVP, I was required to follow best practices within industry and use a Kanban board to manage my project. I chose to use the Trello application to create my Kanban board, due to my familiarity with the software, having seen it used at QA.

The board is designed around user stories to test the CRUD functionalities of the application. These stories are then represented in the product backlog, along with other features needed for the specifics of the project (create this README file for example). These product backlogs are then further broken down in to a sprint backlog, tasks, progress, done and bugs list. These additional lists allow for dynamic progress updates of the project and to maintain specific obtainable objectives throughout the project to allow for a deliverable product by the deadline.

I defined "done" as to mean that the feature had been successfully implemented into the application, and had no negative effect on the pytest application which is detailed later.
Any implemented feature that negatively effected the performance of the application were logged into the bugs column.

#### First Sprint <a name="sprint1"></a>
To include the initial kanban board and an updated board per completed sprint.


## Feature Branch Model <a name="feature_branch"></a>

## Risk Assessment <a name="risk_assessment"></a>
The Risk Analysis categories are: Risk ID, Description, Likelihood, Impact, Consequence and Response Strategy.
The Risk Management categories are: Response Strategy.
Risk IDs 1.X are Operational Risks and 2.X are Objective Risks.

| **Probability/Likelihood Value** | **Chance of occurring during the course of the project** |
|:---:|:---:|
| **1** | Rare (1% to 20%) |
| **2** | Unlikely (21% to 40%) |
| **3** | Possible (41% to 60%) |
| **4** | Likely (61% to 80%) |
| **5** | Certain (81% to 100%) |

| **Severity/Impacts Value** | **Negative effect on the project** |
|:---:|:---:|
| **1** | Minimal |
| **2** | Minor |
| **3** | Moderate |
| **4** | Major |
| **5** | Catastrophic |

Risk Assessment Matrix
A risk matrix is a matrix that is used during risk assessment to define the level of risk by considering the category of probability or likelihood against the category of consequence severity. This is a simple mechanism to increase visibility of risks and assist management decision making.
Risk is the lack of certainty about the outcome of making a particular choice and can be calculated as the the probability multiplied by the severity of a given risk.

| **Risk Value** | **Type of Risk** |
|:---:|:---:|
| 0-4 | Trivial |
| 5-9 | Tolerable |
| 10-14 | Moderate |
| 15-19 | Substantial |
| 20-24 | Extreme |
| 25+ | Intolerable |

Therefor the resulting risk matrix is:
|**Likelihood →** <br> **Impact ↓**|**Rare**|**Unlikely**|**Possible**|**Likely**|**Certain**|
|:---:|:---:|:---:|:---:|:---:|:---:|
|**Minimal**|Trivial|Trivial|Trivial|Trivial|Tolerable|
|**Minor**|Trivial|Trivial|Tolerable|Tolerable|Moderate|
|**Moderate**|Trivial|Tolerable|Tolerable|Moderate|Substantial|
|**Major**|Trivial|Tolerable|Moderate|Substantial|Extreme|
|**Catastrophic**|Tolerable|Moderate|Substantial|Extreme|Intolerable|


|Risk ID|Description|Likelihood|Impact|Risk|Consequence|Response Strategy|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.1|Data compromised|Unlikely|Major|Tolerable|Potential loss of large sections of the project, resulting in setbacks|Using the branch feature in git, and ensuring a frequently updated branch method|
|1.2|GCP (Google Cloud Processing) budget limit exceeded|Rare|Minimal|Trivial|Personal financial cost, whilst minimal setback to project progress|Google provides $300 initial budget for all users, and disables the autopayment if the allowance runs out. To prevent this from becoming a problem, I have to ensure that feature doesn't become enabled, and to keep an eye on my remaining budget.|
|1.3|Internet Connectivity Problems|Likely|Major|Substantial|A lot of the work for this project is done on virtual machines and requires a constant internet connection. Missing this would require large periods of time without being able to work on or update the project|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|2.1|Time mismanagement|Possible|Major|Moderate|Falling behind on tasks means rushing on certain aspects of the project and can result in a lower quality of work.|Using methods such as a Trello board and gantt chart to track my progress and ensure I don't fall behind on my work. If my work starts to fall behind, I can work on my project before/after training hours. |
|2.2|Lack of content knowledge|Possible|Major|Substantial|A lack of understanding of the content covered in the academy will mean that I am unable to fulfill requirements needed for the project|I will first search the internet fo the answers to any questions I have, then seek peer help if I cannot find the answer, before finally approaching my trainer|
|2.3|Jenkins pipeline error|Unlikely|Minor|Trivial|A problem with Jenkins compatibility with the GitHub webhooks would mean that the pipeline would not automatically run for every push to GitHub, compromising the autonomy of the continuous integration|If not able to be resolved by the deadline, then manual build requests in Jenkins can be used.|

## Testing
I used a unit and integration testing method as a measure of my code quality for the application.

### Unit Testing
Unit testing is where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit usually has one or a few inputs and usually a single output. It is the smallest testable part of any software, hence why I ran a URL and DB pytest to test each CRUD function and URL link.

### Integration Testing
Integration testing is where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units. Coverage reports is a type of integration testing, and a target of +45% is acceptable and 80+% is desired. Add discussion for more marks.

### Acceptance Testing
Also known as operational readiness testing, this refers to the checking done to a system to ensure that processes and procedures are in place to allow the system to be used and maintained. This may include checks done to back-up facilities, procedures for disaster recovery, training for end users, maintenance procedures, and security procedures.
Selenium is a portable framework for testing web applications (front-end). Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language (Selenium IDE). It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. The tests can then run against most modern web browsers. Selenium runs on Windows, Linux, and macOS. It is open-source software released under the Apache License 2.0.

## Improvements for the future <a name="improvements_for_the_future"></a>
If I had more time dedicated to this project I would have implemented the following:
+ **Increased testing coverage:**
As shown previous in the coverage report section of the readme file, there was little coverage of the application, even though a lot of its core features where tested. This is definitely an area i would like to improve in later projects.
+ **Improved UI:**
Due to the nature of Agile, I prioritised working CRUD functionality over the documentation and presentation of the project. This meant I did not spend time on the design aspects of the site.
+ **Selenium testing:**
My testing protocol only included unit and integration testing. Had more time been allowed, I would have researched and implemented further methods of testing.
+ **Complex version control branch model:**
I only used two branches in my project; a master branch and developer branch. To help prepare better for best practice in industry, I would have further branches underneath the developer branch for each product backlog then further branches for the sprint backlogs and then again for the tasks.

## Authors <a name="authors"></a>
Thomas Cole - QA Academy Trainee

## Acknowledgements <a name="acknowledgements"></a>
I would like to acknowledge the QA trainers and other members of my cohort, who were able to help me with any problems I had with my project.