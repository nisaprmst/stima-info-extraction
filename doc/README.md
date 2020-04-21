# Info Extraction

The title of this project is **Info Extraction**. This project was created to fulfill Strategi Algoritma course assignment.


## Modules

In this project I implemented the following modules. The modules are stored in folder src/lib

* search_keyword_bm : this module is to match a keyword string to a given list of string using Bayor-Moore algorithm
* search_keyword_kmp : this module is to match a keyword string to a given list of string using Knuth-Morris-Pratt algorithm
* search_keyword_regex : this module is to match a keyword string to a given list of string using regex algorithm


## Getting Started

Repo: https://github.com/nisaprmst/stima-info-extraction

> Getting information off the Internet is like taking a drink from a fire hydrant.
>
> **Mitchell Kapor**

### Prerequisites

* Git - Download and install git especially if you are using Windows
* Python 3 - This project was built using python3 so you need to install it to run this project
* NLTK - This is a python module to parse a text into sentences
* Flask - This is a python module that provides the user with libraries, modules and tools to help build web-based applications

### Installation

Before pulling or running the project, it is necessary to install the following:

* pip3 - https://pypi.org/project/pip/

If you are a Ubuntu user, you can complete the following steps to install pip for Python 3

1. Update your package list
```
sudo apt-get update
```
2. Use following command to install pip3
```
sudo apt-get install python3-pip
```
3. Once the installation is complete, verify the installation by checking the pip version
```
pip3 --version
```

You can install the rest of the prerequisites using pip3

## Running

### For Linux User:

1. Clone the repository using terminal

```
user@userComputer:~/dir git clone https://github.com/nisaprmst/stima-info-extraction
```

2. Open the directory where you stored the project
3. Open folder src
3. Use this command to host the project to your localhost on port 8080
```
python3 main.py
```
4. Open your browser and go to http://127.0.0.1:8080/

## Testing

For this project, I provide some sample texts to be used for testing. The texts are all stored in folder test


## Authors

* **13518085 / Annisa Ayu Pramesti** - [nisaprmst](https://github.com/nisaprmst)