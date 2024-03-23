from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Profil, Block, PortfolioType, Portfolio, VisitorMessage


def index(request):
    profiles = Profil.objects.all()
    my_profile = profiles[0]

    blocks = Block.objects.all()

    portf_types_list = PortfolioType.objects.all()
    portf_types = sorted(portf_types_list, key=lambda x: x.pos_index)
    portfs_list = Portfolio.objects.all()
    portfs = sorted(portfs_list, key=lambda x: x.pos_index)
    portf_dict = {}
    for p_type in portf_types:
        portf_list = []
        for portf in portfs:
            if portf.type.name == p_type.name:
                portf_list.append(portf)
        if len(portf_list) > 0:
            portf_dict[p_type.name] = list(portf_list)
            print(portf_dict)

    my_full_name = my_profile.firstname + ' ' + my_profile.surname
    return render(request, 'cv/index.html', {'my_profile': my_profile, 'my_full_name': my_full_name, 'blocks': blocks, 'portf_dict': portf_dict})


def send_message(request):
    if request.POST.get('action') == 'post':
        response_msg = 'PLease fill all the fields or check the email.'
        # _________GET INFORMATIONS______________
        name = request.POST.get('name').strip()
        mail = request.POST.get('mail').strip()
        obj = request.POST.get('object').strip()
        message = request.POST.get('message').strip()
        # ______________MANAGE EMPTY FIELD ISSUE_____________
        if name == '' or mail == '' or obj == '' or message == '' or '@gmail.com' not in mail:
            return JsonResponse({'response_msg': response_msg})
        # ___________PUT INFORMATIONS IN MODEL_____________
        try:
            message_obj = VisitorMessage(name=name, email=mail, object=obj, text=message)
            message_obj.save()
            response_msg = 'Message sent successfully.'
        except:
            pass
        response = JsonResponse({'response_msg': response_msg})
        return response


def portfolio(request, id):
    current_portfolio = get_object_or_404(Portfolio, id=id)
    wb_ad = ''
    if current_portfolio.web_address:
        _list = current_portfolio.web_address.split('/')
        wb_ad = _list[-1]
    return render(request, 'cv/portfolio.html', {'current_portfolio': current_portfolio, 'wb_ad': wb_ad})
