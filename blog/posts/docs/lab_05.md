#zadanie 4
4.1 /api/posts/ i dodanie 2 obiektow posts
tu dodane:
 {
        "id": 5,
        "title": "zadanie4",
        "text": "dodanie obiektu post",
        "slug": "obiektpostnr2",
        "topic": 2,
        "topic_name": "Grzyby",
        "category_name": "Nieciekawe",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-11-09T12:43:50.306084Z",
        "updated_at": "2025-11-09T12:43:50.306094Z"
    },
    {
        "id": 4,
        "title": "test",
        "text": "test",
        "slug": "test",
        "topic": 1,
        "topic_name": "Kiwi - ciekawostki",
        "category_name": "Ciekawe",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-11-09T12:42:35.534598Z",
        "updated_at": "2025-11-09T12:42:35.534609Z"
    },
4.2 /api/posts/3/ zmiana title,text,slug,topic i klikniecie put
tu zmieniony
 {
        "id": 3,
        "title": "Ślimakowe wyscigi ale to zadanie 4",
        "text": "Ślimaki zdecydowały się nie organizować wyścigu bo było chłodno",
        "slug": "slimakowe-wyscigi-odwolane",
        "topic": 3,
        "topic_name": "Ślimaki",
        "category_name": "Zabawne",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-10-17T09:32:52.830784Z",
        "updated_at": "2025-11-09T12:45:18.709091Z"
    },
4.3/api/posts/2/ i klikniecie delete
4.4/api/posts/search/?title=a 
tu wynik 


GET /api/posts/search/?title=a

HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 5,
        "title": "zadanie4",
        "text": "dodanie obiektu post",
        "slug": "obiektpostnr2",
        "topic": 2,
        "topic_name": "Grzyby",
        "category_name": "Nieciekawe",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-11-09T12:43:50.306084Z",
        "updated_at": "2025-11-09T12:43:50.306094Z"
    },
    {
        "id": 3,
        "title": "Ślimakowe wyscigi ale to zadanie 4",
        "text": "Ślimaki zdecydowały się nie organizować wyścigu bo było chłodno",
        "slug": "slimakowe-wyscigi-odwolane",
        "topic": 3,
        "topic_name": "Ślimaki",
        "category_name": "Zabawne",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-10-17T09:32:52.830784Z",
        "updated_at": "2025-11-09T12:45:18.709091Z"
    },
    {
        "id": 1,
        "title": "Kiwi ptak nielot",
        "text": "kiwi to ptak nielot, wygląda zabawnie, ma skrzydła ale nie służą do latania",
        "slug": "kiwi",
        "topic": 1,
        "topic_name": "Kiwi - ciekawostki",
        "category_name": "Ciekawe",
        "created_by": 1,
        "created_by_username": "piotr",
        "created_at": "2025-10-17T08:30:50.070889Z",
        "updated_at": "2025-10-17T08:30:50.070902Z"
    }
]



