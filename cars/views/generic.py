from django.shortcuts import render, redirect


def generic_create(form_class, temp_name, redirect_view_name):
    def create(request):
        form = form_class()

        if request.method == "POST":
            form = form_class(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                return redirect(redirect_view_name, form.insance.pk)

        return render(request, temp_name, {"form": form})

    return create
