# Bauman
This repository contains the codes and development setup guide of the online sales and inventory system of Bauman E-bike International Inc. using Python Flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine (using Windows OS) for development and testing purposes.

### Installation

Open your command prompt and check if you have Git installed on your computer:

```shell
$ git --version
```

If the command is not recognized by the system, download and install Git through this [link](https://git-scm.com/downloads).

Once you've installed Git, follow these tutorials to setup and create Python Flask apps:

1. [How to install Python](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/installation_guide.MD)
2. [Running your first Python app](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/warm_up.MD)
3. [Setting up and creating my first Python Flask app](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/flask/discussions/2%20-%20setup%20and%20creating%20my%20first%20Flask%20app.MD)

After going through the tutorials successfully, create a new isolated development environment for this project and activate it:

```shell
$ mkvirtualenv Bauman
$ workon Bauman
```

Go to the folder where your virtual environment is located:

```shell
$ cd C:\Users\myusername\Envs\Bauman
```

Install Flask through pip:

```shell
$ pip install Flask
```

Clone this repository:

```shell
git clone https://github.com/alyssonalvaran/bauman.git
```

Move the contents of the cloned repo to the root directory of the project then delete the folder once it's empty:

1. Open the cloned repo in File Explorer (`C:\Users\myusername\Envs\Bauman\bauman`).
2. Select all the files.
3. Paste them on the parent folder or the root directory of your project (`C:\Users\myusername\Envs\Bauman\`).
4. Delete the now empty folder (`bauman`).

Go back to the command prompt and set the `FLASK_APP` and `FLASK_DEBUG` environment variables:

```shell
$ set FLASK_APP=app/app.py
$ set FLASK_DEBUG=1
```

Finally, run your application:

```shell
$ flask run
```

Enjoy!

<!-- ## Development

Once you're done with the installation, set your local machine's global Git configuration with your GitHub account username and email address:

```shell
$ git config --global user.name "myusername"
$ git config --global user.email "myemailaddress@example.com"
``` -->

<!-- ## Deployment

Coming soon! -->

## Built With

* [Python Flask](http://flask.pocoo.org/)

<!-- ### Scripts and Styles

* [jQuery 2.2.4](https://code.jquery.com/jquery/)
* [Bootstrap 3](http://getbootstrap.com/docs/3.3/)
* [Moment.js](https://momentjs.com/)
* [jQuery textarea-autosize](https://github.com/javierjulio/textarea-autosize)
* [jQuery signalR 2.2.2](https://github.com/SignalR/SignalR) -->

## Authors

* **Alysson Alvaran** - [GitHub](https://github.com/alyssonalvaran)
* **Erinel Alberto** - [GitHub](https://github.com/ealberto)
* **Rose Ann Canizo** - [GitHub](https://github.com/canizoroseann)
* **Roland Ciano, Jr.** - [GitHub](https://github.com/CianoRoland)
* **France Delos Santos** - [GitHub](https://github.com/kuysfrance)
* **Ma. Christina Olano** - [GitHub](https://github.com/olanoolano)
* **Ma. Jane Villacacan** - [GitHub](https://github.com/JaneVillacacan)
