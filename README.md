# Workshop

## Installation

### install uv 
Go to uv home page and paste the correct commands into either Bash or powershell
+ For Windows `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
+ Linux `curl -LsSf https://astral.sh/uv/install.sh | sh`


### Initialize workshop project via uv
Go to the root folder under which you would like to install the project folder
`uv init workshop`

### Installation of packages
Install packages via `uv add`
`uv add pandas`
`uv add calocem`
`uv add pathlib`


### Installation Spyder
Spyder will be installed via uv 
`uv tool install spyder`

Also initialize a spyder project. Go to "Projects" - "New Project" and chose "existing folder" and point to the folder with the uv project structure.
To activate the project view, go to "View" - "Panes" - "Project"