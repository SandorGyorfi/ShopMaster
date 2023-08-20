# UX Planes for ShopMaster Project

The ShopMaster project aims to provide users with a seamless and efficient shopping item management experience. To ensure a user-centered design, the project follows the principles of user experience design across multiple UX planes.

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



# Website Construction Plan for ShopMaster Project

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
    - Deploy the application on a web server (e.g., Heroku, AWS, etc.).
    - Ensure the application is accessible online.


# ShopMaster Features

## Existing Features

### 1. Item Management
- Create and manage shopping items easily.
- Set due dates for items to keep track of deadlines.
- Mark items as urgent when needed for better prioritization.

### 2. Category Organization
- Organize items into categories for better organization.
- Add, edit, and delete categories as needed.

### 3. User Profile
- Customize your profile with a unique username.
- Update your email address for communication.

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




# Technologies Used

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
- **FontAwesome:** An icon library used for adding icons to the user interface.
- **Google Fonts:** Used for adding visually appealing fonts to the web pages.

## Future Technology Considerations

As the ShopMaster project evolves, there are several technologies that could be considered for future enhancements:

- **Mobile App Development:** Exploring frameworks like React Native or Flutter for creating a mobile app.
- **AI Integration:** Implementing machine learning libraries for providing personalized item recommendations.
- **Voice Recognition:** Adding voice command features using libraries like Web Speech API.
- **Analytics Tools:** Integrating analytics tools to gather insights into user behavior and preferences.

The selection of these technologies contributes to the project's user experience, performance, and scalability.


# Resources

The development of ShopMaster was made possible with the help of various online resources and platforms. The following resources were instrumental in learning and implementing different aspects of the project:

- **[Code Institute](https://codeinstitute.net/):** Online coding bootcamp that provided valuable tutorials and learning materials for web development.
- **[Google](https://www.google.com/):** Used extensively for searching and finding solutions to various coding challenges and questions.
- **[YouTube](https://www.youtube.com/):** Various coding tutorials, walkthroughs, and explanations from the developer community.
- **[freeCodeCamp](https://www.freecodecamp.org/):** Platform offering free coding courses and resources for learning web development.

These resources played a crucial role in building and enhancing the ShopMaster project. They provided insights, guidance, and solutions that contributed to the development process and the final product.

A special thanks to all the creators, instructors, and contributors who share their knowledge and expertise through these platforms.
