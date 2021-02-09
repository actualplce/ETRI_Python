import os     #커스텀필드 정의하는 fields.py
from PIL import Image                      #1.파이썬의 이미지처리 라이브러리 PIL.Image임포트.
from django.db.models import ImageField   #2.이미지관련 커스텀필드는 ImageField 상속받아서 씀.
from django.db.models.fields.files import ImageFieldFile  #Imagefield는 이미지를 파일시스템에 쓰고 삭제하는 작업필요하니까,
                                                         #ImagefieldFile클래스필요하고 또,
                                                         # 두 개의 클래스를 연계시켜주는 코드도 필요하지.

#커스텀필드: 보통, 기존의 유사필드를 상속받아 작성.
class ThumbnailImageFieldFile(ImageFieldFile):  #3.썸네일이미지필드파일 클래스는 ImageFieldFile을 상속받음.(파일시스템에 직접파일쓰고지우는 작업)
    def _add_thumb(self, s):                   #4.
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in ('jpeg', 'jpg'):    #5.
            parts[-1] = 'jpg'
        return '.'.join(parts)

    @property                   #6.
    def thumb_path(self):
        return self._add_thumb(self.path)

    @property                       #7.
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True):   #8.
        super().save(name, content, save)       #9.

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height) #10.
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))    #11.
        box = (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2))  #12.
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG')    #13.

    def delete(self, save=True):                #14.
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):          #15.
    attr_class = ThumbnailImageFieldFile        #16.

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs): #17.
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)                #18.

