# **Turkish**
## Bu uygulama Imdb veritabani kullanilarak yapilmis inceleme/elestiri uygulamasidir.

## Hakkinda
Kullanicilarin filmler hakkinda incleme yaptigi, puan verdigi, bu incelemelere de yorum yapilabilen ve puan verilebilen bir uygulamadir.

### Nasil calisir?
- Kullanici bir film arar ve film detaylarina girer. Bu esnada film veritabanina kaydedilir. Eger film daha onceden kaydedilmis ise veritabanindan cagirilir. Bu yontem butun IMDB veritabanini kaydetmeden sadece istenilen verileri kaydeder. Belki de unutulmus yuzbinlerce filmi gereksiz yere veritabaninda tutmaz. 
- Giris yapmis kullanici film hakkinda inceleme yazar, puan verir ya da varolan incelemelere yorum yaparak inceleme hakkinda dusuncelerini belirterek puan verir.
- Kullanici temel CRUD islemlerinin hepsini yapabilir.

Database PostgreSQL, Authentication JWT ile olusturulmustur. GenericViews veya ModelViewSet siniflari yerine ViewSet sinifi kullanilmistir. Bununla kod sayisi fazla olsa da arka planda gerceklesen olaylar daha net gorulebilmekte ve daha fazla kontrol edilebilmektedir. Tabi ki Generic Views ve ModelViewSet kullanilarak daha kisa sekilde yazilabilir.

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
