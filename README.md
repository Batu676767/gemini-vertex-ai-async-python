
# Gemini Content Generator Asynchronous 

Gemini Content Generator is a production-ready Python application that leverages Vertex AI's Gemini model to generate content from text prompts and images. It supports both base64 encoded images and image URLs, making it flexible for various use cases such as image analysis, description generation but asynchronous.

---

## Features

- **Asynchronous Processing:** Utilizes Python's `asyncio` to generate content concurrently for multiple inputs.
- **Flexible Input Options:** Accepts text prompts, base64 encoded images, or image URLs.
- **Modular Codebase:** Organized into separate modules for configuration, core functionality, and utilities.
- **Production-Ready:** Includes logging, error handling, and a clean project structure suitable for public repositories and collaborative development.

---

## Repository Structure

```
gemini-content-generator/
├── LICENSE
├── README.md
├── .gitignore
├── requirements.txt
├── setup.py
├── data
│   └── base64.txt                # Sample file with a base64 encoded image
├── docs                          # (Optional) Documentation files
├── src
│   ├── __init__.py
│   ├── config.py                 # Configuration (e.g., Vertex AI settings)
│   ├── generator.py              # Core functions for content generation
│   ├── main.py                   # Application entry point
│   └── utils
│       ├── __init__.py
│       ├── is_image_url.py       # Utility to check if a URL is an image URL
│       └── image_url_to_base64.py# Utility to convert an image URL to base64
└── tests
    ├── __init__.py
    └── test_generator.py         # Unit tests for utilities and core logic
```

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8 or later
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/gemini-content-generator.git
   cd gemini-content-generator
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Vertex AI Credentials:**

   The project uses Vertex AI for content generation. Make sure you have the appropriate credentials set up. You can override default configurations by setting these environment variables:

   - `VERTEX_AI_PROJECT` (default: `savvy-pad-417021`)
   - `VERTEX_AI_LOCATION` (default: `europe-west4`)
   - `VERTEX_AI_MODEL` (default: `gemini-1.5-flash-002`)

   For example, on Unix-based systems you can set an environment variable like so:

   ```bash
   export VERTEX_AI_PROJECT="your-project-id"
   ```

---

## Usage

The main entry point of the application is located in `src/main.py`. It demonstrates how to generate content using both base64 encoded images and image URLs.

### Running the Application

To run the application:

```bash
python -m src.main
```

This will execute the main function, which:
- Reads a sample base64 string from `data/base64.txt`.
- Processes a couple of image URLs.
- Generates content concurrently using the Vertex AI Gemini model.
- Logs the results to the console.

---

## Testing

Unit tests are provided in the `tests` directory. To run the tests, execute:

```bash
python -m unittest discover tests
```

This will discover and run all test cases to ensure that utilities and core functions are working as expected.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

Please make sure your code adheres to the existing style and includes relevant tests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or feedback, please open an issue in the repository or contact [Your Name](mailto:your.email@example.com).

---

Happy coding!
```
