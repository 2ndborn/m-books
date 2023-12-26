
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
  -	Black

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
- [w3schools](https://www.w3schools.com/jsreF/prop_text_disabled.asp)
- [MDN web docs](https://developer.mozilla.org/en-US/)
- [Balsamiq](https://balsamiq.com/) for creating the wireframe
- [Font Awesome](https://fontawesome.com/v4/) for the icons
- [Google fonts](https://fonts.google.com/) to search for the right fonts for the website
- [Materialize](https://materializecss.com/)  to create forms and buttons.
- [MongoDB](https://mongodb.com) for the database.
- Chrome Developer Tools for device testing.
- Google Lighthouse to text site performance.

## Testing

### Code Validation

### Test Cases

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

## Deployment

### Codeanywhere

### Heroku
