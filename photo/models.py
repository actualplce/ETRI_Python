from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField
#1.썸네일이미지필드: 사진원본과 썸네일 모두 저장하는필드.(커스텀필드,fields.py에있오.)


class Album(models.Model):    #album칼럼(앨범엔터티)
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):   #2,8.url반환.'/photo/album/99/'형식의 url반환할거야.
        return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):          #3.photo칼럼(데이터테이블, 포토엔터티)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  #reference.앨범엔터티에서 fk로받아온다.*cascade:같이삭제됨.
    title = models.CharField('TITLE', max_length=30)            #문자열(CharField) 타입이다.
    description = models.TextField('Photo Description', blank=True)  #4.설명(TextField)타입이다.여러줄입력. 내용이 없어도(blank)여도된다. (null허용)
    image = ThumbnailImageField('IMAGE', upload_to='photo/%Y/%m')    #5.썸네일이미지필드 타입.(이미지원본,썸네일 저장), upload_to옵션으로 저장할위치 지정.
                        #'photo/%Y/%m': MEDIA_ROOT로 정의된 디렉토리 하위에 이걸포함해서 디렉토리(폴더)만들고 사진들저장.
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True)  #6.DateTimeField 타입. 객체생성시시각 자동기록위해 오토나우.

    class Meta:     #7.메타 클래스: 객체리스트를 출력할때의 정렬기준 정의(order by?)
        ordering = ('title',)   #title칼럼(엔터티)를 기준으로 오름차순 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self):  #2,8.url반환.'/photo/album/99/'형식의 url반환할거야.
        return reverse('photo:photo_detail', args=(self.id,))

