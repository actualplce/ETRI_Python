from django.contrib import admin

from photo.models import Album, Photo


class PhotoInline(admin.StackedInline): #1.album:photo=1:N관계.즉,앨범객체보여줄때 연결된 사진객체들을 함께보여줄수있단것.
                    #StackedInline: 세로로 나열되는 형식. *TabularInline: 테이블모양처럼 행으로 나열됨.
    model = Photo       #2.추가로 보여줄 테이블은 Photo테이블.
    extra = 2           #3. 이미 존재하는 객체외에 추가로 입력가능한 객체수는 2개. (즉, 총 3개보일거야.)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)        #4.앨범 객체 수정화면 보여줄때, PhotoInline에서 정의한 사항같이보여줌.
    list_display = ('id', 'name', 'description')  #id, name, description 속성을 보여줄겨(models.py)


@admin.register(Photo)              #5.Photo, PhotoAdmin클래스 등록. *admin.site.register()함수써도 되.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')  #id, title, 업로드시각 보여줄겨.(models.py)

