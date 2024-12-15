# Steps for Creating a Python Virtual Environment on Mac and Windows

## Steps to Create a Python Virtual Environment on Mac

### Step 1: Install Python (if not already installed)

1. Check if Python is installed:
   Open the terminal and type:

   ```bash
   python3 --version
   ```

   If Python is not installed, download and install it from the official [Python website](https://www.python.org/downloads/), or use Homebrew:

   ```bash
   brew install python
   ```

### Step 2: Install `virtualenv` (Optional)

Although Python 3 comes with `venv` by default, you can install the `virtualenv` package globally for additional features:

```bash
pip3 install virtualenv
```

### Step 3: Create a Virtual Environment

1. Navigate to your project directory using the terminal:

   ```bash
   cd /path/to/your/project
   ```
2. Create the virtual environment using `venv`:

   ```bash
   python3 -m venv venv_name
   ```

   Replace `venv_name` with the name you want to give to your virtual environment (e.g., `myenv`). This will create a directory named `venv_name` that contains the virtual environment.

### Step 4: Activate the Virtual Environment

1. To activate the virtual environment, use the following command:
   ```bash
   source venv_name/bin/activate
   ```
2. After activation, your terminal prompt will change, indicating that the virtual environment is active. You'll see something like:
   ```
   (venv_name) user@macbook:~/path/to/project$
   ```

### Step 5: Install Dependencies

Once the virtual environment is activated, you can install Python packages using `pip`:

```bash
pip install package_name
```

For example:

```bash
pip install requests
```

### Step 6: Deactivate the Virtual Environment

When you are done working in the virtual environment, deactivate it by running:

```bash
deactivate
```

This will return you to the system's global Python environment.

---

## Steps to Create a Python Virtual Environment on Windows

### Step 1: Install Python (if not already installed)

1. Check if Python is installed:
   Open the Command Prompt (`cmd`) and type:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from the official [Python website](https://www.python.org/downloads/), and make sure to check the box **Add Python to PATH** during installation.

### Step 2: Install `virtualenv` (Optional)

Although Python 3 includes `venv` by default, you can install `virtualenv` for additional functionality:

```bash
pip install virtualenv
```

### Step 3: Create a Virtual Environment

1. Open the Command Prompt and navigate to your project directory:

   ```bash
   cd C:\path\to\your\project
   ```
2. Create the virtual environment using `venv`:

   ```bash
   python -m venv venv_name
   ```

   Replace `venv_name` with the desired name for your virtual environment.

### Step 4: Activate the Virtual Environment

1. To activate the virtual environment, use the following command:
   ```bash
   venv_name\Scripts\activate
   ```
2. After activation, you should see the environment name prefixed to the prompt, indicating that the virtual environment is active:
   ```
   (venv_name) C:\path\to\project>
   ```

### Step 5: Install Dependencies

Once the virtual environment is activated, install Python packages with `pip`:

```bash
pip install package_name
```

For example:

```bash
pip install numpy
```

### Step 6: Deactivate the Virtual Environment

To deactivate the virtual environment and return to the global Python environment, simply type:

```bash
deactivate
```

## Summary of Commands

| Step                                     | Mac/Linux Command                 | Windows Command                |
| ---------------------------------------- | --------------------------------- | ------------------------------ |
| **Check Python version**           | `python3 --version`             | `python --version`           |
| **Install virtualenv (optional)**  | `pip3 install virtualenv`       | `pip install virtualenv`     |
| **Create virtual environment**     | `python3 -m venv venv_name`     | `python -m venv venv_name`   |
| **Activate virtual environment**   | `source venv_name/bin/activate` | `venv_name\Scripts\activate` |
| **Deactivate virtual environment** | `deactivate`                    | `deactivate`                 |
