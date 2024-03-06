"""Posts views."""

#from django.shortcuts import render
from django.http import HttpResponse  

from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Betzy Castillo',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/100/100/?image=1036',
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/100/100/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/100/100/?image=1076',
    }
]

def list_posts(request):
    """List existing posts."""
    content =[]
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    
    return HttpResponse('<br>'.join(content))
