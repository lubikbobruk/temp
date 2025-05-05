# Movie Recommendation System 🎬

## Project Structure: 📁
- `backend/`: Backend directory housing server-side code written in **Python Flask**. It utilizes the **MVC architecture** and employs **SQLite3** as a testing database. This directory contains the logic for the recommendation system.
- `frontend/`: Frontend directory holding client-side code written in **ReactJS**.
- `README.md`: Markdown file providing an overview of the project.
- `SpearmanRecsysDocumentation.pdf`: PDF document containing documentation related to the Spearman Recommendation System.

## Technology Stack: 🔍
- **Backend:**
    - **Language:** Python
    - **Framework:** Flask
    - **Database:** SQLite3 for testing
    - **Architecture:** MVC (Model-View-Controller)
- **Frontend:**
    - **Language:** JavaScript
    - **Library:** ReactJS
    - **State Management:** React hooks and context
- **Algorithms:**
    - **Collaborative Filtering:** For generating recommendations based on user similarities.
    - **Spearman's Rank Correlation:** To measure the strength and direction of association between users' movie ratings.
- **Other Tools:**
    - **Testing:** Unit tests for both backend and frontend components.
    - **Build Tools:** Webpack and Babel for frontend build processes.

## What is it capable of? 🚀

### **Core Features:** ⚙️
- Implements a **Movie Recommendation System** that serves users and their movie recommendations.
- Utilizes **collaborative filtering** and **correlation-based recommendation** algorithms.

### **Overview:** 💡
The core of the Movie Recommendation System lies in the application of **collaborative filtering**, which predicts a user's interests by collecting preferences from many users. This method assumes that if two users agree on one issue, they are likely to agree on others as well.

In this application, the **collaborative filtering** method is complemented with the use of **Spearman's rank correlation coefficient** for quantifying the statistical relationships between users' movie ratings.

## Concepts 📗

### Collaborative Filtering 🪛
- **Collaborative filtering** algorithms predict a user's interests by collecting preferences from many users.
- This technique assumes that if two users agree on one issue, they are likely to agree on others as well.
- In the context of this movie recommendation system, **collaborative filtering** is used to suggest movies that similar users have liked in the past.

### Correlation-Based Recommendation 📊
- In addition to **collaborative filtering**, this project uses a **correlation-based recommendation system**.
- It employs the _Spearman's rank correlation coefficient_, a non-parametric measure of rank correlation.
- This measures the strength and direction of the association between two users' rankings of movies they have both rated.
- The correlation coefficient ranges from -1 to 1, where 1 implies a perfect increasing relationship and -1 implies a perfect decreasing relationship.
- This coefficient is used as a weight when predicting a user's rating for a movie they haven't seen yet, based on the ratings given by users with a high correlation coefficient.
