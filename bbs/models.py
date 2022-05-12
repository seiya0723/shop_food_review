from django.db import models
from django.utils import timezone


from django.core.validators import MinValueValidator,MaxValueValidator

class Shop(models.Model):

    name    = models.CharField(verbose_name="店名",max_length=200)
    lat     = models.DecimalField(verbose_name="緯度",max_digits=9, decimal_places=6)
    lon     = models.DecimalField(verbose_name="経度",max_digits=9, decimal_places=6)


    #レビュー数をカウントして返却
    def review_count(self):
        return Review.objects.filter(shop=self.id).count()

    #TODO:星の平均を表示させるメソッドを追加
    def avg_star_score(self):
        reviews  = Review.objects.filter(topic=self.id).aggregate(Avg("star"))

        if reviews["star__avg"]:
            return reviews["star__avg"]
        else:
            return 0


    def __str__(self):
        return self.name


class Review(models.Model):

    shop    = models.ForeignKey(Shop,verbose_name="対象店舗",on_delete=models.CASCADE)

    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    comment = models.CharField(verbose_name="コメント",max_length=1000)

    #レビューの星の数、惣菜の画像、買ったときの値段、買ったときの日付と時間帯←日時型にした方が都合がよいと思われる
    
    ip          = models.GenericIPAddressField(verbose_name="投稿した人のIPアドレス")
    approval    = models.BooleanField(verbose_name="承認済み",default=False)

    #画像の投稿機能を実装(同じファイル名がアップロードされた時、Djangoが自動的に名前を変えてくれる)
    image       = models.ImageField(verbose_name="画像",upload_to="bbs/review/image/",null=True,blank=True)

    star        = models.IntegerField(verbose_name="星の数",validators=[MinValueValidator(1),MaxValueValidator(5)])

    
    #price       = models.IntegerField(verbose_name="買ったときの価格",validators=[MinValueValidator(0)])
    #bought_dt   = models.DateTimeField(verbose_name="買ったときの日時")

