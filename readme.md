![ch](static\images\logo.png)

&nbsp; 

ShopMaster is a user-friendly web application designed to help you manage your shopping lists and items efficiently.


# Features

- Create and manage your shopping items with ease.
- Organize your items into categories for better organization.
- Set due dates and mark items as urgent when needed.
- Customize your profile and account settings.
- Admin users can manage categories.

Visit live page here: [ShopMaster](https://shopmaster-929db9c57928.herokuapp.com)

## Getting Started

1. Register an account or log in if you already have one.
2. Create new shopping items and categorize them.
3. View and manage your items in your profile.
4. Make use of the search functionality to quickly find items.
5. Customize your account settings and update your information.

Ready to get started? [Log In](https://shopmaster-929db9c57928.herokuapp.com/login) or [Register](https://shopmaster-929db9c57928.herokuapp.com/register).

&nbsp; 

![ch](static\images\mockup.png)

&nbsp; 


# UX Planes for ShopMaster Project
&nbsp; 

The ShopMaster project aims to provide users with a seamless and efficient shopping item management experience. To ensure a user-centered design, the project follows the principles of user experience design across multiple UX planes.

## Responsiveness

ShopMaster is designed to provide a seamless experience across different devices and screen sizes. The application's responsive design ensures that you can manage your shopping lists and items conveniently, whether you're using a desktop, tablet, or mobile device.

### Mobile-Friendly

The application's user interface adapts gracefully to mobile devices, allowing you to easily access and manage your shopping items on the go. Whether you're using a smartphone or tablet, ShopMaster provides an intuitive and user-friendly experience.

### Tablet and Desktop

ShopMaster's responsive layout ensures that you can efficiently interact with the application on larger screens as well. The user interface elements are optimized to make use of available screen space, making it comfortable to manage your shopping lists and items on tablets and desktops.

### Example Screenshots

Here are some example screenshots showcasing how ShopMaster looks on different devices:

#### Mobile View:
&nbsp; 
![ch](static\images\menu.png)


#### Desktop View:
&nbsp; 
![ch](static\images\desktop.png)


## Strategy Plane

### User Needs and Goals

The project identifies key user needs and goals:
- **Creating and Managing Shopping Items:** Users need a way to add, edit, and delete shopping items efficiently.
- **Organizing Items:** Users want to categorize items to stay organized.
- **Priority Setting:** Users want to set due dates and mark items as urgent.
- **Profile Customization:** Users expect the ability to customize their profiles.
- **Admin Privileges:** Admin users require the ability to manage categories.

### Business Goals

The project aligns with business goals by providing a feature-rich application that meets user needs, thereby increasing user engagement and satisfaction.

## Scope Plane

### Features and Functionality

ShopMaster offers the following features:
- Creating, editing, and deleting shopping items.
- Organizing items into categories.
- Setting due dates and marking items as urgent.
- Customizing user profiles.
- Admin users can manage categories.

## Structure Plane


### Information Architecture

The application's structure is designed for easy navigation and clear information hierarchy. Categories, items, and user profiles are organized logically.

## Skeleton Plane

### User Interface (UI) Design

The user interface is designed with a clean and intuitive layout:
- Clear labels and icons for actions.
- Consistent color scheme for visual harmony.
- Easy-to-access buttons for item management.
- Form inputs for adding and editing items.
- Dropdowns for category selection.

## Surface Plane

### Visual Design

The visual design elements enhance the overall user experience:
- Use of lime and white color scheme for a fresh and energetic vibe.
- Material Design icons for a modern and familiar appearance.
- Typography choices for legibility and readability.
- Responsive design for a seamless experience on different devices.

&nbsp; 

# Website Construction Plan for ShopMaster Project
&nbsp; 

![ch](static\images\app_map.png)

The ShopMaster project involves the construction of a web application that facilitates efficient management of shopping items. The construction plan outlines the steps and technologies involved in building the application.

## Technologies Used

The project utilizes the following technologies:

- **Front-end:**
  - HTML5: For structuring the web pages.
  - CSS3: For styling and layout design.
  - JavaScript: For interactive features and functionality.
  - Materialize CSS: A responsive front-end framework for modern and mobile-first designs.
  
- **Back-end:**
  - Python: The primary language for server-side development.
  - Flask: A lightweight and powerful web framework for building the application's backend.
  - MongoDB: A NoSQL database for storing user data, shopping items, and categories.

## Construction Steps

1. **Project Setup:**
   - Create a new Flask project.
   - Set up virtual environment and dependencies.

2. **Front-end Development:**
   - Design base templates for consistent layout.
   - Create HTML templates for different pages (home, profile, items, etc.).
   - Use Materialize CSS for styling and responsiveness.
   - Integrate JavaScript for interactive elements (form validation, dropdowns, etc.).

3. **Back-end Development:**
   - Configure Flask routes for different pages and actions.
   - Implement user authentication and sessions.
   - Set up MongoDB connection and models for user profiles, items, and categories.
   - Implement CRUD operations for items and categories.

4. **User Profile and Authentication:**
   - Allow users to register and log in.
   - Implement profile customization (username, email, etc.).
   - Define access controls for regular users and admin users.

5. **Item Management:**
   - Create forms for adding, editing, and deleting items.
   - Implement due date and urgent marking functionality.
   - Display user-specific items on the profile page.

6. **Category Management:**
   - Allow admin users to manage categories.
   - Create forms for adding, editing, and deleting categories.

7. **Search Functionality:**
   - Implement a search form for users to find specific items.
   - Integrate search functionality with MongoDB queries.

8. **Testing and Debugging:**
   - Test the application's functionality and responsiveness.
   - Debug any issues or errors in the code.

9. **Documentation:**
   - Document the project's setup, installation, and usage.
   - Provide clear instructions for running the application locally.

10. **Deployment:**
    - Deploy the application on a web server (Heroku).
    - Ensure the application is accessible online.

&nbsp; 

# ShopMaster Features

&nbsp; 

## Existing Features

### 1. Item Management
- Create and manage shopping items easily.
- Set due dates for items to keep track of deadlines.
- Mark items as urgent when needed for better prioritization.

&nbsp; 

![ch](static\images\edit.png)

### 2. Category Organization
- Organize items into categories for better organization.
- Add, edit, and delete categories as needed.

&nbsp; 

![ch](static\images\select.png)

### 3. User Profile
- Customize your profile with a unique username.
- Update your email address for communication.

&nbsp; 

![ch](static\images\action.png)

&nbsp; 

### 4. User Authentication
- Register an account with a username and password.
- Log in securely to access personalized features.
- Maintain user sessions for seamless navigation.

### 5. Admin Functionality
- Admin users can manage categories for better data organization.

## Planned Features

### 1. User Preferences
- Allow users to set default categories for new items.
- Enable theme customization for personalization.

### 2. Notifications
- Send reminders for approaching due dates or urgent items.

### 3. Shopping Lists
- Create multiple shopping lists for different purposes.

### 4. Item Sharing
- Share shopping lists or specific items with other users.

### 5. Item History
- Maintain a history of completed items for reference.

### 6. Mobile App
- Develop a mobile app for on-the-go item management.

## Future Enhancements

### 1. Data Insights
- Provide visualizations and insights into shopping patterns.

### 2. AI Recommendations
- Suggest items based on user preferences and history.

### 3. Collaborative Lists
- Enable collaborative shopping lists among friends and family.

### 4. Integration with E-commerce
- Integrate with e-commerce platforms for easy item import.

### 5. Voice Commands
- Implement voice commands for hands-free item management.

&nbsp; 

# Technologies Used

&nbsp; 

The ShopMaster project utilizes a variety of technologies to create a seamless and user-friendly shopping item management platform.

## Front-End Technologies

- **HTML5:** Used for structuring the web pages and user interfaces.
- **CSS3:** Used for styling the web pages and creating an appealing design.
- **JavaScript:** Used for adding interactivity and dynamic behavior to the website.
- **Materialize CSS:** A modern responsive CSS framework that provides pre-styled components and responsive design.
- **jQuery:** Used for simplified DOM manipulation and event handling.

## Back-End Technologies

- **Python:** The main programming language used for server-side logic and backend development.
- **Flask:** A lightweight web framework for building web applications in Python.
- **Jinja2:** A template engine for rendering dynamic content on the web pages.
- **MongoDB:** A NoSQL database used for storing user profiles, items, and categories.
- **PyMongo:** A Python library for interfacing with the MongoDB database.
- **WTForms:** A library used for creating and validating forms in Flask applications.
- **Passlib:** Used for password hashing and encryption.
- **Heroku:** A cloud platform used for hosting and deploying the application.

## Additional Tools and Services

- **Git:** Used for version control and collaboration among developers.
- **GitHub:** A platform for hosting and sharing the project's source code.
- **Visual Studio Code:** A popular code editor used for development.
- **Axios:** A JavaScript library used for making HTTP requests from the frontend.
- **Google Fonts:** Used for adding visually appealing fonts to the web pages.

## Future Technology Considerations

As the ShopMaster project evolves, there are several technologies that could be considered for future enhancements:

- **Mobile App Development:** Exploring frameworks like React Native or Flutter for creating a mobile app.
- **AI Integration:** Implementing machine learning libraries for providing personalized item recommendations.
- **Voice Recognition:** Adding voice command features using libraries like Web Speech API.
- **Analytics Tools:** Integrating analytics tools to gather insights into user behavior and preferences.

The selection of these technologies contributes to the project's user experience, performance, and scalability.

## Testing Analysis and Results

In this section, I provide a detailed analysis of the testing process for the "ShopMaster" application. The application was tested using the Pytest framework, allowing for efficient and comprehensive testing of its various components and functionalities.

### Testing Approach

The testing approach for the "ShopMaster" application involved creating unit tests using the Pytest framework. Unit tests are designed to verify individual components or functions in isolation, ensuring their correctness. The goal was to ensure that each unit of the application functions as intended and produces the expected output.

Pytest, a widely used testing framework for Python applications, provided a straightforward way to define test cases and assertions. It automatically discovered and executed test functions, offering detailed information about test results, including successes, failures, and errors.


### Test Coverage

The application's testing efforts focused on different areas, including routing, user authentication, data manipulation, and handling various scenarios. The following test cases were created and executed:

1. **Page Not Found Test (`test_page_not_found`):**
   This test verified that accessing a non-existent page returns a 404 error page. It ensured the application correctly handled invalid URLs.

2. **Contact Developer Test (`test_contact_developer`):**
   This test simulated sending a message to the developer using the "Contact Developer" feature. It checked if the response status code was 302, indicating successful redirection after submitting the message.

3. **Delete Account Confirmation Test (`test_delete_account_confirm`):**
   This test confirmed that users could access the "Delete Account Confirmation" page and that the appropriate content was displayed. It verified the response status code as 200 and checked for the expected content.

4. **Add Item Test (`test_add_item`):**
   This test examined the functionality of the "Add Item" page, ensuring its accessibility to authenticated users and confirming the displayed content was as expected.

5. **Change Email Test (`test_change_email`):**
   Similar to the previous tests, this test focused on the "Change Email" page, verifying its accessibility and content presentation.

6. **Change Password Test (`test_change_password`):**
   This test ensured the proper functioning of the "Change Password" page for authenticated users.

7. **Handle Profile Action Test (`test_handle_profile_action`):**
   This test explored the behavior of profile action handling, such as changing the password. It verified correct redirection and content display.

8. **CRUD Tests (`test_crud`):**
   The CRUD tests covered the Create, Read, Update, and Delete operations. These tests assessed the application's ability to perform essential database operations, such as adding, retrieving, modifying, and deleting items. All CRUD tests passed successfully, confirming the application's data manipulation functionalities.

### Testing Results

During testing, the application underwent rigorous examination using defined test cases. The outcome of the tests is summarized below:

- **CRUD Tests:** All CRUD tests passed successfully, indicating that the application can perform essential database operations accurately.

  &nbsp; 

![ch](static\images\crud_test.png)

&nbsp; 

- **Other Tests:** The remaining tests, including page access, user actions, and profile handling, also passed successfully, validating the application's core functionalities.

&nbsp; 

![ch](static\images\other_tests.png)

&nbsp; 

### Test Coverage and Confidence

The comprehensive testing provided a high level of confidence in the functionality and correctness of the "ShopMaster" application. Key features, user authentication, and various user interactions were thoroughly tested across different scenarios. The successful test execution ensures the application operates as intended, delivering a seamless and error-free user experience.

The test coverage is robust, encompassing critical components. However, continuous testing and the addition of more test cases, particularly for edge cases and uncommon scenarios, could further enhance the application's resilience.

&nbsp; 

# Project Barriers & Solutions

&nbsp; 

During the development and testing of ShopMaster, several challenges and barriers were encountered. This section outlines some of the key barriers that were identified and the solutions that were implemented to overcome them.

## Barriers and Solutions

### Barrier: Typos and Text Errors
Typos and text errors in the application's user interface and content were affecting the user experience.

**Solution:** A comprehensive review of the application's content was conducted, including menus, messages, and labels. Automated tests were set up to detect typos and errors in UI elements. Additionally, all user-facing content was stored in language files for easier editing and localization.

### Barrier: Pagination and Data Presentation
The pagination and presentation of large datasets were challenging to implement effectively.

**Solution:** A custom pagination mechanism was developed that allows users to navigate through large data sets with ease. Automated tests were established to verify the accuracy of pagination, ensuring that the correct number of items was displayed per page.

### Barrier: Object IDs and Data Integrity
Managing object IDs and ensuring data integrity in database operations was critical.

**Solution:** Object IDs were generated using MongoDB's ObjectId mechanism to ensure uniqueness and consistency. Tests were created to validate the correct generation and handling of object IDs during data operations.

### Barrier: Long Text Display
Displaying long text entries in a readable format without overflowing UI components was problematic.

**Solution:** The `textwrap` Python library was utilized to intelligently wrap and format long text entries in UI components. Tests were written to ensure that the text wrapping functionality worked as expected.

## Test-Driven Development

Throughout the development process, test-driven development (TDD) principles were followed. This approach helped identify issues early and facilitated a proactive approach to addressing barriers.

## Continuous Improvement

The testing process for ShopMaster is an ongoing effort. As new barriers are identified and resolved, the testing strategy is continuously refined to ensure the application's quality, reliability, and user satisfaction.

&nbsp; 

# Deployment and Version Control

&nbsp; 

## Deployment

ShopMaster is a web application built to streamline online shopping experiences. The deployment process involves making the application accessible to users on the internet.

### Hosting Platform

ShopMaster is hosted on [Heroku](https://www.heroku.com/), a cloud platform that provides easy deployment, scaling, and management of web applications. The deployment process is automated through Heroku's integration with this GitHub repository.

## Version Control

Version control is an essential aspect of the development process for ShopMaster. It enables effective collaboration, code organization, and the ability to track changes and roll back if needed.

### Git and GitHub

Git is a distributed version control system that allows multiple developers to work on the same project simultaneously. GitHub is a web-based platform that hosts Git repositories and provides collaboration tools.

#### Commit History

The commit history of this project on GitHub serves as a detailed log of all changes made to the codebase. Each commit is associated with a concise message describing the purpose of the change.

#### Branching Strategy

A branching strategy was adopted to manage different features, bug fixes, and development phases. The `main` branch represents the stable production-ready version of the application, while feature branches are used for developing new features or addressing specific issues. Pull requests and code reviews ensure that changes are thoroughly reviewed and tested before merging into the `main` branch.

#### Release Tagging

Release tagging is employed to mark important milestones or versions of the project. Tagged releases provide a way to easily reference specific versions for deployment or documentation purposes.

### Collaboration and Contribution

Collaborators and contributors are encouraged to fork the repository, make changes in their own branches, and submit pull requests to propose changes to the main codebase. Code reviews and discussions ensure the quality and coherence of the project.

### Continuous Integration

Continuous Integration (CI) is integrated into this project using GitHub Actions. Automated tests are run on each pull request and push to ensure that new changes do not introduce regressions or break existing functionality.

## How to Contribute

If you'd like to contribute to ShopMaster, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them with descriptive messages.
5. Push your changes to your forked repository on GitHub.
6. Create a pull request from your branch to the `main` branch of the original repository.
7. Engage in the code review process and address any feedback.

## Summary

ShopMaster's deployment on Heroku and version control through Git and GitHub have been fundamental to its development process. They have enabled smooth deployment, collaboration, code quality assurance, and continuous improvement, making it easier to manage and maintain the project over time.

&nbsp; 

# Resources

&nbsp; 

The development of ShopMaster was made possible with the help of various online resources and platforms. The following resources were instrumental in learning and implementing different aspects of the project:

- **[Code Institute](https://codeinstitute.net/):** Online coding bootcamp that provided valuable tutorials and learning materials for web development.
- **[Google](https://www.google.com/):** Used extensively for searching and finding solutions to various coding challenges and questions.
- **[YouTube](https://www.youtube.com/):** Various coding tutorials, walkthroughs, and explanations from the developer community.
- **[freeCodeCamp](https://www.freecodecamp.org/):** Platform offering free coding courses and resources for learning web development.

These resources played a crucial role in building and enhancing the ShopMaster project. They provided insights, guidance, and solutions that contributed to the development process and the final product.

A special thanks to all the creators, instructors, and contributors who share their knowledge and expertise through these platforms.

&nbsp; 

# Credits

&nbsp; 

### Code and Content

All the code and content for this application were written and developed by [Sandor Gyorfi](https://github.com/SandorGyorfi). You have poured your time and effort into building a user-friendly and efficient shopping list management tool.

### Contributions

While this application was primarily developed by [Sandor Gyorfi](https://github.com/yourusername), it's always open for contributions and improvements from the community. If you'd like to contribute, feel free to fork this repository and submit pull requests.

## Acknowledgements

I would like to express my gratitude to the following individuals and organizations who have contributed to the development of ShopMaster:

- Ben Smith, Pasquale Fasulo from City of Bristol College, for their valuable insights and feedback.
- The Code Institute, for providing a comprehensive curriculum and resources that helped shape this application.

Your support and guidance have been instrumental in the creation of this project.

### Contact

If you have any questions, suggestions, or feedback, feel free to reach out to me at [mr.sandorgyorfi@gmail.com](mailto:mr.sandorgyorfi@gmail.com).


![ch](static\images\logo.png)

