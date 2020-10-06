from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Voted


# Create your views here.
def view_poll(request):
    """
    simple function to pass the products with their respective
    nr of votes.
    """

    poll_product_list = Poll.objects.all()
    template = 'poll/poll.html'
    context = {
        'poll_product_list': poll_product_list
    }

    return render(request, template, context)


def add_vote(request, poll_product_id):
    """
    This functions adds a vote to the product that corresponds with the
    button pressed. Before adding the vote to the counter it checks
    the model 'voted' to see if the users emailadres is present.
    If not, the emailadres is added to the field and the vote is
    incremented.
    """
    product_type = get_object_or_404(Poll, pk=poll_product_id)
    current_user_email = request.user.email
    all_emails = Voted.objects.values_list('user_email', flat=True)
    redirect_url = request.POST.get('redirect_url')
    if current_user_email not in all_emails:
        product_type.votes += 1
        product_type.save()
        Voted.objects.create(user_email=current_user_email)
        vote_status = True

    else:
        vote_status = False

    print(vote_status)
    return redirect(redirect_url, vote_status)
