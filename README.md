# **English**
## This application is a review/criticism application made using the Imdb database.

## About
It is an application where users review movies, give ratings, and comments and ratings can be given to these reviews.

### How does it work?
- User searches for a movie and enters movie details. Meanwhile, the movie is saved in the database. If the movie has been recorded before, it is called from the database. This method saves only the desired data without saving the entire IMDB database. Maybe it doesn't keep hundreds of thousands of forgotten movies in its database unnecessarily.
- The logged in user writes a review about the movie, gives a rating or gives a rating by commenting on the existing reviews and expressing their thoughts about the review.
- User can do all basic CRUD operations.

Database PostgreSQL is created with Authentication JWT. ViewSet class is used instead of GenericViews or ModelViewSet classes. With this, even though the number of codes is high, the events taking place in the background can be seen more clearly and can be controlled more. It can of course be written in a shorter way using Generic Views and ModelViewSet.

### Endpoints

| URL           | Methods           | Action  |
| ------------- |:-------------:| -----:|
| /api      | GET | Root |
| /api/movies/      | GET      |   List Movies |
| /api/movies/{imdb_id}/ | GET      |    Movie Details  |
| /api/movies/search/{movie_or_series_name}/{result_page_number}/ | GET      |    Search IMDB data (page number optional)  |
| /api/movies/{imdb_id}/reviews/ | GET      |    Movie Reviews  |
| /api/reviews/ | GET-POST      |    List and Create Review  |
| /api/reviews/{review_id}/ | GET-PUT-PATCH-DELETE      |    Review Details, Update or Delete  |
| /api/reviews/{review_id}/comments/ | GET      |    Review Comments  |
| /api/comments/ | GET-POST      |    List and Create Comments  |
| /api/comments/{comment_id} | GET-PUT-PATCH-DELETE      |    Comment Details, Update or Delete  |

### Params

| Params        | Action           | Required  |
| ------------- |:-------------:| -----:|
| page      | List Movie, Movie Reviews, List Reviews, Review Comments, List Comments | Optional |
| size      | List Movie, Movie Reviews, List Reviews, Review Comments, List Comments      |   Optional |
| type | List Movie      |    Optional (type=series, type=movie, type=game) |

### Images
**Search word = "lord of the" , page = 1**
![](https://i.imgur.com/eITjsKB.png)

**Movie Detail**
![](https://i.imgur.com/qAKgUiT.png)

**Movie Reviews page=3 size=5**
![](https://i.imgur.com/DgEz06c.png)

***JWT Access***
![](https://i.imgur.com/pCS7Cyt.png)

# **Turkish**
## Bu uygulama Imdb veritabani kullanilarak yapilmis inceleme/elestiri uygulamasidir.

## Hakkinda
Kullanicilarin filmler hakkinda incleme yaptigi, puan verdigi, bu incelemelere de yorum yapilabilen ve puan verilebilen bir uygulamadir.

### Nasil calisir?
- Kullanici bir film arar ve film detaylarina girer. Bu esnada film veritabanina kaydedilir. Eger film daha onceden kaydedilmis ise veritabanindan cagirilir. Bu yontem butun IMDB veritabanini kaydetmeden sadece istenilen verileri kaydeder. Belki de unutulmus yuzbinlerce filmi gereksiz yere veritabaninda tutmaz. 
- Giris yapmis kullanici film hakkinda inceleme yazar, puan verir ya da varolan incelemelere yorum yaparak inceleme hakkinda dusuncelerini belirterek puan verir.
- Kullanici temel CRUD islemlerinin hepsini yapabilir.

Database PostgreSQL, Authentication JWT ile olusturulmustur. GenericViews veya ModelViewSet siniflari yerine ViewSet sinifi kullanilmistir. Bununla kod sayisi fazla olsa da arka planda gerceklesen olaylar daha net gorulebilmekte ve daha fazla kontrol edilebilmektedir. Tabi ki Generic Views ve ModelViewSet kullanilarak daha kisa sekilde yazilabilir.
