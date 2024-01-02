
# M.Books

## Project Goals

M.Books is a web application designed that enables its users to search for Japanese Manga comic that they would like to read.

## User Goals

- All users can find Japanese Manga comic to read.
- Registered users can recommend titles that they are familiar with.
- Registered users can add, edit and remove titles to/from the website.

## Business and Development Goals

- Earn money on each book purchased via a link from the site.

## User Stories

- All users can see Home, Sign-In and Register on the navigation bar.
- All users will see an opaque background image on every page.
- Registered/Admin users who have signed in can see Home, Profile, Add Title and Sign Out in their navigation options.
- Registered/Admin users who have signed in are greeted with a welcome message on their Profile page.
- Registered/Admin users who have signed in can view all of their added Titles and Reviews on the Profile page.
- Registered/Admin users who have signed in can toggle between Titles and Review via a toggle switch.
- All user will be able to search for Manga titles titles using the search bar on the Home page.
- Users will view a list of Manga titles in alphabetical order.
- All users who click on a title will be transported to a Summary page where they can learn more.
- The Summary page will show all users a picture of the title, the year it was published and summary of the storyline.
- All users can view the reviews of the Manga titles below the summary section.
- All users that click on the back button will be transported back to the Home page
- Registered/Admin users will access buttons to Add/Edit/Delete Titles and Reviews.
- Registered/Admin users that access the Add-Title page will need to add the Title, Year of Release, Story Summary and Upload a picture of the title to add to the database.
- Registered/Admin users that add a click the Add/Edit a Review button will generate a pop form in the centre of the page that to add/edit the review.
- Registered/Admin users that click the Delete button will generate a pop-up window asking "Are you sure you want to delete {Title Name}". The user will need to press "Yes" or "No". If the user presses "No" then the window will disappear. If the user presses "Yes" then the record will be deleted redirecting the user to the Profile page and displaying the message "Record Successfully Deleted".
- Registered/Admin users that press Sign-Out will be redirected to the Sign-In page displaying the message "Successfully Signed Out".

## Features

-	**Page Consistency**
-	Each page has the “M.Books” header in the top left corner of the page. Clicking on the text transfers the user to the top of the home page.
-	Tablet and Mobile users will view the header “M.Books” in the top left corner of the page. Clicking on the text will refresh the home page.
-	**The Navigation Bar**
-	Desktop - Positioned on the right side
-	Tablet and Mobile - A burger menu with side navigation.
-	Navigation Bar (Un-Registeted Users)
- Each page will have navbar with a Home, Sign-In, Register and Search bar.
- Navigation Bar (Registered/Admin Users)
- Each page will have a Home, Sign Out, Add-Title, Contact Us.
- **Background-Image**
  - Each page will have the same opaque background image.
- **Home Page**
		- Search bar at the top of the page that allows visitors to search for a title of interest.
		- Below the search bar is a list of titles organised alphabetically.
- **Sign In page**
  - Two text input areas at the centre of the screen with Username and Password placeholder.
  - Below is a prompt "New Here?" and a link that says "Register". The link directs the user to the Register page.
  - Below the prompt is a "Sign In" button.
- **Registration Page**
  - Two text input areas at the centre of the screen with Username and Password placeholder.
  - Below is a prompt "Already Registered?" and a link that says "Sign In". The link directs the user to the Sign In page.
  - Below the prompt is a "Register" button.
- **Profile Page**
  - A toggle switch enabling the user to switch between Titles and Reviews.
  - Below is a search bar that enables the user to search for Titles/Reviews that they have added. Alternatively the user can just scroll through the list.
  - Clicking on a title directs the user to the Summary page.
- Summary Page
  - Users can view a summary of a manga title
  - Registered users have the option to add a review.
  - Registered users have the option to edit/delete Titles and Reviews added by them.
  - Admin users can add/delete all Titles and Reviews. The can only edit their own.
- **Add Title Page**
  - There are 4 input boxes for registered users to complete
		1.	Title Name
		2.	Year of Release
		3.	Summary
		4.	Provide a picture that relates to the title.
  -	Below is a "Add Title" button

##	Future Features

- Admin users will be able to Add Genre.
- Upvoting for each title which will contribute to a top 10 titles feature.
- Users will be able to reset their password.

## Typography & Colour

- **Typography**
  - Orbitron is used for the Logo and Navigation options.
  - Ubuntu is used for everything else.

-	**Colour**
  - Black for the Navigation bar.
  -	White for the Logo and Navigation bar text.
  -	Cyan for the Text Shadow, Manga List items and Edit Buttons.
  -	Red for the Delete Button.
  -	Blue for the Write a Review Button.
  
## Wireframes

![Home Page](readme.files/Home%20Page.png)
![Register](readme.files/register.png)
![Sign In](readme.files/sign-in.png)
![Sign Out](readme.files/sign-out.png)
![Profile](readme.files/profile.png)
![Summary Page](readme.files/summary.png)
![Add Title](readme.files/add-title.png)
![Navigation](readme.files/nav.png)
![Templates](readme.files/template.png)
![Write a Review](readme.files/write_edit%20_review.png)
![Delete](readme.files/delete.png)

## Technology

- [Codeanywhere](https://app.codeanywhere.com/) to build the repository.
- [GitHub](https://github.com/Code-Institute-Org/ci-full-template) to push changes to the repository.
- [Heroku](https://id.heroku.com/login) to deploy the application.
- [W3C](https://validator.w3.org/) to validate the HTML and CSS code
- [jslint](https://www.jslint.com/) to validate JavaScript to validate the JavaScript code.
- [extendsclass](https://extendsclass.com/python-tester.html) to validate python code.
- [w3schools](https://www.w3schools.com/css/css_text_shadow.asp)
- [MDN web docs](https://developer.mozilla.org/en-US/)
- [Balsamiq](https://balsamiq.com/) for creating the wireframe
- [Font Awesome](https://fontawesome.com/v4/) for the icons
- [Google fonts](https://fonts.google.com/) to search for the right fonts for the website
- [Materialize](https://materializecss.com/)  to create forms and buttons.
- [MongoDB](https://mongodb.com) for the database.
- Chrome Developer Tools for device testing.
- Google Lighthouse to text site performance.
- [wall.alphacoders.com](https://wall.alphacoders.com/big.php?i=1342052) for the background image.

## Testing

### Code Validation

-	**HTML**

  -	title.html ![Home](readme.files/html_get-title.png)
  -	signin.html ![Signin](readme.files/html_signin.png)
  -	register.html ![Register](readme.files/html_register.png)
  -	profile.html ![Profile](readme.files/html_profile.png)
  -	add-title.html ![add-title](readme.files/html_add-title.png)
  -	summary.html ![Summary](readme.files/html_summary.png)
  
-	**CSS** ![CSS](readme.files/css.validator.png)
-	**Python** ![Python](readme.files/python.validator.png)
-	**JavaScript** ![JavaScript](readme.files/jslint.png)
-	**Home Page** ![Lighhouse get_title](readme.files/lh.get_title.png)
-	**Sign-In Page** ![Lighhouse sign_in](readme.files/lh.sign_in.png)
-	**Registration Page** ![Lighhouse register](readme.files/lh.register.png)
-	**Profile** ![Lighhouse profile](readme.files/lh.profile.png)
-	**Add-Title Page** ![Lighhouse add_title](readme.files/lh.add_title.png)
-	**Summary Page** ![Lighhouse summary](readme.files/lh.summary.png)
- [Background Bedroom Image](https://wall.alphacoders.com/big.php?i=1342052) <https://wall.alphacoders.com/big.php?i=1342052>

### Test Cases

- The users journey begins at the Home page. The navbar is at the top of the page with the logo on the left and the Home, Sign-In and Register options on the right. There is a blured image of a bedroom in the background. The "Manga List" header is just below the navbar and underneath is Search bar and a list of manga titles. ![Home page](readme.files/homepage.png)
- The search bar has an text input box  with a red "Reset" and blue "Search" button on the right.
- Entering a title into the search bar will render the list down and show the  related title. Pressing the reset button will refresh the page. ![Search](readme.files/search.png)
- Unrelated words or titles will return a message "No Results Found". ![no results](readme.files/noresult.png)
- Pressing on the Home button directs users to the Home page.
- If the user clicks on the logo the Home page is refreshed. This is the same on every page.
- The user is directed to the Summary page when a title from the list is clicked. ![Press title](readme.files/demon_title.png)
- The Summary page has a "Summary" header and below is a card that shows an image of the related title, Name of title, Year of Release, Status, Mangaka (author) and the Storyline. The image will be enlarged if the user clicks on the image. Users can get back to the home page if they press the back button located at the top left-hand side of the page. When the user scrolls further down the page they can see reviews left by registered users. ![Summary page](readme.files/testcase_2.png)
- ![Enlarged image](readme.files/enlarge_img.png)
- To register for an account users can press "Register" located on the navbar to be directed to the registration page. There are 2 input boxes for users to choose a username and a password of at least 5 characters. Below the input boxes is a green "Register" button. In the event the user wanted the Sign page, there is a prompt below the "Register" button that says "Already register Sign In" Pressing Sign In will redirect the user to the Sign In page. ![Registration page](readme.files/register_page.png)
- If the user does not enter the required amount of characters, the line will turn red. Users will need to click the "Register" button to complete their registration. ![Registration requirements](readme.files/reg_requirement.png)
- If the username exist the page will be refreshed displaying the message "Username already exists" ![existing_user](readme.files/existing_user.png)
- A successful registration will direct users to the profile page displaying the message "Registration Successful!" The profile page features a card displaying the message "'Username's Profile".![success_reg](readme.files/success_reg.png)
- The Sign In page is very similar to the Registration page. There are 2 input boxes to enter the username and password and a green button that says "Sign In". Below the button there is a prompt "New here? Register". Pressing Register directs users to the registration page. ![signin page](readme.files/signin_page.png)
- To complete a sign in users must click on the Sign In button
- Text input areas left blank will turn the area red as both areas are required for a successful sign in. ![signin_requirements](readme.files/sign_requirement.png)
- If the user does not enter the correct username or password then a message "Incorrect Username and/or Password entered" ![incorrect_user](readme.files/incorrect_user.png)
- A successful sign in will direct the user to the profile page with the message "Welcome {username}". ![profile_page](readme.files/profile_page.png)
- Once a user has signed in the navbar options will update to Home, Profile, Add Title and Sign Out in the navbar. ![reg_user_menu](readme.files/reg_user_menu.png)
- Clicking on Home still directs users to Home page.
- Clicking on a title still directs users to the summary page. Registered user will see everything a unregistered user can see.
- Below the story section registered users will see a blue button "Write a Review" of that title. ![write_rev_btn](readme.files/write_rev_btn.png)
- If the user is the creator of the entry then they will see a green "Edit" and a red "Delete" button. ![edit_del_btn](readme.files/edit_del_btn.png)
- Pressing the "Write a Review" button triggers a model with 2 input boxes, "Name Your Review" and "Write a Review". Below is a red "Cancel" button and a green "Add Review" button. ![rev_modal](readme.files/rev_modal.png)
- Both input boxes are required with a minimum of 5 charactor otherwise the review will not submit. Users press the "Add Review" button once this has been completed.
- Pressing the red cancel button refreshes the Summary Page.
- Pressing the green "Add Review" button directs users tot he Home page displaying a message "Review Successfully Added" ![rev_add_success](readme.files/rev_add_success.png)
- If the user goes back to that titles summary page they will see that their review has been added to the review section with an  "Edit" and "Delete" button . ![added_review](readme.files/added_review.png)
- If a user attempts to enter a 2nd review on the same title they will be redirected to the Home page with the message "You have already reviewed this title." ![existing_review](readme.files/existing_review.png)
- Pressing the green "Edit" button in the Summary section opens up a model that is pre populated with the titles existing data. At the bottom of the modal is a red "cancel" button that refreshes the page and a green "complete" button that submits the changes the user has made. ![edit_title](readme.files/edit_title.png)
- Once the user has pressed the "complete" button they are redirected to the Home page with a the message "Title Successfully Updated". ![update_title_mes](readme.files/update_title_mes.png)
- Pressing the red "Delete" button in the summary section opens up a modal that warns the user "{title} will be permanently deleted". At the botttom of the modal is a red "No" button and a green "Yes" ![del_title](readme.files/del_title.png)
- Pressing "No" refreshes the page.
- Pressing "Yes" redirects the user to the Home page with a message "Title Successfully Deleted". ![del_title_mess](readme.files/del_title_mess.png)
- In the review section if the user presses the green "Edit" button then a modal is opened that is prepopulated with the review data and a red "Cancel" button and a green "Complete" button. ![edit_rev](readme.files/edit_rev.png)
- The cancel button will refresh the page and the complete button will redirect the user to the Home page with the message "Review Successfully Updated" ![edit_rev_mess](readme.files/edit_rev_mess.png)
- Pressing the red "Delete" button in the Review section opens up a modal that warns the user "Review will be permanently deleted". At the botttom of the modal is a red "No" button and a green "Yes" ![del_rev](readme.files/del_rev.png)
- Pressing "No" refreshes the page.
- Pressing "Yes" redirects the user to the Home page with a message "Review Successfully Deleted". ![del_rev_mess](readme.files/del_rev_mess.png)
- Users who press the Add Title in the navbar will be directed to the Add title page. They will have to complete 6 text input areas. Name of title, Image (url), Year of release, Status, Mangaka (Author) and Story. At the bottom of the page is a green "Add Title" button and a red "Cancel" button. ![add_title_page](readme.files/add_title_page.png)
- All sections need to be completed in order to submit a new title otherwise the input area turns red. ![add_title_req](readme.files/add_title_req.png)
- If the user pressed the cancel button they are redirected to the Home page. If they press the Add Title button they are redirected to the Home page with the message "Title Successfully Added". ![add_title_mes](readme.files/add_title_mess.png)
- If a user submits a title that already existing the add title page will refresh with a message "Title alreday exists" ![exist_title_mess](readme.files/exist_title_mess.png)
- If the user presses Sign Out on the navbar they are directed to the Sign In page with the message "You have signed out" ![signout_mess](readme.files/signout_mess.png)

### Test Procedure

- Does the “M-Book” Logo refresh/direct the user back the home page?
  -	*I pressed the “M-Book” Logo and it refreshed the page. The Home page is refreshed when the “M-Book” Logo is pressed.*
  - *The user is directed to the Home page when the " M-Book" Logo” is pressed on the Home, Sign-In, Register, Profile, Summary and Add-Title pages.*
- Does the “Home” link on the navigation bar refresh/direct the user to
   the Home page?

  - *The Home page is refreshed when the “Home” link is pressed.*
  - *The user is directed to the Home page when the "Home” link is pressed on the Sign-In, Register, Profile, Summary and Add-Title pages.*

- Does the “Sign-In” link on the navigation bar refresh/direct the user to the Sign-In page?
	 - *The Sign-In page is refreshed when the “Sign-In” link is pressed.*
	 - *The user is directed to the Sign-In page when the "Sign-In” link is pressed on the Home and Register pages.*

- Does the “Register” link on the navigation bar refresh/direct the user to the Register page?
	 - *The Register page is refreshed when the “Register” link is pressed.*
	 - *The user is directed to the Register page when the "Register” link is pressed on the Home and Sign-In pages.*

#### Signed In

- Does the “Profile” link on the navigation bar refresh/direct the user to the Profile page?
	 - *The Profile page is refreshed when the “Profile” link is pressed.*
	 - *The user is directed to the Profile page when the "Profile” link is pressed on the Summary and Add-Title pages.*

- Does the “Add-Title” link on the navigation bar refresh/direct the user to the Add-Title page?
	 - *The Add-Title page is refreshed when the “Add-Title” link is pressed.*
	 - *The user is directed to the Add-Title page when the "Add-Title” link is pressed on the Summary and Profile pages.
Home Page*

- When a manga title is entered into the search bar and the search button is pressed does it render the list displaying related titles?
	 - *Demon Slayer was displayed when the word “Demon” was entered into the search bar and the search button was pressed.

- Does the reset button refresh the page when pressed?
	 - *The page is refreshed with he reset button is pressed.*
- Is the user directed to the summary page of the same title when a manga title is pressed?
  - *When the “Demon Slayer” is pressed, the Demon Slayer summary page is rendered.*

#### Sign-In Page

- When the correct username and password is entered successfully, is the profile page rendered after the Sign-In button is pressed?
	 -	*The Profile page is rendered displaying the message “Welcome {{username}}” when the correct username and password is entered after the “Sign-In button is pressed.*

- When an incorrect username and/or password is entered, is the page refreshed displaying the message “incorrect Username and/or Password entered” after the Sign-In button is pressed?
	 - *The page is refreshed displaying the message “incorrect Username and/or Password entered” after the Sign-In button is pressed when an incorrect username and/or password is entered.*

- When the requirements of the text input boxes are not met, does the line turn red displaying the message “Please match the format requested”?
	 - *The line turns red when the requirements of the text input boxes are not met, displaying the message “Please match the format requested”.*

- When the Register link at the bottom of the page is clicked, is the user directed to the Register page?
	 - The user is directed to the Register page when the Register link at the bottom of the page is pressed.

#### Register Page

- When a username and password is entered successfully, is the profile page rendered after the Register button is pressed?
	 - *The Profile page is rendered displaying the message “Registration Successful” when the correct username and password is entered after the “Register” button is pressed.*

- When an existing username is entered, is the page refreshed displaying the message “Username already exists” after the Register button is pressed?
	 - *The page is refreshed after the Register button is pressed displaying the message “Username already exists” when an existing username is entered.*

- When the requirements of the text input boxes are not met, does the line turn red displaying the message “Please match the format requested”?
	 - *The line turns red when the requirements of the text input boxes are not met, displaying the message “Please match the format requested”.*

- When the Sign-In link at the bottom of the page is clicked, is the user directed to the Sign-In page?
	 - *The user is directed to the Sign-In page when the Sign-In link at the bottom of the page is pressed.*

#### Add-Title Page

- When the requirements of the text input boxes are not met, does the line turn red displaying the message “Please match the format requested”?
	 - The line turns red when the requirements of the text input boxes are not met, displaying the message “Please match the format requested”.

- When user presses the cancel button are they directed to the Home page?
	 - *The user is directed to the Home page, when the cancel button is pressed.

- When all information is entered correctly and after the Add-Title button is pressed, is the user directed to the Home page displaying the message “Title Successfully Added”?
	 - *The user is directed to the Home page displaying the message “Title Successfully Added” when all information is entered correctly, and the Add-Title button is pressed.*

- When the user enters a title that already exists, after the Add-Title button is pressed, is the Add-Title page refreshed displaying the message “Title already exists”?
	 - *The page is refreshed after pressing Add-Title button displaying the message “Title already exists”, when the user enters a title that already exists.*

#### Summary Page (Signed Out)

- Does the Summary page provide read only access in the form of the Title image, Name of Title, Year of Release, Status, Mangaka (Author), Storyline, Review Name and Review details.
	 - *The Summary page provide read only access in the form of the Title image, Name of Title, Year of Release, Status, Mangaka (Author), Storyline, Review Name and Review details.*

#### Summary Page (Signed In)

- When the summary page is accessed, does the user have access to the Write a Review button?
	 - *The user has access to the write review button when the summary page is accessed.*

- When the Write a Review button is pressed, is the modal activated displaying a Review Name text input box, a Write a Review text input box, a red Cancel button and a green Add Review button?
	 - *The modal is activated when the Write a Review button is pressed displaying a Review Name text input box, a Write a Review text input box a red Cancel button and a green Add Review button.*

- When the Write a Review Cancel button is pressed, does it direct the user to the Home page?
	 - *The user is directed to the Home page when the Write a Review Cancel button is pressed.*

- When the user satisfies the requirements to add a review, is the user directed to the Home page displaying the message “Review Successfully Added”?
	 - *The user is directed to the Home page displaying the message "Review Successfully Added” when the requirements to add a review have been met.*

- When the requirements to add a review have not been met, does the lines turn red displaying the message “Please match the format requested”?
	 - *The line turns red displaying the message “Please match the format requested” when the requirements to add a review have not been met.*
- Does the Edit and Delete buttons display only if the user is the creator or an admin user?
	 - *If the user is the creator or an admin user the Edit and Delete buttons are displayed or else they do not.*

#### Summary Edit Title

- When the Edit button in the title section is pressed, does the modal activate displaying prepopulated manga title data with a red “Cancel” and a green “Complete” button?
	 - *The modal is activated when the Edit button is pressed displaying prepopulated manga title data with a red “Cancel” and a green “Complete” button.*

- When the cancel button is pressed does it direct the user to the Home page?
	 - *The user is directed to the Home page when the cancel button is pressed.*

- When the Complete button is pressed does it direct the user to the Home page displaying the message “Title successfully updated”.
	 - *The user is directed to the Home page displaying the message “Title successfully updated” when the complete button is pressed.*

- Are the details of the manga title updated following the changes made when the user accesses the summary page.
	 - *Changes were made on all sections of the summary page and these were successfully updated following the changes that were made.*

#### Summary Delete Title

- When the Delete button in the title section is pressed, does the modal activate displaying the message “Are you sure? {Title} will be permanently deleted with a red “No” and a green “Yes” button?
	 - *The modal is activated when pressed, displaying the message “Are you sure? {Title} will be permanently deleted with a red “No” and a green “Yes” button.*

- When the “No” button is pressed is the page refreshed?
	 - *The page is refreshed when the no button is pressed.*

- When the “Yes” button is pressed is the user directed to the Home page displaying the message “Title successfully deleted”?
	 - *The user is directed to the Home page displaying the message "Title successfully deleted” when the “Yes” button is pressed.*

- Does the title still appear within the list of manga titles on the   Home page?  
	 - *The title is no longer available within the list of manga titles on the Home page.*

#### Review Section

- Does the Edit and Delete buttons display only if the user is the  creator or an admin user?
  - The Edit and Delete buttons display only if the user is the creator or an admin user.

#### Edit Review

- When the Edit button is pressed, does the modal activate displaying prepopulated review data with a red “Cancel” and a green “Complete” button?
	 - *The modal activates when the Edit button is pressed displaying prepopulated review data with a red “Cancel” and a green “Complete” button.*

- When the “Cancel” button is pressed does it direct the user to the Home page?
	 - *The user is directed to the Home page when the cancel button is pressed.*

- When the Complete button is pressed does it direct the user to the Home page displaying the message “Review successfully updated”
	 - *The user is directed to the Home page displaying the message “Review successfully updated” when the complete button is pressed.*

- Have the details of the review been updated following the changes made when the user accesses the summary page?
	 - *Changes were made on all sections of the review, and these were successfully updated following the changes that were made.*

### Device Testing

- 1024px
![1024](readme.files/1024.png)
- 912px
![912](readme.files/912.png)
- 820px
![820](readme.files/820.png)
- 768px
![768](readme.files/768.png)
- 540px
![540](readme.files/540.png)
- 430px
![430](readme.files/430.png)
- 412px
![412](readme.files/412.png)
- 390px
![390](readme.files/390.png)
- 360px
![360](readme.files/360.png)
- 280px
![280](readme.files/280.png)

### Fixed Bugs

-	**Accessing individual Titles on the Summary page**: I  wanted  to  make  it  so when the user clicks a title, they would be transported to the summary screen with further deals of that title.
![Summary Page](readme.files/bug_1.1.png)
However,  what  displayed  was a 404 message.
![404 Message](readme.files/bug_1.2.png)
I rewatched the course content “Bind the data to the Edit_task form” and with some trial & error and the help of Jinja I was able to deduce that because href in titles.html was wrapped in a for loop I needed to change titles.id to title.id. This solved the problem.
![Issue](static/readme.files/bug_1.3.png)
![app.py file](readme.files/bug_1.4.png)
![Fix](readme.files/bug_1.5.png)
-	**Getting related reviews to show up on the Summary Page:** I wanted reviews to show up on the summary page only if they related to the book title. At first on clicking a title, all of the reviews from the reviews dictionary were being pulled, which is the opposite of what I wanted. I watched a video on [YouTube](https://youtu.be/rtYoUDEz4wo?si=yXGBtvS9Ege95-tN) that helped me understand I could make the title ObjectId part of the review data. Then I could use the ObjectId as a parameter to call all the reviews related to a specific book title.
![Summary](readme.files/bug_2.1.png)Initially, my @app.route(“/summary”) was set up to find ObjectId(titles_id), however, the  @app.route(“/add_review”) review variable was adding “title_id”: title_id.
![add_review](readme.files/bug_2.2.png) When the summary function was being called the entry couldn’t be found because it didn’t exist, therefore nothing happened. I put my frustrations to one side and focused on other parts of the application. I came back a looked at the code and saw where the error was.
![fix](readme.files/bug_2.3.png)
I changed the title_id in the review variable in the @app.route(“/summary”) function to add “title_id”: ObjectId(title_id). This immediately solved the problem.

### Browser Testing

- **Chrome** ![Chrome](readme.files/chrome.test.png)
- **Edge** ![Edge](readme.files/edge.test.png)
- **Firefox** ![Firefox](readme.files/firefox.test.png)
- **Opera** ![Opera](readme.files/opera.test.png)

## Deployment

### Codeanywhere

 1. Go to [https://app.codeanywhere.com/](https://app.codeanywhere.com/)
 2. In the Workspaces section click on “2ndborn-m-books-7m988zenj5”.
![codeanywhere workspace](readme.files/codeany_workspace.png)
 3. Once the page is loaded open a new terminal and type “python3 app.py”. Then press Enter.
![terminal](readme.files/terminal.png)
 4. Options to open the preview page or the browser will be shown. Click on the browser.
![port options](readme.files/port.png)
 5. The browser will open.
![webpage](readme.files/main_webpage.png)

### Heroku

1. Go to [Heroku.com](https://id.heroku.com/login)
![heroku_webpage](readme.files/heroku_webpage)
2. From the home page find the application "m-books" and click on it.
![heroku_homepage](readme.files/heroku_con_github)
3.	Click on the deploy tab.
![deploy_tab](readme.files/deploy_tab)
4. Scroll down to deployment method, click on GitHub, search for your repository profile, key in the name of the repository and then press search.
![heroku_con_github](readme.files/heroku_con_github)
5. Once the repository has been found click on connect. This will initially the install process.![heroku_install](readme.files/heroku_install)
6. Once installation ahve been completed, press enable automatic deploy.
![heroku_enable](readme.files/heroku_enable)
7. Press deploy.
![heroku_press_deloy](readme.files/heroku_press_deloy)
8. Finally, click on the Open App button at the top of the page.
![heroku_open_app](readme.files/heroku_open_app)
