# Skills Framework for the Information Age (SFIA) - Project 2
---
# Generate your own Superhero name! 

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
    2. [My Proposal](#my_proposal)
    3. [Kanban Board](#kanban_board)
        1. [First Sprint](#sprint1)
        3. [Final Sprint](#final_sprint)
        4. [Future Sprint](#future_sprint)
3. [Feature Branch Model](#feature_branch)
4. [Risk Assessment](#risk_assessment)
    1. [Risk Assessment Matrix](#risk_matrix)
        1. [Likelihood Table](#likelihood_table)
        2. [Impact Table](#impact_table)
        3. [Risk Table](#risk_table)
        4. [Resulting Risk Matrix](#resulting_risk_matrix)
    2. [Initial Risk Assessment](#initial_risk_assessment)
    3. [Ongoing Risk Assessment](#ongoing_risk_assessment)
    4. [Final Risk Assessment](#final_risk_assessment)
5. [Project Architecture](#project_architecture)
    1. [Deployment](#project_deployment)
    2. [Wireframe Diagram](#use_case_diagram)
    3. [Service Architecture Diagram](#service_architecture_diagram)
    4. [Security](#project_security)
6. [Testing](#testing)
    1. [Unit Testing](#unit_testing)
    2. [Integration Testing](#integration_testing)
    3. [Testing Influence](#testing_influence)
7. [Retrospective](#retrospective)
    1. [What Went Well](#what_went_well)
    2. [What Didn't Go Well](#what_didn't_go_well)
    3. [Improvements for the Future](#improvements_for_the_future)
<!-- 6. [Installation Guide](#installation) -->
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
|Version Control System (VCS)|Git and Dockerhub|
|CI Server|Jenkins|
|Cloud server|GCP virtual machines|
|Containerisation|Docker|
|Configuration Management|Ansible|
|Orchestration Tool|Docker Swarm and Docker Stack|



|Additional Technology|Used in this project|
|:---:|:---:|
|Database|Google Cloud Platform (GCP) SQL Server|
|Programming language|Python and MySQL|
|Unit Testing with Python|Pytest|
|Integration Testing with Python|Coverage|
|Acceptance Testing with Python|Selenium|
|Front-end|Flask and HTML (including Jinja2, CSS and Bootstrap)|
|Load Balancing|Nginx|
|IDE|Visual Studio Code|


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
For this project I implemented an Agile methodology. I chose to use Agile over other methodologies, such as Waterfall, due to Agile's values and principles. These allow for dynamic project aims, prioritising working code over comprehensive documentation and for testing to be completed in the same iteration as programming.
However, the Agile methodology is intended to be implemented in a team environment working to produce a product for a customer. Due to the nature of my project being independent and not to be distributed to a customer, some of the values and principles had to be adapted:
+ **Individuals and Interactions over processes and tools:**
Normally, this would involve daily team scrums and sprint reviews, instead, I had a daily standup with my trainer, and used various project management tools such as gannt charts and kanban boards to maintain all areas of the project were being tracked simultaneously.
+ **Working Software over comprehensive documentation:**
This value is designed to prioritise a working end product over a un-finished well documented project. However, my projects scope is designed to make sure that I understand the content, hence, comprehensive documentation is required for the purpose of this project. Instead, I prioritised working functionalities over front-end design.
+ **Customer Collaboration over contract negotiation:**
The application would have no users or customers. So, I acted as the users and treated my trainer as a customer.
+ **Responding to Change over following a plan:**
All my project management allowed additional time for change.

### My Proposal <a name="my_proposal"></a>
My proposal for the solution to this project is to create a "Generate your own Superhero name" website. I took inspiration from popular quizzes on sites such as Buzzfeed. Users would be able to generate either random Superhero names for themselves, or be able to personalise the name based on a variety of user defined inputs, such as: type of superpower, their own name and good or evil.

Service #1 would serve as the user interface server and would provide the application with the user inputs and output the name back to the user. Services #2 and #3 would generate the names and Service #4 would store this information onto a file or equivalent (CSV or MySQL).

### Kanban Board <a name="kanban_board"></a>
As stated for the MVP, I was required to follow best practices within industry and use a Kanban board to manage my project. I chose to use the Trello application to create my Kanban board, due to my familiarity with the software, having seen it used at QA.

The board is designed around user stories to test the functionalities of the application. These stories are then represented in the product backlog. These product backlogs are then further broken down in to a sprint backlog, tasks, progress, done and bugs list. These additional lists allow for dynamic progress updates of the project and to maintain specific obtainable objectives throughout the project to allow for a deliverable product by the deadline.

I used the MoSCow Prioritisation Method on the Kanban Board with the following key:
|MoSCow Method Key|Colour Used|
|:---:|:---:|
|Must Have|Green|
|Should Have|Orange|
|Could Have|Yellow|
|Won't Have|Red|


I defined "done" as to mean that the feature had been successfully implemented into the application, and had no negative effect on the testing features. If a feature negatively impacted the test results, they were logged into the bugs column.

#### First Sprint <a name="sprint1"></a>
For my first sprint, I was still learning new content on Docker and the concept of containerisation. Hence a lot of the project work was project management, and basic fundamentals.
![Initial Kanban Board](https://i.imgur.com/atJdkjJ.png)

#### Second Sprint <a name="sprint2"></a>
As I entered the second sprint, I adapted my Kanban board to include dynamic rolling project management goals, such as initial, rolling and final risk assessments. I had successfully connected to my new VM and generated my initial risk assessment and matrix. I did however encounter my first bug; accessing the new VM via ssh. The authorisied keys file needed deleting and the SSH pub key needed re-entering into the GCP console. 
![Second Kanban Board](https://i.imgur.com/mF0Ax0e.png)

#### Third Sprint <a name="sprint3"></a>
The third sprint was to get the application to running off individual services that were yet to be connected in a internal network. Running each application independently they were able to pass information from one another. 
![Third Kanban Board](https://i.imgur.com/Y8G0SXi.png)

#### Fourth Sprint <a name="sprint4"></a>
By the fourth sprint, the application had been "dockerised". Using dockerswarm and stack, an internal network had been made for which the services could communicate between one another. 
![Fourth Kanban Board](https://i.imgur.com/Rv8vELO.png)

#### Fifth Sprint <a name="sprint5"></a>
I now needed to set up Jenkins, so that it would be activated by a github webhook to build and deploy the application every time the developer branch would merge with the master branch. Unfortunately this presented itself with a lot of new bugs, to install some of the required packages for Jenkins to run the pipeline, the VM that Jenkins was on needed to be restarted, this meant the IP address would be changed and numerous tweaks needed to be made to the backend of the application.
![Fifth Kanban Board](https://i.imgur.com/TKL138o.png)

#### Final Sprint <a name="final_sprint"></a>
The MVP had now been completed; the application was running on 4 independent services, each a container within a private network that was being orchestrated by ansible. The server was also set up using Jenkins to ensure a continuous integration.#
![Final Kanban Board](https://i.imgur.com/7TXfjxv.png)

#### Future Sprint <a name="future_sprint"></a>
If I had more time for this project, there are more features I would like to implement as detailed in the improvements for future section further down. My initial future sprint would be to implement a MySQL database such that the generated names would be saved to a database.
![Future Kanban Board](https://i.imgur.com/F1TnJga.png)

### Time Management <a name="time_management"></a>
I decided to use Gantt charts to better manage my time.
My initial Gantt chart was made at the start of the project and coincided with my initial Kanban board. I did not fully understand the scope of the project and so the chart is limited.
![Initial Gantt Chart](https://i.imgur.com/ZVc1MKX.png)
As the project progressed, I understood more of what needed to be done, but did not implement the risk assessment to allow for more time.
![Ongoing Gantt Chart](https://i.imgur.com/GaXhDZk.png)
As seen in my final gantt chart (current as of the day of completion), this is a reflection on the work done during the project. The biggest changes were that to work over weekends and bank holidays, as well as previous sections of the project having to be worked on and updated at various points in the project.
![Final and Future Gantt Chart](https://i.imgur.com/3tPDFZ8.png)

## Feature Branch Model <a name="feature_branch"></a>
For this project I used a feature branch model that has three tiers:
+ Master Branch, which is associated with the Jenkins CI webhook. This acts as the production application
+ Developer Branch, this manages all the features and only merges to the Master Branch once fully tested
+ Feature Branches, these branches are where the edits are made and then merged with the developer branch.
A diagram of this model is shown below:
![Feature branch model](https://i.imgur.com/hYX8eGv.png)

|Node|Description|
|:---:|:---:|
|A|Initial production version|
|B|Initial developer version|
|C,G,E,I|Feature branch, server #1,#2,#3 and #4 completed respectively and pushed to developer branch|
|D,F,H|Next production release pushed up from developer branch|
|J|Final production release|
|K|Ongoing Developer branch|

## Risk Assessment <a name="risk_assessment"></a>
A risk assessment determines possible mishaps, their likelihood and consequences, and the tolerances for such events. It is a combined effort of identifying and analysing potential (future) events that may negatively impact the project and making judgments on the tolerability of the risk on the basis of a risk analysis while considering influencing factors.

### Risk Assessment Matrix <a name="risk_matrix"></a>
A risk matrix is a matrix that is used during risk assessment to define the level of risk by considering the category of probability or likelihood against the category of consequence severity. This is a simple mechanism to increase visibility of risks and assist management decision making.
Risk is the lack of certainty about the outcome of making a particular choice and can be calculated as the the probability multiplied by the severity of a given risk.

#### Likelihood Table <a name="likelihood_table"></a>
| **Probability/Likelihood Value** | **Chance of occurring during the course of the project** |
|:---:|:---:|
| **1** | Rare (1% to 20%) |
| **2** | Unlikely (21% to 40%) |
| **3** | Possible (41% to 60%) |
| **4** | Likely (61% to 80%) |
| **5** | Certain (81% to 100%) |


#### Impact Table <a name="impact_table"></a>
| **Severity/Impacts Value** | **Negative effect on the project** |
|:---:|:---:|
| **1** | Minimal |
| **2** | Minor |
| **3** | Moderate |
| **4** | Major |
| **5** | Catastrophic |


#### Risk Table <a name="risk_table"></a>
| **Risk Value** | **Type of Risk** |
|:---:|:---:|
| 0-4 | Trivial |
| 5-9 | Tolerable |
| 10-14 | Moderate |
| 15-19 | Substantial |
| 20-24 | Extreme |
| 25+ | Intolerable |


#### Resulting Risk Matrix <a name="resulting_risk_matrix"></a>
|**Likelihood →** <br> **Impact ↓**|**Rare**|**Unlikely**|**Possible**|**Likely**|**Certain**|
|:---:|:---:|:---:|:---:|:---:|:---:|
|**Minimal**|Trivial|Trivial|Trivial|Trivial|Tolerable|
|**Minor**|Trivial|Trivial|Tolerable|Tolerable|Moderate|
|**Moderate**|Trivial|Tolerable|Tolerable|Moderate|Substantial|
|**Major**|Trivial|Tolerable|Moderate|Substantial|Extreme|
|**Catastrophic**|Tolerable|Moderate|Substantial|Extreme|Intolerable|

### Initial Risk Assessment <a name="initial_risk_matrix"></a>
The risks are broken down into two categories: Operational Risks and Objective Risks. These are represented by their Risk ID's: 1.X are Operational Risks and 2.X are Objective Risks.
The risk assessment is also broken into two categories: Risk Analysis and Risk Management.
The Risk Analysis categories are: Risk ID, Description, Likelihood, Impact, Consequence and Response Strategy.
The Risk Management categories are: Response Strategy.


|Risk ID|Description|Likelihood|Impact|Risk|Consequence|Response Strategy|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.1|Data compromised|Unlikely|Major|Tolerable|Potential loss of large sections of the project, resulting in setbacks|Using the branch feature in git, and ensuring a frequently updated branch method|
|1.2|GCP (Google Cloud Processing) budget limit exceeded|Rare|Minimal|Trivial|Personal financial cost, whilst minimal setback to project progress|Google provides $300 initial budget for all users, and disables the autopayment if the allowance runs out. To prevent this from becoming a problem, I have to ensure that feature doesn't become enabled, and to keep an eye on my remaining budget.|
|1.3|Internet Connectivity Problems|Likely|Major|Substantial|A lot of the work for this project is done on virtual machines and requires a constant internet connection. Missing this would require large periods of time without being able to work on or update the project|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|2.1|Time mismanagement|Possible|Major|Moderate|Falling behind on tasks means rushing on certain aspects of the project and can result in a lower quality of work.|Using methods such as a Trello board and gantt chart to track my progress and ensure I don't fall behind on my work. If my work starts to fall behind, I can work on my project before/after training hours. |
|2.2|Lack of content knowledge|Possible|Major|Substantial|A lack of understanding of the content covered in the academy will mean that I am unable to fulfill requirements needed for the project|I will first search the internet fo the answers to any questions I have, then seek peer help if I cannot find the answer, before finally approaching my trainer|
|2.3|Jenkins pipeline error|Unlikely|Minor|Trivial|A problem with Jenkins compatibility with the GitHub webhooks would mean that the pipeline would not automatically run for every push to GitHub, compromising the autonomy of the continuous integration|If not able to be resolved by the deadline, then manual build requests in Jenkins can be used.|

### Ongoing Risk Assessment <a name="ongoing_risk_matrix"></a>
As the project progressed, I encountered new problems that I had and hadn't forseen. I also became aware of new risks that could impact the progress of the project.
Some major problems from the initial risk assessment I was able to reduce the Likelihood and Impact, such as the internet connectivity problems. I was able to get a new ISP and the Likelihood of the Risk was reduced.

|Risk ID|Description|Likelihood|Impact|Risk|Consequence|Response Strategy|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.1|Data compromised|Unlikely|Major|Tolerable|Potential loss of large sections of the project, resulting in setbacks|Using the branch feature in git, and ensuring a frequently updated branch method|
|1.2|GCP (Google Cloud Processing) budget limit exceeded|Rare|Minimal|Trivial|Personal financial cost, whilst minimal setback to project progress|Google provides $300 initial budget for all users, and disables the autopayment if the allowance runs out. To prevent this from becoming a problem, I have to ensure that feature doesn't become enabled, and to keep an eye on my remaining budget.|
|1.3|Internet Connectivity Problems|Unlikely|Major|Trivial|A lot of the work for this project is done on virtual machines and requires a constant internet connection. Missing this would require large periods of time without being able to work on or update the project|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|1.4|GCP Service Error|Unlikely|Catastrophic|Moderate|A lot of the work for this project is done on virtual machines, hence a problem with the cloud service provider would mean the project would be unable to continue.|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|1.5|COVID-19|Possible|Major|Moderate|Due to the current pandemic, the range of symptoms due to the virus range from mild fever to hospitalisation and in some extreme cases, death.|I follow social distancing procedures and self isolation to reduce the risk of becoming infected|
|2.1|Time mismanagement|Possible|Major|Moderate|Falling behind on tasks means rushing on certain aspects of the project and can result in a lower quality of work.|Using methods such as a Trello board and gantt chart to track my progress and ensure I don't fall behind on my work. If my work starts to fall behind, I can work on my project before/after training hours. |
|2.2|Lack of content knowledge|Possible|Major|Substantial|A lack of understanding of the content covered in the academy will mean that I am unable to fulfill requirements needed for the project|I will first search the internet fo the answers to any questions I have, then seek peer help if I cannot find the answer, before finally approaching my trainer|
|2.3|Jenkins pipeline error|Likely|Moderate|Moderate|A problem with Jenkins compatibility with the GitHub webhooks would mean that the pipeline would not automatically run for every push to GitHub, compromising the autonomy of the continuous integration|If not able to be resolved by the deadline, then manual build requests in Jenkins can be used.|

### Final Risk Assessment <a name="final_risk_matrix"></a>
The final risk assessment, was the risk assessment as of the completion of the project.
Revaluation of various risks as well as additions have been included.

|Risk ID|Description|Likelihood|Impact|Risk|Consequence|Response Strategy|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.1|Data compromised|Unlikely|Major|Tolerable|Potential loss of large sections of the project, resulting in setbacks|Using the branch feature in git, and ensuring a frequently updated branch method|
|1.2|GCP (Google Cloud Processing) budget limit exceeded|Rare|Minimal|Trivial|Personal financial cost, whilst minimal setback to project progress|Google provides $300 initial budget for all users, and disables the autopayment if the allowance runs out. To prevent this from becoming a problem, I have to ensure that feature doesn't become enabled, and to keep an eye on my remaining budget.|
|1.3|Internet Connectivity Problems|Unlikely|Major|Trivial|A lot of the work for this project is done on virtual machines and requires a constant internet connection. Missing this would require large periods of time without being able to work on or update the project|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|1.4|GCP Service Error|Unlikely|Catastrophic|Moderate|A lot of the work for this project is done on virtual machines, hence a problem with the cloud service provider would mean the project would be unable to continue.|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|1.5|COVID-19|Possible|Major|Moderate|Due to the current pandemic, the range of symptoms due to the virus range from mild fever to hospitalisation and in some extreme cases, death.|I follow social distancing procedures and self isolation to reduce the risk of becoming infected|
|1.6|General Illness|Possible|Moderate|Tolerable|A range of illnesses could prevent me from continuing the project|Due to the pandemic, I am already practicing social distancing, but am staying healthy as to avoid other illnesses. If I were to become ill, I would alert my trainer as to ask for additional time if needed.|
|1.7|Family Crisis|Likely|Catastrophic|Extreme|Due to the current pandemic, the range of symptoms vary from mild to extreme. My Mother lives alone and is in the highest risk category, therefore if she were to become ill, I may need to care for her.|I have arranged procedures with my brothers to ensure that one of us could be there for my Mum is she becomes ill.|
|2.1|Time mismanagement|Possible|Major|Moderate|Falling behind on tasks means rushing on certain aspects of the project and can result in a lower quality of work.|Using methods such as a Trello board and gantt chart to track my progress and ensure I don't fall behind on my work. If my work starts to fall behind, I can work on my project before/after training hours. |
|2.2|Lack of content knowledge|Possible|Major|Substantial|A lack of understanding of the content covered in the academy will mean that I am unable to fulfill requirements needed for the project|I will first search the internet fo the answers to any questions I have, then seek peer help if I cannot find the answer, before finally approaching my trainer|
|2.3|Jenkins pipeline error|Likely|Moderate|Moderate|A problem with Jenkins compatibility with the GitHub webhooks would mean that the pipeline would not automatically run for every push to GitHub, compromising the autonomy of the continuous integration|If not able to be resolved by the deadline, then manual build requests in Jenkins can be used.|
|2.4|Dockerhub repository error|Unlikely|Moderate|Tolerable|If I were unable to provide the Docker swarm network with a version controlled image, then it is not best practice for DevOps tools.|The online feature is best practice but offline images can be used if the service is not available.|

## Project Architecture <a name="project_architecture"></a>
### Tools <a name="project_tools"></a>
+ Docker:
Docker is a container service that allows RAM+CPU to be distributed throughout the containers. This makes the application more efficient.
+ Docker Swarm and Stack:
Docker Swarm is an orchestration tool that allows us to cluster Docker containers on different nodes for redundancy and high availability, meaning we can have containers deployed over multiple virtual machines.
Whilst stack allow us to deploy multiple services at once
+ Ansible:
Ansible is an open-source software provisioning, configuration management, and application-deployment tool. It allows for automation of deployment of containers across nodes.
### Deployment <a name="project_deployment"></a>
I made a deployment diagram at the start of the project to show how I initially intended the application to be deployed and set up.
![Initial Deployment](https://i.imgur.com/R9XrkOq.png)
By the end of the project, the application had adapted; I had removed the MySQL, and included NGINX and Ansible.
![Final Deployment](https://i.imgur.com/xQiKHno.png)
### Front-end Wireframe <a name="use_case_diagram"></a>
At the start of the project, this is how I wanted the front end to look.
![Initial Wireframe](https://i.imgur.com/kwvvcIV.png)
As it adapted, I just used two implementations based on forms, not user input.
![Final Wireframe](https://i.imgur.com/qnbNYZ8.png)
### Service Architecture Diagram <a name="service_architecture_diagram"></a>
How I initially intended the application to be deployed.
![Initial Service Architecture Diagram](https://i.imgur.com/l7IkDhz.png)
How the application was deployed at the end.
![Final Service Architecture Diagram](https://i.imgur.com/EkUmIRl.png)

### Security <a name="project_security"></a>
This project was designed to focus on efficiency and security. With the efficiency comes more security risks, so it is important that the security has been improved form the previous project.
As shown in my testing bellow, there are no exposed ports on both the master and worker nodes, showing that port 5000 isn't exposed on any of the containers. I used NGINX to port 80 reverse proxy into service_1.
My GCP firewall rules only expose port 80 (NGINX) publicly. My Jenkins (port 8080) is exposed to the home and use NGINX.

## Testing <a name="testing"></a>
I used a unit, integration and acceptance testing method as a measure of my code quality for the application.

### Unit Testing <a name="unit_testing"></a>
Unit testing is where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit usually has one or a few inputs and usually a single output. I ran tests to test the functionality of the application and the security of both nodes, as the project progressed I included more tests, resulting in a final 16 tests.
![Pytest](https://i.imgur.com/jAVxZy3.png)

### Integration Testing <a name="integration_testing"></a>
Integration testing is where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units. Coverage reports is a type of integration testing, and a target of +35% is adequate, 50%+ is acceptable and 80+% is desired. My final coverage resulted in %51 coverage making it acceptable, I aimed for a minimum fo 35 as the project progressed, but included further tests and security to get the coverage to above 50.
![Coverage Report](https://i.imgur.com/FFZQEE7.png)


### Influence <a name="testing_influence"></a>
My testing results influence the structure of my code. Initially I had intended to have all my ports secure and to be accessed through a NGINX reverse proxy, however, the testing showed that the ports were resulting in a 200 (success) page, so it was failing the tests. I was then able to properly implement the security protocols to be able to get the ports returning a 500 error, for both the master and worker nodes.

## Retrospective  <a name="retrospective"></a>
### What went well <a name="what_went_well"></a>
+ **Docker Swarm and Stack:**
I was able implement a Swarm and stack Service for my project, which would allow multiple nodes to communicate with each other over a overlay network. This improved the efficiency due to the sharing of docker images/containers.
+ **NGINX:**
The security of the site is greatly improved due to the implementation of NGINX, this allowed the application to hide any exposed ports that would have otherwise been a security flaw.
+ **Jenkins:**
My Jenkins used a webhook to clone the master branch of my code. My feature branch model allowed for full testing and version control without having to keep building my application. This level of automation and efficiency was greatly improved over my last project.
+ **Ansible:**
Ansible helped with the automation and allowed me to deploy the application on a worker node without further work past the setup.

### What didn't go well <a name="what_didn't_go_well"></a>
+ **Implementations:**
The imagination of the application itself is very limited. I did not include as many implementations as I would have liked.
+ **Database:**
I was unable to successfully have a MySQL database integration with the application
+ **Security:**
My Ansible inventory.cfg file is pushed up to github so that it can be downloaded by Jenkins. This should be kept private.

### Improvements for the future <a name="improvements_for_the_future"></a>
If I had more time dedicated to this project I would have implemented the following:
+ **Increased testing coverage:**
Although I was happy with my unit and integration testing results, as the site would expand with the further improvements so would the testing procedures to ensure the high quality of the site. 
+ **Improved UI:**
Due to the nature of Agile, I prioritised working CRUD functionality over the documentation and presentation of the project. This meant I did not spend time on the design aspects of the site.
+ **Acceptance Testing:**
My testing protocol only included unit and integration testing. Had more time been allowed, I would have researched and implemented further methods of testing. Acceptance Testing, also known as operational readiness testing, refers to the checking done to a system to ensure that processes and procedures are in place to allow the system to be used and maintained. This includes checks done to back-up facilities, procedures for disaster recovery, training for end users, maintenance procedures, and security procedures.
+ Selenium is a portable framework for testing front-end web applications.
+ SonarQube is an open-source platform for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs, code smells, and security vulnerabilities. It offers reports on duplicated code, coding standards, unit tests, code coverage, code complexity, comments, bugs, and security vulnerabilities. SonarQube can also record metrics history and provides evolution graphs as well as providing fully automated analysis and integration with CI integration tools such as Jenkins.
+ **MySQL Database**
I had initially intended to have MySQL integration with the application, but due to time limitations I had to exclude this feature
+ **More implementations**
A more complex python backend to allow for Easter Eggs and more personalised name generation for the application.
+ **More nodes:**
If more time were allowed I would have also attempted to include more nodes within the network.

<!-- ## Install Guide <a name="installation"></a>
Provide support and advice to an initial user looking to use this application.
Include how to deploy application, whilst keeping brief (use bullet points).
Include steps like: git clone, install jenkins, etc.
Be able to answer questions on this -->

## Authors <a name="authors"></a>
Thomas Cole - QA Academy Trainee

## Acknowledgements <a name="acknowledgements"></a>
I would like to acknowledge the QA trainers and other members of my cohort, who were able to help me with any problems I had with my project.