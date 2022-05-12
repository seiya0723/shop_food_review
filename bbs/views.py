from django.shortcuts import render,redirect
from django.views import View


from .models import Shop,Review
from .forms import ShopForm,ReviewForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["shops"]    = Shop.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = ShopForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)

        return redirect("bbs:index")

index   = IndexView.as_view()



#個別ページを表示させるビュー(レビューも受け付ける)
class SingleView(View):

    def get(self, request, pk, *args, **kwargs):

        #ショップの個別ページなので、Shopのidを使って1つに特定する必要が有る
        print(pk)

        context             = {}
        context["shops"]     = Shop.objects.filter(id=pk)
        context["reviews"]   = Review.objects.filter(shop=pk).order_by("-dt")

        return render(request,"bbs/single.html",context)


    #ここにレビューの投稿を
    def post(self, request, pk, *args, **kwargs):
        
        #commentが送られてくるので、pk(対象店舗のid)と組み合わせてバリデーションさせる

        #このリクエストオブジェクトはイミュータブルなオブジェクトなので、書き換えができない
        #request.POST["shop"]    = pk
        
        print(request.POST)

        copied          = request.POST.copy()
        copied["shop"]  = pk


        ip_list = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_list:
            ip  = ip_list.split(',')[0]
        else:
            ip  = request.META.get('REMOTE_ADDR')

        copied["ip"]    = ip

        print(copied)

        form    = ReviewForm(copied, request.FILES)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)

        #引数ありのURLの場合、カンマ区切りで引数を入れる
        return redirect("bbs:single",pk)

single  = SingleView.as_view()

