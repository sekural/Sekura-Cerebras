# Sekura-Cerebras

We have developed an innovative, AI-powered security vulnerability detection system that seamlessly integrates into modern development workflows. The system automatically identifies, analyzes, and provides remediation guidance for OWASP Top 10 vulnerabilities within software codebases. By leveraging large language models and advanced vector similarity search, our tool delivers real-time security insights that enable development teams to address potential security risks during the early stages of development.

## Installation

### Prerequisites

Ensure that you have Python 3.x installed and the following tools are set up:

- Git
- Python package manager `pip`

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/sekural/Sekura-Cerebras.git
    ```

2. Navigate into the project directory:

    ```bash
    cd sekura-cerebras
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Tool

1. After installation, run the tool by executing the `main_infer.py` file:

    ```bash
    python main_infer.py
    ```

## Generating Vector_DB

To leverage the vector similarity search capabilities of Sekura-Cerebras, you need to generate a database of document vectors. This is done by processing PDF files relevant to security vulnerabilities.

### Steps to Generate the Vector Database

1. **Create a folder named "data"** in the project directory:

    ```bash
    mkdir data
    ```

2. **Add PDF files** that contain relevant information (e.g., documentation, security guides, vulnerability databases) into the `data` folder.

3. **Run the vector database generation script** by executing the following command:

    ```bash
    python data_to_vecdb.py
    ```

    This will process the PDFs in the `data` folder, generate vectors for the contents, and store them in a vector database.

Once the vector database is generated, it can be used for similarity search, allowing the tool to offer targeted insights into security vulnerabilities based on the PDF content. We have currently created a vector DB with the necessary data required, so a developer can directly run main_infer.py to identify the vulnerabilities in their code.

