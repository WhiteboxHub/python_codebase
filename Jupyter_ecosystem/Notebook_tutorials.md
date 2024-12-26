# Getting Started with Jupyter Notebook

This guide provides step-by-step instructions on how to install, create, and use Jupyter Notebook for Python development.

## Step 1: Install Jupyter Notebook

### Option 1: Install via Anaconda
Anaconda is a popular Python distribution that includes Jupyter Notebook and many other data science tools.

1. Download Anaconda: [https://www.anaconda.com/](https://www.anaconda.com/).
2. Install Anaconda by following the instructions for your operating system.
3. Open the Anaconda Navigator and launch Jupyter Notebook.

### Option 2: Install via `pip`
If you prefer a lightweight installation, you can use `pip`.

1. Open your terminal or command prompt.
2. Run the following command:
   ```bash
   pip install notebook
   ```

## Step 2: Launch Jupyter Notebook

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create your notebook.
   ```bash
   cd path/to/your/directory
   ```
3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Your default web browser will open, displaying the Jupyter Notebook interface.

## Step 3: Create a New Notebook

1. In the Jupyter Notebook interface, click on the **New** button in the top-right corner.
2. Select **Python 3** (or your desired kernel).
3. A new notebook will open in a new tab.

## Step 4: Using Jupyter Notebook

### 4.1 Adding and Running Cells

1. Write your Python code in a cell.
2. Run the cell by pressing `Shift + Enter` or clicking the **Run** button.

### 4.2 Markdown Cells

1. Change a cell to markdown by selecting **Cell Type: Markdown** from the toolbar.
2. Write formatted text using Markdown syntax (e.g., `# Heading`, `**bold**`).
3. Run the cell to render the Markdown.

### 4.3 Saving the Notebook

1. Click **File > Save and Checkpoint** or press `Ctrl + S`.
2. Your notebook will be saved with a `.ipynb` extension in the current directory.

## Step 5: Example Notebook

Below is an example workflow for your first Jupyter Notebook:

### Cell 1: Basic Python Code
```python
# Print a message
print("Hello, Jupyter Notebook!")
```

### Cell 2: Importing Libraries
```python
! pip install numpy  matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Create data
data = np.linspace(0, 10, 100)
plt.plot(data, np.sin(data))
plt.show()
```

### Cell 3: Markdown
```markdown
# My First Jupyter Notebook
This is an example of a **markdown cell**. You can use it to document your notebook.
```

## Step 6: Close the Notebook

1. Save your work.
2. Close the browser tab for the notebook.
3. Stop the notebook server in the terminal by pressing `Ctrl + C` and confirming with `y`.

## Example: 

Look at the [demo.ipynb](demo.ipynb) for the basic usecase of notebook.
   

## Additional Resources

- [Official Jupyter Documentation](https://jupyter.org/documentation)
- [Markdown Guide](https://www.markdownguide.org/)
