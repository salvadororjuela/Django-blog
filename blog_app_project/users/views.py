from django.shortcuts import render, redirect
# Creates forms
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup_view(request):
    # If user reaches via post
    if request.method == "POST":
        # The form obtains the user information
        form = UserCreationForm(request.POST)
        # Validation
        if form.is_valid():
            # Saves the user's information into the database
            form.save()
            # Log the user in
            #########################
            # After logging in the user is redirected to the list of articles
            # When redirecting to a html file in another app folderl use ":"
            # ("blog:index")
            return redirect("blog:index")

        # If form data is not valid, it is returned to the sign up form to
        # correct it
        else:
            return render(request, "users/signup.html", {
                "form": form
            })
    # If user reaches via get
    else:
        # Creates the form
        form = UserCreationForm()
        return render(request, "users/signup.html", {
                "form": form
            })
