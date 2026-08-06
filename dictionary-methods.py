"""
recipes = [                                 #Bu Şekilde liste halinde de oluşturulabilir.
    {
    "foodName" : "Musakka",
    "recipe" : "recipe explaination",
    "picture" : "1.png"
},
    {
    "foodName" : "Musakka",
    "recipe" : "recipe explaination",
    "picture" : "1.png"
},
    {
    "foodName" : "Musakka",
    "recipe" : "recipe explaination",
    "picture" : "1.png"
}

]
"""

recipe = {
    "foodName" : "Musakka",
    "recipe" : "recipe explaination",
    "picture" : "1.png"
}

#access items
result = recipe["foodName"]         # foodName key'ine ait value döner. Mussakka
result = recipe.get("foodName")     # foodName key'ine ait value döner. Mussakka
result = recipe.keys()              # recipe içindeki bütün key'leri liste içinde döner.
result = recipe.values()            # recipe içindeki bütün value'leri liste içinde döner.
result = recipe.items()             # recipe içindeki bütün value ve key'leri liste içinde döner.

#update items
recipe["foodName"] = "Mantı"        #foodName güncellenir.
recipe["foodName2"] = "Mantı"       #foodName2 Var olmadığı için listenin sonuna yenibir eleman ekler yani ekleme de yapılabilir.

recipe.update({"foodName" : "Makarna"}) #Bu methodla da kolayca günceleme yapılabilir.
recipe.update({"foodName3" : "Makarna"}) #Bu methodla da listede bulunmadığı için ekleme yapılabilir.

#delete item
recipe.pop("foodName")               #Kolayca silme yapılır.
recipe.popitem()                     #Son eklenen elemanı siler.
recipe.clear()                       #liste içindeki bütün elemanlaarı siler.
print(result)