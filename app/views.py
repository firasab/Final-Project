from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from . import app

from .models import (
users,
userss,
album_cur_list,
album,
message_list,
message
)
#from .models import products
from . import forms
is_user=-1

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/category_songs/<string:number>")
def category(number):
    return render_template("category_songs.html",number=number, all_videos=album_cur_list)


@app.route("/admin_message")
def admin_messages():
    return render_template("admin_message.html",message_list=message_list)

@app.route("/profile_page/<user_name>")
def profile_page(user_name):
    for user in users:
        if user['name'].lower() == user_name.lower():
            break
    else:
        return "User not found"
    return render_template("profile_page.html", user=user,is_user=is_user)


@app.route("/users_list")
def users_list():
    return render_template("users_list.html", all_users=userss)

@app.route("/video_list")
def video_list():
    return render_template("video_list.html", all_videos=album_cur_list)

@app.route("/Admin")
def admin():
    #form = forms.AlbumForm()
    return render_template("Admin.html")


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = users(form.username.data,form.password.data)
            user.save_user()
            return redirect('/')
        else:
            print("Form errors:", form.errors)
    return render_template("signup.html", form=form)


@app.route("/upload_video", methods=["GET", "POST"])
def upload_video():
    form = forms.AlbumForm()
    if request.method =="POST":
        if form.validate_on_submit():
            aulbm = album(form.name.data,form.source.data,form.category.data)
            aulbm.save_album()
            return redirect('/Admin')
    return render_template("upload_video.html",form=form)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    form = forms.MessageForm()
    if request.method =="POST":
        if form.validate_on_submit():
            messag= message(form.name_of_sender.data,form.subject_of_message.data,form.source_of_video.data)
            messag.save_message()
            return redirect('/')
    return render_template("contact_us.html",form=form)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = users(form.username.data,form.password.data)
            if user.check_this_user()==1:
                   is_user=1

                   return render_template("profile_page.html", user=user,is_user=is_user, all_videos=album_cur_list)
            if user.check_this_user()==2:# for admin
                 #form = forms.AlbumForm()
                 if request.method == "POST":
                        if form.validate_on_submit():
                            is_user=2
                            #return render_template("Admin.html", user=user,is_user=is_user,form=form)
                            return render_template("Admin.html", user=user,is_user=is_user)
            else:
                return redirect('/')
        else:
            print("Form errors:", form.errors)
    return render_template("signin.html", form=form)
