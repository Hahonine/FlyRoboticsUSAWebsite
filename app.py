from flask import Flask, render_template, request, redirect
# from static.python.passHandle import passcheck, passencrypt
# from static.python.db import makeUserTable
from static.python.utility import getActive
import static.python.utility as util
import os

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)

active_item = "sidebar-menu__item-active"
inactive_item = "sidebar-menu__item"

# @app.before_request
# def before_request():
#     if not request.is_secure:
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)


@app.route('/')
def index():
    title = "Hahonine.com your resource for most things odd"
    menu_list = getActive(util.navbar_list,1,inactive_item, active_item)
    return render_template('index.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Contact_Us/')
def contact():
    title = "Meet our team"
    menu_list = getActive(util.navbar_list,6,inactive_item, active_item)
    return render_template('contact.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Contact/Luke/')
def contactluke():
    title = "Founder and Insane-In-Chief Luke"
    menu_list = getActive(util.navbar_list,6,inactive_item, active_item)
    return render_template('lukeresume.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/DnD/')
def dndeeznutz():
    title = "Beware of Mimics!"
    menu_list = getActive(util.navbar_list,2,inactive_item, active_item)
    return render_template('dungeons.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Economics/')
def economy():
    title = "Learn how to money here"
    menu_list = getActive(util.navbar_list,3,inactive_item, active_item)
    return render_template('econ.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Login/', methods=["POST", "GET"])
def login():
    title = "Papers, Please!"
    menu_list = getActive(util.navbar_list,8,inactive_item, active_item)
    return render_template('login.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Register/', methods=["POST", "GET"])
def register():
    title = "I don't know you... yet!"
    menu_list = getActive(util.navbar_list,7,inactive_item, active_item)
    return render_template('index.html', active_title=title,menu_class=menu_list, menu_size=len(menu_list))
    return render_template('register.html', active_title=title, menu_class=menu_list, data = makeUserTable())


@app.route('/IRnPLC/')
def industrial():
    title = "I don't sleep... or eat..."
    menu_list = getActive(util.navbar_list,4,inactive_item, active_item)
    return render_template('index.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Analytics/')
def dataana():
    title = "The computer is smarter than I am!"
    menu_list = getActive(util.navbar_list,5,inactive_item, active_item)
    return render_template('index.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route('/Blog/')
def poems():
    title = "Musings of a Madman!"
    menu_list = getActive(util.navbar_list,9,inactive_item, active_item)
    return render_template('poetry.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))


@app.route("/Login/Processing/", methods=["POST", "GET"])
def process():
    # check DB and verify identity
    menu_list = getActive(util.navbar_list,1,inactive_item, active_item)
    if 1 == 0:
        title = "Login Failed, please retry."
        return render_template('login.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))
    title = "Welcome " + request.form['uname'] + ", Enjoy your stay!"
    return render_template('index.html', active_title=title, menu_class=menu_list, menu_size=len(menu_list))

if __name__ == "__main__":
    app.run()
