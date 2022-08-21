# PyScript and my journey to the Web

## Code

The `main` branch contains code that was written as part of my PyScript journey. Any code in this repo authored by me is covered by the [MIT license](https://choosealicense.com/licenses/mit/).

The repo does contain some code obtained from various open source projects (e.g., PyScript). That code is covered by the original projects' licenses.

**Direct Dependancies**
  - [PyScript](https://pyscript.net/)
  - [Pyodide](https://pyodide.org/en/stable/)
  - [Flask](https://flask.palletsprojects.com/en/2.2.x/)

### Code Layout

- `hello_world` : a very basic "Hello World" web page implemented using **PyScript**. You should be able to load this directly into your browser via `File` -> `Open` (i.e., no web server should be needed). An internet connection is required since the page will dynamically download **PyScript** and **Pyodide**. **Pyodide** in particular is quite large (253Mb as of this writing) so if you are not blessed with a fast internet connection, the page might take some time to load and render.
- `flask-hello_world` : a trivial **Flask** app used to verify that **Flask** is installed correctly.
- `server` :

### Web Server Set Up

I used Python 3.10 during development. However any modern, supported version of Python should work. _"Your milage may vary."_

#### Virtual Environment

- Create a virtual environment and install **Flask** (assumes `pip` is installed)
```sh
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- Test that the web server is installed and works on `localhost`
```sh
cd flask-hello_world
flask run --port 5050
```
- Check the [flask app](http://127.0.0.1:5050/)<br/>
![Flask Hello World](flask_hello_world.png)

## Slides

The `gh-pages` branch contains the slides for **PyScript and my journey to the Web**. The presentation contents are licensed under [CC-BY-4.0](https://choosealicense.com/licenses/cc-by-4.0/). The slides are available at [https://sjirwin.github.io/pyscript-journey/](https://sjirwin.github.io/pyscript-journey/). They are rendered using [reveal.js](https://revealjs.com) via GitHub pages.
