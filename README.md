# Study Buddies 
Welcome to the Study Buddies Project. 

Study Buddies is a website dedicated to sharing study and exam tips to all who need it. Exam season can be stressful and knowing where to begin studying can be intimidating, therefore this site lets people (who've been through it all) to share any tips and tricks they want to. A source of inspiration for this site was Wikipedia. On Wikipedia people can share anything they'd like (as long as it follows the rules) regarding any topic. Whilst Wikipedia encompasses all topics related to absolutely anything in the world, Study Buddies focus on specifically studying, whether it's studying just for revision or studying for the all dreaded exam. Similar to Wikipedia, logged in users can share their own posts which ensures we have the latest tips and tricks and we can be sure they work! Even more importantly, it's crucial to be aware that everybody has different ways of working and studying. Because Study Buddies consists of posts written by users, we can be sure there is a plethora of information suitable for every need. The primary focus of the site is to provide advice based on previous experience of users. However, fundamentally StudyBuddies is a site which users can utilise for their journey in education regardless of where they're at. Therefore users also share other posts (not necessarily study tips or exam tips) such as exam-style questions. 

You can view the deployed site [here](https://studybuddies-pp4-87eb5b7c6767.herokuapp.com/)

# Contents
* [**Project**](<#project>)
    * [Users Goal](<#users-goal>)
    * [Owners Goal](<#owners-goal>)
    * [Agile](<#agile>)
* [**User Experience**](<#user-experience>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
* [**Features**](<#features>)
    * [Header](<#header>)
    * [Navigation](<#navigation>)
    * [Pages](<#pages>)
    * [Footer](<#footer>)
    * [Comments](<#comments>)
    * [More Features](<#more_features>)
* [**Technologies Used**](<#technologies_used>)
* [**Tests**](<#tests>)
  * [Manual Testing](<#manual-testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Code**](<#code>)
* [**Acknowledgements**](<#acknowledgements>)


# **Project**
## Users Goal
The user is somebody who would like to find out more information about the best ways to study both in regular day to day studying and for exams. It can be used as a study tool also if a user decides to share subject related quizzes or questions. 

## Owners Goal
The owner would like the community to be able to share tips and tricks to readers of the site to make studying and exams easy. Furthermore, StudyBuddies can be used as a tool for users to study as users can share questions for other user's benefit. 

### Agile
A Github board (project) was used for the agile aspect of this project to manage my user stories. 

### Database
The models created for this project are called:
1. Post - which is the database related to the each blog post. 
2. Comment - which is the database related to the comments on each blog post. 

The following Entity Relationship Diagrams (ERD) using Microsoft Word Online were created for this project. 

![ERD](readme_images/erd.JPG)

# **User Experience**
## Wireframes
The following wireframes were created to design the layout of the pages and was created using Microsoft Paint.
![Posts](readme_images/1_posts_pages.png)
![About/Who We Are](readme_images/2_about_page.png)
![Create Post Form](readme_images/3_create_form.png)

## User Stories
The User Stories can be split into two perspectives. 
1. Site User 
2. Site Admin

To view the User Stories for this project, you can visit my GitHub board [here.](https://github.com/users/fatimamahate/projects/15)

# **Features**
## Header
The header of the page includes the name of the site which is Study Buddies. The sites name is linked to the homepage so that when users would like to go back, they simply need to click on the site name. Furthermore, the colour chosen is #4A4A4F which is dark grey. This is because it is softer than the harsh black against the background which is rgb(196, 215, 228). See image in Navigation section for the Header also. 

## Navigation
The navigation (nav bar) has the following pages. 
1. Home
2. Study Tips
3. Exam Tips
4. Who We Are
5. Search
6. Sign Up
7. Sign In

![Header](readme_images/header.JPG)

If the User is logged in, then in addition to the pages 1-5 from above, we have the following pages.
1. My Posts
2. Create
3. Sign Out

![Nav Bar](readme_images/nav_bar.JPG)

## Pages
Each navigation takes you to the following pages:
1. Home - this page shows all posts regardless of category and is paginated. This page contains all posts even if they are not of either category. For example, a user may choose to post a worksheet they made. Whilst it is studying, it is not a study tip. 

![Home](readme_images/home.JPG)

2. Study Tips - page shows all posts of the study tip category and is paginated. This page can have regular study tips.

![Study](readme_images/study.JPG)

3. Exam Tips - page shows all posts of the exam tip category and is paginated. Since exams are most likely why the user is studying, this will allow them to find all information in one page.

![Exam](readme_images/exam.JPG)

4. Who We Are - page gives a small about section along with when the last post was created to show how their can always be new ideas or tips.

![Who](readme_images/who.JPG)

5. Search - user can search for posts and retrieve a list of all posts that contain the query. It is not case sensitive.

![Search](readme_images/search.JPG)

6. Sign Up - a new user can create an account. Then when they are logged in, there is a constant message to say hello, username. This shows they are logged in. As can be seen in the header/navigation image above, there is a message to say hello, you are not logged in. This is to show that the site user is not logged in.

![Sign Up Page](readme_images/sign_up.JPG)

7. Sign In -  a returning user can log in. Onc logged in the user can see a message to say it is successful. When they are logged in, there is a constant message to say welcome, username. This shows they are logged in.

![Sign In](readme_images/sign_in.JPG)
![Signed In](readme_images/signed_in.JPG)

8. My Posts - user can view all published and draft posts. Published posts have a button which allow users to view their post. Draft Posts have 2 buttons - one to continue to edit the post and one to delete the post. 

![Draft Posts](readme_images/draft_my_posts.JPG)
![Pulished Posts](readme_images/published_my_posts.JPG)

9. Create - given a logged in user, they are able to fill in the form to add a post. 

![Create 1](readme_images/create_1.JPG)
![Create 2](readme_images/create_2.JPG)

10. Sign Out - when clicking on sign out, user will be asked to confirm they would like to sign out.

![Sign Out](readme_images/sign_out_page.JPG)
![Sign Out Message](readme_images/signed_out.JPG)

11. 404 Error - when a user enters the incorrect url, they will get this custome error page. 

![Error](readme_images/404_page.JPG)

12. Post submitted, deleted and updated pages - a message is seen depending on what function has occurred. These are important since a post is the main part of the website. Therefore, they are rendered in a different page. 
![Post Submitted](readme_images/post_submitted.JPG)
![Post Updated](readme_images/post_updated.JPG)
![Post Delete Message](readme_images/post_delete_message.JPG)
![Post Deleted](readme_images/post_deleted.JPG)

## Footer 
The footer has the icons which take you to the relevant social media pages. 

![footer](readme_images/footer.JPG)

## Comments
The comments can be written, edited and deleted on each page given a logged in user. Furthermore, a comment count looks at how many comments there are with the blog post. 
When editing the comment, the date and author is written in the box. Should the user wish, they can keep a log of when the edits were made. 
A message appears and is delierately different to what the editing, deleting or submitting the post- to differentiate a comment from the post. 

![Posted comment](readme_images/comment_posted.JPG)
![Delete comment](readme_images/comment_delete.JPG)
![Edit comment](readme_images/comment_update.JPG)
![Approved comment](readme_images/comment_count_and_approved_comment.JPG)
![Submitted comment message](readme_images/comment_submitted.JPG)
![Updated comment message](readme_images/comment_updated.JPG)
![Deleted comment message](readme_images/comment_deleted.JPG)


## More Features
Further to the features above, there are some features which would be beneficial to implement. These are listed below:

1. Search bar in nav bar instead of in a new page
  - Search to also reveal a cards of blog posts instead of a list of pages however this was decided against. This is because if there are many posts that fit the query, it would be easier for the user to scan through the list to find the post they are looking for instead of going through each page. 
  - Whilst a search in or near the nav bar would be better in this instance, a seperate page would allow for added filters and queries to refine searches which is another feature yet to be implemented.
2. Automated Testing
3. Approval for edited posts
  - Currently, as the admin has rights of approving they have already seen and trusted the user, therefore are trusted to edit their page correctly. It would be better and more efficient if the post will be sent for approval.
4. Currently, the email is optional. However, in the future it would be good to make it compulsory so that the email can be used for sending out newsletters regarding Study Buddies.

# **Technologies Used** 
The following technologies were used:

- [Python](https://www.python.org/)
- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Microsoft Paint](https://www.microsoft.com/en-us/windows/paint?msockid=160fadd2f2ff628f2dfebcd9f31f633f) - for wireframes
- [Microsoft Word](https://www.microsoft.com/en-us/microsoft-365/word?msockid=160fadd2f2ff628f2dfebcd9f31f633f) - for ERD
- [Cloudinary](https://cloudinary.com/) - to store user images
- [HTML Validator](https://validator.w3.org/) - validate html pages
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - validate css pages

# **Tests**
## Manual Testing
Acceptance criteria of each user story is met for test to pass.
|  <u>User Stories</u> |<u>Test</u>   |
|---|---|
|  As a site user I can view all study/exam tip posts so that I can select a post to read. |  Passed  |
|  As a site user I can view a list of study tip posts so that I can select a study tip post to read. | Passed  |
|  As a site user I can view a list of exam tips posts so that I can select an exam tip post to read. | Passed  |
|  As a site user/admin I can create a draft post so that I can save my work and come back to it.  |  Passed |
| As a site user I can sign up to an account so that create, read, update and delete my posts. I can also make comments so that I am involved in the conversation.  | Passed   |
| As a site user/admin I can edit and delete my posts so that I can modify/ remove the posts I am not entirely happy with.  | Passed  |
| As a site user I can view an about page so that I can find out who started this page and what it is about. |  Passed |
| As a site user I can delete a comment so that I can delete a comment if I am not happy with it. | Passed   |
| As a site user I can view all comments on a post so that I can read the conversation users are having.  | Passed  |
| As a site user/admin I can view my posts so that so that I can find a specific post easily.  | Passed  |
| As a site user I can edit my comment so that I can fix any typos or add extra clarification on my comment.  | Passed   |
| As a site admin I can approve/disapprove comments so that I can remove any rude or illegal comments.  | Passed  |
| As a site user I can click on the social media links in the footer so that I can follow Study Buddies on social media.  | Passed  |
| As a site user/admin I can create a post so that I can share my exam/study tips.  |  Passed |
| As a site user I can comment on posts so that I can be involved in the conversation. | Passed  |
| As a site user I can search for a post so that I don't have to look through all posts.  | Passed  |
| As a site admin I can have access to an admin area so that I can view the users and posts and comments  |  Passed |

## Validation
1. HTML Testing - this recieved no errors and therefore passed testing.
![HTML Validation](readme_images/HTML_validation.JPG)
2. CSS Testing - this recieved no errors and therefore passed testing.
![CSS Validation](readme_images/CSS_validation.JPG)

# **Deployment**
Heroku was used to deploy the live project. The following steps were used to set up Heroku app. 
1. Log in to Heroku website (you may need 2 factor authentication)
2. Click on new and then create new app.
3. Type in a unique app name
4. Select the region closest to you
5. Click on create app.
6. Make sure to open the app you have just created on heroku.
7. Check your version of python and check the heroku stack is compatible
8. In the settings tab, add your config_vars (such as your databases)
9. Navigate to the deploy tab and next to deployment method, choose to connect to your github repo
10. Once connected, as long as your settings.py has DEBUG=False, you can make a manual deployment.
11. Your site is now live. 

# **Credit**
Images were all take from [Unsplash](https://unsplash.com/) and they were free to use. 

There were two default images although one was only used once for the who we are page. 

- Who We Are Page - Photo by: [Priscilla Du Preez](https://unsplash.com/photos/three-men-laughing-while-looking-in-the-laptop-inside-room-XkKCui44iM0)

- Default image as placeholder - Photo by:[Joanna Kosinska](https://unsplash.com/photos/two-gray-pencils-on-yellow-surface-1_CMoFsPfso)

- 'Tackling Your Maths Exam' Post - Photo by: [Antoine Dautry](https://unsplash.com/photos/mathematics-computation-05A-kdOH6Hw)

- 'Studying vs Social Media' Post - Photo by: [freestocks](https://unsplash.com/photos/woman-holding-red-phone-m7zKB91brGo)

# **Code**
1. [Stack Overflow](https://stackoverflow.com/questions/61657061/how-do-i-resize-the-width-of-summernote) - to resize the summernote
2. [Learn Django](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages) - to include a custom 404 error page
3. [PyTutorial](https://pytutorial.com/django-search-function/) - to include the search function
4. [Code Institute I Think Therefore I Blog Walkthrough (Current and Deprecated)](https://codeinstitute.net/) - a guide to follow for my own blog

# ** Acknowledgements**
This project would not have been completed without my mentor, Precious Ijege's support and advice. Also tutor support for their help on issues I had. 
