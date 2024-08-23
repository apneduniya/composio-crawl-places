# Crawl Places

This AI helps you to extract place details from any website made using [**composio**](https://www.composio.dev/) & [**crew AI**](https://docs.crewai.com/)! 🎉
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <span>Getting Started</span>
      <ul>
        <li><a href="#-prerequisites">Prerequisites</a></li>
        <li><a href="#-steps-to-run">Steps to Run</a></li>
      </ul>
    </li>
    <li><a href="#%EF%B8%8F-project-structure">Project Structure</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
  </ol>
</details>

## 🫳 Prerequisites
You should have

- Python 3.8 or higher
- OPENAI API KEY
- [COMPOSIO API KEY / COMPOSIO CLI](https://docs.composio.dev/patterns/howtos/get_api_key)

## 👣 Steps to Run
**Navigate to the Project Directory:**
Change to the directory where the `setup.sh`, `main.py`, `requirements.txt`, and `README.md` files are located. For example:
```shell
cd path/to/project/directory
```

### 1. Run the Setup File
Make the setup.sh Script Executable (if necessary):
On Linux or macOS, you might need to make the setup.sh script executable:
```shell
chmod +x setup.sh
```
Execute the setup.sh script to set up the environment, install dependencies, login to composio and 
add necessary tools:
```shell
./setup.sh
```
Now, Fill in the `.env` file with your secrets.

### 2. Run the python script
```shell
python3 main.py
```

## 🏛️ Project structure

```bash
├── .env.example
├── .gitignore
├── helpers.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── setup.sh
```

## 🤗 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

## 🧾 License
This project is licensed under the [MIT License](LICENSE).