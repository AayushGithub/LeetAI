# LeetAI

LeetAI is a project that aims to enhance my Leetcode solutions by combining them with AI-generated problem descriptions and explanations. With this project, I can save my Leetcode solutions along with detailed problem descriptions and explanations, all automatically generated using OpenAI's GPT-3.5 API.

## How it Works

LeetAI consists of several components working together:

1. **GPT-3.5 API**: OpenAI's GPT-3.5 API is used to generate problem descriptions and solution explanations. Given a problem's title, description, and my solution, GPT-3.5 generates a detailed explanation, providing a deep understanding of the problem and solution.

2. **GitHub Integration**: LeetAI seamlessly integrates with GitHub, allowing you to save my Leetcode solutions and their corresponding problem descriptions and explanations directly to my GitHub repository. This ensures that my solutions are well-documented and organized.

## How It Works

The LeetAI project consists of two main components:

1. `parse_solution.py`: This Python script is responsible for parsing the solution file in the specified format and extracting essential information such as the Leetcode link, question ID, question name, and the solution code itself. The solution files should be structured with specific comments to indicate these details.

2. `generate_explanation.py`: This script utilizes the OpenAI API, specifically the GPT-3.5 turbo model, to generate detailed explanations for the given Leetcode solution. It formats the problem details and the solution code into a prompt and uses the AI model to generate a markdown-formatted explanation.

## Usage

To use LeetAI, follow these steps:

1. Clone the LeetAI repository to your local machine:
```
git clone https://github.com/AayushGithub/LeetAI.git
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```
3. Sign up for an OpenAI API key and set it as an environment variable `OPENAI_API_KEY`.

4. Organize Leetcode solution files in the following format:

```python
# Link - <link to the Leetcode problem>
# Question ID - <Leetcode question ID>
# Question Name - <Leetcode question name>
# SOLUTION
```
5. Commit your Leetcode solution files to the repository in a directory titled with the Leetcode question name, in a file titled `solution.py`.
6. GitHub Actions will automatically trigger when you push a new solution. It will execute the parse_solution.py script to extract the necessary details and then invoke the generate_explanation.py script to generate an explanation using GPT-3.5. Finally, it will save the explanation as a markdown file named explanation.md in the same folder as the solution.

## Important Notes
* Ensure that you have appropriate permission to use the GPT-3.5 turbo model from OpenAI by providing a valid API key.

* LeetAI is designed to work specifically with Leetcode-style solution files. Make sure your solution files follow the specified format with comments for the Leetcode link, question ID, and question name.

## Contributions and Support

Contributions to LeetAI are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

For support or general inquiries, feel free to contact the project maintainers.

## License

This project is licensed under the [MIT License](LICENSE).
