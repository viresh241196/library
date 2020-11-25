from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import timedelta, datetime
# Create your views here.
from account.forms import ProfileRegister, RequestBookForm
from account.models import CustomUser
from library.models import Store, Records, Profile


def home(request):
    books = Store.objects.all()
    return render(request, 'library/home.html', {'books': books})


def book_detail(request, id):
    book = Store.objects.get(id=id)
    return render(request, 'library/book_detail.html', {'book': book})


def book_request(request, id):
    if request.method == 'POST':
        name = request.POST['Name']
        email_id = request.POST['email_id']
        address = request.POST['address']
        town = request.POST['town']
        adhar_card = request.POST['adhar_card']
        book_name = request.POST['book_name']
        Copies_required = request.POST['Copies_required']
        data = Store.objects.get(book_name=book_name)
        if name == request.user.username and email_id == request.user.profile.email_id and int(
                data.Number_of_copies) >= int(Copies_required):
            data.Number_of_copies = int(data.Number_of_copies) - int(Copies_required)
            data.save()
            profile_update(data=request.user.profile, book_status=True, book_name=book_name,
                           Copies_required=Copies_required)
            record_entry(data=request.user.profile)
            messages.success(request, f'successful')
            return redirect('home')
        else:
            messages.warning(request, f'invalid details or book is not available')
            return redirect('book_request', id)
    else:
        book = Store.objects.get(id=id)
        return render(request, 'library/book_request.html', {'book': book})


def book_return(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email_id = request.POST['email_id']
        address = request.POST['address']
        town = request.POST['town']
        adhar_card = request.POST['adhar_card']
        book_name = request.POST['book_name']
        Copies_return = request.POST['Copies_return']
        if name == request.user.username and email_id == request.user.profile.email_id:
            print('working')
            if int(request.user.profile.copies_taken) == int(Copies_return):
                pass
            if int(request.user.profile.copies_taken) > int(Copies_return):
                pass

        # data = Store.objects.get(book_name=book_name)
        # if name == request.user.username and email_id == request.user.profile.email_id and int(
        #         data.Number_of_copies) >= int(Copies_return):
        #     data.Number_of_copies = int(data.Number_of_copies) - int(Copies_return)
        #     data.save()
        #     profile_update(data=request.user.profile, book_status=True, book_name=book_name,
        #                    Copies_required=Copies_required)
        #     record_entry(data=request.user.profile)
        #     messages.success(request, f'successful')
            return redirect('home')
        else:
            messages.warning(request, f'invalid details or book is not available')
            return redirect('book_return')
    else:
        if request.user.profile.book_status:
            return render(request, 'library/book_return.html')
        else:
            messages.warning(request, f'you don\'t have any book to return')
            return redirect('home')


def profile_update(data, book_status, book_name, Copies_required):
    today = datetime.today().strftime("%d-%m-%Y")
    expire_date = datetime.today() + timedelta(15)
    expire_date = expire_date.strftime("%d-%m-%Y")
    data.book_status = book_status
    data.book_name = book_name
    data.copies_taken = Copies_required
    data.borrow_date = today
    data.return_date = expire_date
    data.save()


def record_entry(data):
    entry = Records.objects.create(name=data.name, email_id=data.email_id, address=data.address,
                                   book_name=data.book_name,
                                   copies_taken=data.copies_taken, borrow_date=data.borrow_date, return_date='pending',
                                   expired_date=data.return_date)


def profile_details(request):
    pk = request.user.id
    data = Profile.objects.filter(user_info=pk).first()
    return render(request, 'library/profile_details.html', {'data': data})
