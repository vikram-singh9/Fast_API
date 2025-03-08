

### Installation

1.  **Clone the repository (if applicable) or create a new project.**
2.  **Initialize the project using `uv`:**

    ```bash
    uv init file name
    ```

    This will create a `requirements.txt` file (or `pyproject.toml` if using a modern project structure).

3.  **Create a virtual environment:**

    ```bash
    uv venv
    ```

4.  **Activate the virtual environment:**

    ```bash
    venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS and Linux
    ```

5.  **Add FastAPI as a dependency using `uv`:**

    ```bash
    uv add fastapi
    ```

    This will install FastAPI inside your virtual environment.

### Running the Application

1.  **Navigate to the directory containing `main.py`.**
2.  **Run the application using Uv**

    ```bash
    fastapi dev main.py
    ```

    This will start the server, and you can access the API at `http://127.0.0.1:8000`.
    This will start the server, and you can access the API at `http://127.0.0.1:8000/docs`.

## API Endpoints

* **`/famous_poetries`**

    * Returns a random famous poem.
    * Method: `GET`
    * Example Response:

        ```json
        {
          "Famous Poetries ": "The woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep. - Robert Frost, 'Stopping by Woods on a Snowy Evening'"
        }
        ```

* **`/famous_quotes`**

    * Returns a random famous quote.
    * Method: `GET`
    * Example Response:

        ```json
        {
          "Famous quotes ": "The only way to do great work is to love what you do. - Steve Jobs"
        }
        ```

## Code Explanation

The `main.py` file contains the following:

* **Import Statements:**
    * `FastAPI` from `fastapi` for creating the API.
    * `random` for selecting random quotes and poems.
* **Initialization:**
    * `app = FastAPI()` creates an instance of the FastAPI application.
* **Data:**
    * `famous_poetries` and `famous_quotes` lists store the poems and quotes.
* **Endpoints:**
    * `@app.get("/famous_poetries")` and `@app.get("/famous_quotes")` define the API endpoints.
    * The functions `get_famous_poetries()` and `get_famous_quotes()` return a random poem or quote as a JSON response.

## Why `uv`?

* **Speed:** `uv` is significantly faster than `pip` for installing and managing Python dependencies.
* **Efficiency:** It optimizes the installation process, reducing the time and resources required.
* **Modern:** It's designed to work seamlessly with modern Python project structures.
* **Install UV:** pip install uv. or direct install from official uv website...


## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
