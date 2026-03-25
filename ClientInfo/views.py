from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


# ClientInfo/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


@login_required
def Profile_view(request):
    # ✅ try to get existing profile, or create new one
    profile_instance = Profile.objects.filter(user=request.user).first()

    form = ProfileForm(instance=profile_instance)  # pre-fill if exists

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('swipping')

    context = {
        'form': form,
        'posts': Profile.objects.all()
    }
    return render(request, 'ClientInfo.html', context)

def save_profile(request):
    if request.method == 'POST':
        # comes from your chip UI as "MOVIES,GAMING,MUSIC"
        interests_raw = request.POST.get('interests', '')
        interests_list = [i.strip() for i in interests_raw.split(',') if i.strip()]

        profile = Profile.objects.get(user=request.user)
        profile.set_interests_list(interests_list)
        profile.save()


