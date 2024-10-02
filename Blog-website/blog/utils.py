

def check_read_articles(request):
    try:
        read_articles = request.session['read_articles']
    except:
        request.session['read_articles'] = []
        read_articles = request.session.get('read_articles')
        
    return read_articles


def check_select_ratings(request):
    try:
        select_ratings = request.session['select_ratings']
    except:
        request.session['select_ratings'] = []
        select_ratings = request.session.get('select_ratings')
        
    return select_ratings

# from django.contrib.sessions.models import Session
# from django.utils import timezone

# # Hozirda amal qilayotgan sessiyalarni olish
# sessions = Session.objects.filter(expire_date__gt=timezone.now())

# for session in sessions:
#     data = session.get_decoded()  # Sessiya ma'lumotlarini dekodlash
#     print(data)  # Bu yerda sessiyadagi ma'lumotlarni ko'rishingiz mumkin
