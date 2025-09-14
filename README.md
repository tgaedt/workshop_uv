# Workshop

## Folder structure of the repository
The repository contains four subfolders. The four folders contain the following items 

+ `Data Management Basics` contains data, python scripts and slides as shown by Dr. Matthias Hofmann in the first part of the workshop.
+ `data` contains calorimetry data and metadata which will be used for the demonstration of the Calocem package
+ `notebooks` contains Jupyter notebooks which can be opened using Google colab (see below)
+ `scripts` contains two Python scripts which were developed for a earlier version of this workshop. They are intended for local use with local data and could be run if you have a suitable virtual environment and have cloned the repository.


## Installation
We have noticed during the workshop that in many instances an installation of any program on a managed computer is impossible. Therefore, it is mandatory to have an option to work with Python and access data without a local installation. Google colab is an attractive option in this scenario.

## Using Google Colab
If you have a google account, you will also have access to Google colab (https://colab.google/). In google's own words: "Colab is a hosted Jupyter Notebook service that requires no setup to use and provides free access to computing resources, including GPUs and TPUs. Colab is especially well suited to machine learning, data science, and education."

For the notebooks in this workshop, we provide an "open in colab" badge which you can click to directly open the notebook in your colab environment.


## uv
A consensus seems to be emerging that the program uv (https://docs.astral.sh/uv/) is becoming the de facto standard for package management (and more) in Python. If you do not need conda packages and you have the privilges to install software, we recommend to check out uv. Furthermore, we leave our brief installation instructions here for your reference. Much more detailed information is found on the uv homepage.

Furthermore, to leverage the full potential of Python for scientific computing and data analysis, we strongly recommend that you have a running Python installation and a suitable IDE on your computer. 

### install uv 
Go to uv home page and paste the correct commands into either Bash or powershell
+ For Windows `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
+ Linux `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Running the scripts
If you have cloned the github repository at https://github.com/tgaedt/workshop_uv and you have a working uv installation, you should be able to just run the scripts in the `scripts` folder by calling `uv run 1_intro_dataframes.py` (if you are inside the `scripts` folder). uv will automatically install all necessary dependencies into a local `.venv` environment. Note that the necessary dependencies are all declared in the `pyproject.toml` file in the root folder of this workshop.

## Setting up a project from scratch with uv


### Initialize workshop project via uv
Go to the root folder under which you would like to install the project folder
`uv init workshop`

### Installation of packages
Install packages via `uv add`
`uv add pandas`
`uv add calocem`
`uv add pathlib`


# IDEs
To work with Python you only need a text editor and a Python installation. 
However, if you work with Python, an integrated development environment (IDE) is a very useful tool. One important example which is not available in text editors is debugger. Notable IDEs for use with Python are PyCharm, VS Code, or Spyder (see below). 

## Installation of Spyder (IDE)
Spyder (https://www.spyder-ide.org/) is an IDE optimized for Python and scientific computation. It is inspired by matlab and comes with an open source license. Furthermore, we consider it to be beginner friendly. 

Spyder will be installed via uv 
`uv tool install spyder`

Spyder can then be started using the command `uvx spyder`


Also initialize a spyder project. Go to "Projects" - "New Project" and chose "existing folder" and point to the folder with the uv project structure.
To activate the project view, go to "View" - "Panes" - "Project".