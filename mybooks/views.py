from django.http import HttpResponse

def book_list(request):
    html = '<html><body><h1>Kitoblar ro`yxati</h1><ul>'
    html += f'<li><a href="/book/1/">Ikki eshik orasi</a></li>'
    html += f'<li><a href="/book/2/">Oq kema</a></li>'
    html += f'<li><a href="/book/3/">O`tkan kunlar</a></li>'
    html += '</ul></body></html>'
    return HttpResponse(html)

def book_detail_1(request):
    html = f'<html><body><h1>Ikki eshik orasi</h1>'
    html += f'<p><strong>Author:</strong> O`tkir Hoshimov</p>'
    html += f'„Ikki eshik orasi“ — oʻzbek yozuvchisi Oʻtkir Hoshimov qalamiga mansub roman. Asar Oʻtkir Hoshimov merosining asosiy oʻrinlardan birini egallaydi. Asarda insonlar taqdiri va inson umrining murakkabligini mahorat bilan tasvirlangan. Adib, birinchi navbatda, tinchlikka rahna solgan urushni tilga oladi. Ayniqsa, urush voqeligining har bir ota-ona qalbini jarohatlagani, koʻngillariga ozor yetkazgani romanning umuminsoniy pafosini tashkil etadi. Adib qalamga olgan obrazlari oddiy odamlarning fazilatlari — mardligi, matonati, vatanparvarligi va sabr-bardoshi haqida soʻzlaydi. Tajribali yozuvchi roman hodisalarini teran oʻrgangani uchun har bir epizod oʻquvchini qalbiga jiddiy taʼsir qiladi. Asarda tasvirlangan hayot manzaralari, insonlararo munosabatlar shuningdek, yozuvchining oʻziga xos badiiy uslubi juda tabiiy hamda samimiyligi bilan ajralib turadi. Yetti qism, qirq yetti bobdan tarkib topgan roman kompozitsion qurilishi jihatidan ham oʻziga xosligi bilan ajralib turadi. Undagi voqea-hodisalar bayonida qatnashgan toʻqqizta personaj hikoyalarini adib bir-biriga ustalik bilan bogʻlagan.'
    html += '<br><br><a href="/">Ortga qaytish</a></br></br>'
    html += '</body></html>'
    return HttpResponse(html)

def book_detail_2(request):
    html = f'<html><body><h1>Oq kema</h1>'
    html += f'<p><strong>Author:</strong> Chingiz Aytmatov</p>'
    html += f'„Oq kema“ (ruscha: Белый пароход), „Ertakdan keyin“ deb ham ataladi — qirgʻiz yozuvchisi Chingiz Aytmatov qalamiga mansub qissa. Ilk bor 1970-yil „Noviy mir“ jurnalida chop etilgan. „Oq kema“ bir necha tilga, jumladan, oʻzbek tiliga tarjima qilingan. Qissada Issiqkoʻl boʻyida yashovchi yetti yoshli yetim bola haqida hikoya qilinadi. 1975-yil qissa asosida „Qirgʻizfilm kinostudiyasida film suratga olingan. Film SSSR davlat mukofoti bilan taqdirlangan.'
    html += '<br><br><a href="/">Ortga qaytish</a></br></br>'
    html += '</body></html>'
    return HttpResponse(html)

def book_detail_3(request):
    html = f'<html><body><h1>O`tkan Kunlar</h1>'
    html += f'<p><strong>Author:</strong> Abdulla Qodiriy</p>'
    html += f'Oʻtkan kunlar, baʼzi manbalarda Oʻtgan kunlar – oʻzbek yozuvchisi Abdulla Qodiriy qalamiga mansub oʻzbek adabiyotidagi ilk roman. 1969-yil „Oʻzbekfilm“ kinostudiyasida ushbu roman asosida „Oʻtgan kunlar“ nomli film suratga olingan. Adib romanni yozishda arab yozuvchisi Jurji Zaydon asarlaridan ilhomlangan. Roman 1920-yillar boshida yozilgan boʻlib, 1922-yil ilk bor „Inqilob“ jurnalida chop etilgan va 1926-yilda alohida kitob holida nashr etilgan.'
    html += '<br><br><a href="/">Ortga qaytish</a></br></br>'
    html += '</body></html>'
    return HttpResponse(html)