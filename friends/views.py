from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Friend, FriendshipRequest


User = get_user_model()


@login_required
def add_friend_view(request, to_username):
    if request.method == "POST":
        to_user = User.objects.get(username=to_username)
        from_user = request.user
        Friend.objects.add_friend(from_user=from_user, to_user=to_user)

    return JsonResponse({"added": "add"})


@login_required
def accept_request_view(request, friendship_request_id):
    if request.method == "POST":
        user = request.user
        friendship_request = get_object_or_404(
            FriendshipRequest, id=friendship_request_id, to_user=user
        )
        friendship_request.accept()

    return JsonResponse({"status": "accepted"})


@login_required
def reject_request_view(request, friendship_request_id):
    if request.method == "POST":
        user = request.user
        friendship_request = get_object_or_404(
            FriendshipRequest, id=friendship_request_id, to_user=user
        )
        friendship_request.reject()

    return HttpResponse("rejected")


@login_required
def remove_friend_view(request, to_username):
    if request.method == "POST":
        to_user = User.objects.get(username=to_username)
        from_user = request.user
        Friend.objects.remove_friend(from_user=from_user, to_user=to_user)

    return HttpResponse("removed")


@login_required
def unaccepted_requests_view(request):
    user = request.user
    requests = Friend.objects.unaccepted_requests(user=user)

    return render(
        request,
        "friends/unaccepted_requests.html",
        {"user": user, "requests": requests},
    )


@login_required
def rejected_requests_view(request):
    user = request.user
    requests = Friend.objects.rejected_requests(user=user)

    return render(
        request, "friends/rejected_requests.html", {"user": user, "requests": requests}
    )


@login_required
def friend_list_view(request):
    user = request.user
    friends = Friend.objects.friends(user=user)

    return render(
        request, "friends/friend_list.html", {"user": user, "friends": friends}
    )


@login_required
def search_friend_view(request):
    friends = []
    user = request.user

    if request.method == "GET":
        query = request.GET.get("query")
        if query:
            friends = Friend.objects.friends(user=user).filter(
                from_user__username__icontains=query
            )

    return render(
        request, "friends/friend_list.html", {"user": user, "friends": friends}
    )
