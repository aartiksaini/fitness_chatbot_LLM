# Fitness Chatbot

A personalized AI fitness companion providing exercise descriptions, tailored workout recommendations, and answers to your fitness-related questions.

## Introduction

The Fitness Chatbot leverages a  comprehensive exercise database and the power of large language models (LLMs) to facilitate your fitness journey. Whether you're a beginner or a seasoned athlete, this chatbot has something for you.

**Key Features**

* **Exercise Descriptions:** Get clear instructions and form tips for a wide range of exercises.
* **Workout Recommendations:** Receive personalized workout plans based on your goals (weight loss, muscle building, endurance), experience level, and equipment availability.
* **Fitness Q&A:**  Ask questions  about training principles, nutrition, or anything fitness-related and get informative responses. 

## Technologies Used

* **Python:** Core programming language.
* **Cohere:** Large language model for workout generation and understanding fitness queries.
* **Streamlit:**  Web framework for building the user interface.
* **Pandas:** Data manipulation and analysis (for managing the exercise database).
* **AWS Lightsail:** Deployment platform.


# Streamlit Deployment Link :

Streamlit link : ([http://34.200.246.244:8503](https://fitness1.streamlit.app/)/)

# Screenshot of UI

![HomepageUI](Screenshot.JPG)

## How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone (https://github.com/shubh-vedi/fitness_chatbot_LLM.git)

2.  **cd Fitness-Chatbot
    ```bash
    pip install -r requirements.txt

3. **Set Environment Variables:

*Obtain your Cohere API Key and create a .env file in the project's root directory with the following content:

**COHERE_API_KEY=YOUR_API_KEY
**Load the environment variables using a library like dotenv.

4. **Run the Streamlit App:
    ```bash
    streamlit run app.py

## Deployment on AWS Lightsail

**Prerequisites:**

* An AWS account with Lightsail access.
* Knowledge of basic Linux commands.

**Steps**

1. **Create a Lightsail Instance:**

   * Choose an appropriate Linux distribution (e.g., Ubuntu).
   * Select an instance size with sufficient resources for your app.

2. **SSH into the Instance:**

   * Connect to your instance using its public IP address.
   * Install any necessary updates (e.g., `sudo apt update && sudo apt upgrade`).

3. **Set up and Install Dependencies:**

   * Follow the same setup steps as in the "How to Run Locally" section, including:
      * Cloning your repository (`git clone [your_repo_link]`).
      * Installing dependencies (`pip install -r requirements.txt`).
      * Configuring environment variables for your Cohere API key.

4. **Run the Streamlit App:**

   * Start the app using `streamlit run app.py`.
   * **Important:** To keep the app running after you close the SSH session, use tools like `tmux` or `screen`.

5. **Configure Firewall (Optional):**

   * If needed, adjust your Lightsail firewall settings to allow incoming traffic on the port Streamlit uses (typically port 8501). Instructions for this step will depend slightly on your chosen Linux distribution.

**Example: Opening Port 8501 on Ubuntu**

* Run `sudo ufw allow 8501`

## License

[State your chosen license - MIT, Apache 2.0, etc.]

## Get Involved!

Contributions, suggestions, and feedback are welcome! Feel free to open issues or submit pull requests.


