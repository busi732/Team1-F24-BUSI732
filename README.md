# Team1-F24-BUSI732
This is a project repository for Team 1 members in BUSI 732, Fall2024

The following instructions will guide you on how to set up the project, run it in VS Code, and contribute by updating the Conda environment.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Selecting the Conda Environment in VS Code](#selecting-the-conda-environment-in-vs-code)
4. [Running the Project](#running-the-project)
5. [Contributing to the Project](#contributing-to-the-project)
6. [Project Structure](#project-structure)

---

## Getting Started

1. **Prerequisites**:
   - Make sure you have either Anaconda or Miniconda installed. If not, you can download and install Miniconda from this [link](https://docs.anaconda.com/miniconda/).
   - Ensure that **VS Code** is installed with the **Python** and **Jupyter** extensions enabled.  

2. **Clone the Repository**:
   - Open Visual Studio Code, then open the terminal by going to **View > Terminal** or pressing `Ctrl + ` ` (backtick).
   - Clone the repository by running the following commands:
     ```bash
     git clone https://github.com/busi732/Team1-F24-BUSI732.git
     cd Team1-F24-BUSI732
     ```

## Setting Up the Environment

The project uses Conda for managing dependencies. You’ll set up the environment using the `environment.yml` file, which includes all required packages.

1. **Create the Conda Environment**:
   - Run the following command in the terminal to create the environment:
     ```bash
     conda env create -f environment.yml
     ```
   - This command will create a new Conda environment called `wind_turbine_env` with the dependencies listed in `environment.yml`.

2. **Activate the Environment**:
   - After creating the environment, activate it with:
     ```bash
     conda activate 732_turbine_env
     ```

3. **Add the Environment to Jupyter**:
   - To ensure that the environment is available as a kernel in Jupyter notebooks, run:
     ```bash
     python -m ipykernel install --user --name=732_turbine_env --display-name "Python (732_turbine_env)"
     ```

## Selecting the Conda Environment in VS Code

After setting up the Conda environment, follow these steps to select it in VS Code:

1. **Open a Jupyter Notebook**:
   - In VS Code, navigate to `notebooks/mytests/check_conda.ipynb` or any other notebook in the project.

2. **Open the Kernel Selector**:
   - At the top right of the notebook, you’ll see a kernel selector (or a prompt asking you to select a kernel). Click on it to open the environment selection dropdown.

3. **Choose the Correct Environment**:
   - In the list, look for `732_turbine_env` with the specified Python version (e.g., `Python 3.8.x`). It should appear under **Conda Env**.
   - Click on `732_turbine_env` to select it as the active environment for the notebook.

4. **Verify the Selection**:
   - Once selected, you should see "732_turbine_env (Python 3.8.x)" displayed at the top of the notebook. This confirms that the notebook is using the correct Conda environment.

## Running the Project

1. **Run Cells**:
   - Run individual cells in the notebook. Verify that each cell executes successfully to confirm that your environment is set up correctly.

## Contributing to the Project

To contribute, you may need to add new packages or update existing ones in the environment. Here’s how to do it:

1. **Installing Packages**:
   - Once the environment is activated, you can install additional packages as needed using either conda or pip:
     ```bash
     conda install <package-name>
     ```
     or
     ```bash
     pip install <package_name>
     ```
     for example:
     ```bash
     conda install numpy pandas
     pip install requests
     ```
2. **Update Environment**
   - It’s a good idea to periodically run:
     ```bash
     conda update --all
     ```
     This keeps all packages up to date and avoids compatibility issues.
     
     > **Note**: Running `conda update --all` does not automatically update the `environment.yml` file. After updating packages, you need to manually update the environment file.
     
   - To update the `environment.yml` file with this change, export the current environment:
     ```bash
     conda env export --from-history > environment.yml
     ```
     > **Note**: `--from-history` includes only the packages you explicitly installed, which keeps `environment.yml` clean and avoids unnecessary dependencies.

     > ⚠️ **Important:** Please make sure the conda-forge is still under the channels section, if it is not, add it back to the first line under the channels section.
     
     > ⚠️ **Important:** Remove the last prefix line if it exists.

3. **Merging Updates**:
   - After updating `environment.yml` or pull the latest changes from the repository (including an updated `environment.yml`). you need to update the local environment to match the new configuration:
     ```bash
     conda env update --file environment.yml --prune
     ```
   This will update your environment to match the `environment.yml` file, adding or removing packages as needed.
     
   > **Note**: The `--prune` flag ensures any packages removed from the environment are also removed locally, keeping everyone’s environment consistent.

4. **Commit Your Changes**:
   - When you’ve made changes to the environment or code, commit and push them:
     ```bash
     git add .
     git commit -m "commit message"
     git push origin feature/your-branch-name
     ```
   - Consider opening a pull request (PR) for your contributions so they can be reviewed and merged.

---

## Project Structure

This project follows a standard data science directory structure to keep code and data organized:

```plaintext
Team1-F24-BUSI732/
├── data/                   # Data files
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data
│   └── external/           # External data sources
├── notebooks/              # Jupyter notebooks
│   ├── mytests/            # Test notebooks
│   └── check_conda.ipynb   # A notebook for testing Conda setup
├── src/                    # Source code scripts
├── models/                 # Serialized models and model checkpoints
├── reports/                # Generated analysis and reports
├── requirements.txt        # Dependencies for pip (optional)
├── environment.yml         # Conda environment configuration
└── README.md               # Project documentation
