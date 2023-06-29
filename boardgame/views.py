from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "boardgames" : [
            {
                "name": "Catan",
                "complexity": 1.8,
                "played": 33,
                "players": "2-5",
            },
            {
                "name": "Monopoly",
                "complexity": 1.4,
                "played": 7,
                "players": "2-5",
            },
            {
                "name": "Cannon Fodder",
                "complexity": 3.2,
                "played": 47,
                "players": "1",
            },
        ]
    }
    return render(request, "boardgame/main.html", context)
