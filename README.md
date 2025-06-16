# Portfolio Project 5

## How to use this repo

Fork this repo.

In your forked churnometer repo click on the green Code button.

Then, from the Codespaces tab, click Create codespace on main.

Wait for the workspace to open. This can take a few minutes.

Open a new terminal and pip3 install -r requirements.txt

Click the kernel button and choose Python Environments.

Choose the kernel Python 3.12.1 as it inherits from the workspace, so it will be Python-3.12.1 as installed by Codespaces. To confirm this, you can use ! python --version in a notebook code cell.

Your workspace is now ready to use. When you want to return to this project, you can find it in your Cloud IDE Dashboard. You should only create 1 workspace per project.

## Dataset Content

* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data.

The dataset contains information about AI developers over 500 days.

| Variable | Meaning | Unit |
| :-----: | :----- | :-----|
| hours_coding | Total focused hours spent on software development work (0–12 hours) | 0–12 hours |
| coffee_intake_mg | Daily caffeine intake in milligrams | 0–600 mg |
| distractions | Number of distractions (e.g., meetings, Slack notifications) | 0–10 |
| sleep_hours | Number of hours of sleep the previous night | 3–10 hours |
| commits | Number of code commits pushed during the day | 0–20 |
| bugs_reported | Number of bugs reported in code written that day | 0–10 |
| ai_usage_hours | Number of hours spent using AI tools  | 0–12 |
| cognitive_load | Self-reported mental strain | a scale of 1 to 10 |
| task_success | Whether the daily productivity goal was achieved | 0 or 1 where 0 = no and 1 = yes |

## Terms and Jargon

* Examples for AI tools: ChatGPT, Copilot

## Business Requirements

* Describe your business requirements

1. The client would like to know which factors are most relevant for task success.
2. Furthermore the client is interested if there is a "sweet spot" for the use of AI tools in terms of hours in relation to task success.
3. The client would like to have a model to predict whether or not a developer is likely to not succeed based on the most relevant factors.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them)

* We suspect that the most relevant factors will be sleep_hours (because sleeping to little leads to a lack of focus), distractions (since that holds someone back from doint the work), ai_usage (since depending on the amount, too much usage will result in a poorer outcome).
  * We will conduct a correlation study.
* We hypothesize that there is a certain range of usage that is beneficial for task success. However, too much might lead to a confusing code or even distract from doing the work.
  * The results from the study mentioned above should give us the necessary insights.
* We suspect that we can create a model that can reliably predict which developer needs help based on the most relevant factors.
  * After finding the most relevant factors will train and test model.

## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks

* Business Requirement 1: Correlation study with data visualization
  * We will inspect the data related to the productivity of AI developers.
  * We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to `task_success`.
  * We will search for the four top correlated variables
  * We will plot the main variables against `task_success` to visualize insights.

* Business Requirement 2: Correlation study with data visualization
  * In the correlation study we will also answer the question if there is a certain amount of AI tools usage that is beneficial to productivity measured in successfully completing a task and what this amount is.

* Business Requirement 3: Predicting task success
  * We want to predict if a developer will succeed in task completion.
  * For that We want to build a binary classifier that uses the most relevant variables from the dataset.

## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

### Predict Task Success

#### Classification Model

* We want an ML model to predict if a developer will succeed in task completion based on the dataset. The target variable is numerical. We consider a classification model with the outcome of: 0 (no task success) and 1 (task success)
* Our ideal outcome is to provide the client with insights on where they can help their developers with task completion.
* The model success metrics are
  * at least 80% Recall for no task success, on train and test set
* The model output is defined as a flag, indicating if a developer will succeed in task completion or not and the associated probability of not succeeding.
* Heuristics: Currently, there is no approach to task success.
* The training data to fit the model comes from a dataset containing records of 500 days of AI developers.
  * Train data - target: `task_success`; features: all other variables.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

### Page 1: Short project summary

Project Terms & Jargon
Describe Project Dataset
State Business Requirements

### Page 2: Productivity Study

Before the analysis, we knew we wanted this page to answer business requirement 1 and 2, but we couldn't know in advance which plots would need to be displayed.
After data analysis, we agreed with stakeholders that the page will:
State business requirement 1
State business requirement 2
Checkbox: data inspection on AI developer dataset (display the number of rows and columns in the data, and display the first ten rows of the data)
Display the most correlated variables to task_success and the conclusions
Checkbox: Individual plots showing the task_success levels for each correlated variable

### Page 4: Project Hypothesis and Validation

Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:

* We suspect that the most relevant factors will be `sleep_hours`
(because sleeping to little leads to a lack of focus), `distractions`
(since that holds someone back from doint the work), `ai_usage_hours`
(since depending on the amount, too much usage will result in a
poorer outcome).
This proved to be mostly incorrect. The most relevant factors are
`caffeine_intake_mg` and `hours_coding` which show a strong positive
correlation to `task_success`. The use of AI shows only a weak
correlation."

* We hypothesize that there is a certain range of usage that is
beneficial for task success. However, too much might lead to a
confusing code or even distract from doing the work.
This proved to be correct. At 2-hour mark of AI usage the data shows
the biggest discrepancy between task success and no task success
suggesting that this might be the sweet spot for AI usage.

* We suspect that we can create a model that can reliably predict
which developer needs help based on the most relevant factors.
This proved to be correct (see test results under Predict Task Success).
However, we were suprised to learn that `caffeine_intake_mg` was the
most relevant factor with more than double the importance than the
second place which was `cognitive_load` and common sense suggests
that there might be more to it. That is why further analysis might
be justifed to see if it really is just the caffeine intake that
drives the successful completion of a task or if it just a proxy for
an underlying correlation that is the real reason. (E.g. maybe
developers who take in more caffeine also code the optimum amount of
hours like others ut are also more alert thus making more progress
with less errors.)

### Page 5: Predict Task Success

State business requirement 2.

Considerations and conclusions after the pipeline is trained
Present ML pipeline steps
Feature importance
Pipeline performance

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

* I was not able to fix the 'FutureWarning' when I ran a code cell that used the ppscore package in the 'DataCleaning' notebook. The message was:  
  "/home/cistudent/.local/lib/python3.12/site-packages/ppscore/calculation.py:201: FutureWarning: is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype CategoricalDtype) instead or is_categorical_dtype(series)".  
  If I updated ppscore it caused a compatibility error with pandas since it needed pandas<2.0.0,>= 1.0.0. However, downgrading pandas was also not a good option since when ydata-profiling called visions it needed pandas>=2.0.0. Downgrading visions to version 0.7.5 was compatible with the pandas<2.0.0 but then in turn incompatible for the purposes it was called by ydata-profiling.  
  So in short: Either ppscore would not work or ydata-profiling (or better visions) depending on the pandas version. So I decided, since it was 'only' a future warning and not error to hide it from view.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log into your Heroku account
2. Click on 'New' in the upper right-hand corner.
3. From the dropdown menu select 'Create new app'.
4. Give the app a name of your choosing.
5. Choose your location.
6. (Don't add to pipeline.)
7. Click on the 'Deploy'-tab.
8. Under 'Deployment Method' choose 'GitHub'.
9. Search for your copy of the repository and choose it.
10. Click on 'Deploy Branch' and wait until the built is done.
11. 
12. At the Deploy tab, select GitHub as the deployment method.
13. Select your repository name and click Search. Once it is found, click Connect.
14. Select the branch you want to deploy, then click Deploy Branch.
15. Click now the button Open App on the top of the page to access your App.

Note: If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

