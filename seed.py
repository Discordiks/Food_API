from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine) #пересоздание таблиц
models.Base.metadata.create_all(bind=engine) #пересоздание таблиц

with Session(bind=engine) as session:
    #123456 и qwerty
    u1=models.User(name="Малинина", mail="recipes228@mail.ru",img_avatar="recipe/files/food.png", password="$2b$12$/2gx.pO8GYYk7yASJfH3m.rYwOgaO/GvZ6Mzvqvyq.ZdT/mnZBpRS", mailing=False, email_verify=1) #пользователи
    u2=models.User(name="Хомяк", mail="recipes223@mail.ru",img_avatar="recipe/files/food4.jpg", password="$2b$12$o3y6j3I0lS/MqDQ79AxSG.hZIBKC9JyYOUYeIaQh1lCsYeRWKzg9i", mailing=False, email_verify=1)
    u3=models.User(name="edok228", mail="admin@mail.ru",img_avatar="recipe/files/food.png", password="$2b$12$3/w7zRoYtYe4344FtJtlRuKDkfLAiZd3XqZaHaxn1zJ/DFcG/Brs6", mailing=True, email_verify=1)
    u4=models.User(name="Любимка", mail="lovelove@mail.ru",img_avatar="recipe/files/food2.jpg", password="$2b$12$3/w7zRoYtYe4344FtJtlRuKDkfLAiZd3XqZaHaxn1zJ/DFcG/Brs6", mailing=True, email_verify=1)
    u5=models.User(name="Обжоркин", mail="objorkin@mail.ru",img_avatar="recipe/files/food3.jpg", password="$2b$12$3/w7zRoYtYe4344FtJtlRuKDkfLAiZd3XqZaHaxn1zJ/DFcG/Brs6", mailing=True, email_verify=1)
    
    c1=models.Category(name="Десерт") #категории
    c2=models.Category(name="Мясо")
    c3=models.Category(name="Суп")
    c4=models.Category(name="Рыба")
    c5=models.Category(name="Напиток")
    c6=models.Category(name="Основное")

    m1=models.Mealtime(name="Завтрак") #время приёма пищи
    m2=models.Mealtime(name="Обед")
    m3=models.Mealtime(name="Ужин")

    i1=models.Ingredient(name="Пшеничная мука") #ингредиенты
    i2=models.Ingredient(name="Вода") #пицца
    i3=models.Ingredient(name="Сухие дрожжи")
    i4=models.Ingredient(name="Растительное масло")
    i5=models.Ingredient(name="Сахар")
    i6=models.Ingredient(name="Соль")
    i7=models.Ingredient(name="Помидоры")
    i8=models.Ingredient(name="Майонез") 
    i9=models.Ingredient(name="Кетчуп")
    i10=models.Ingredient(name="Чеснок")
    i11=models.Ingredient(name="Приправы")
    i12=models.Ingredient(name="Сыр Моцарелла")
    i13=models.Ingredient(name="Сырокопчёная колбаса")
    i14=models.Ingredient(name="Оливковое масло")
    i15=models.Ingredient(name="Шоколад") #клубника в шоколаде
    i16=models.Ingredient(name="Клубника")
    i17=models.Ingredient(name="Макароны") #макароны с сыром
    i18=models.Ingredient(name="Гречневая крупа") #гречка с молоком
    i19=models.Ingredient(name="Молоко")
    i20=models.Ingredient(name="Сливочное масло")
    i21=models.Ingredient(name="Малина") #чай с малиной
    i22=models.Ingredient(name="Чёрный чай")
    i23=models.Ingredient(name="Лайм")
    i24=models.Ingredient(name="Мята")
    i25=models.Ingredient(name="Сметана") #манник
    i26=models.Ingredient(name="Манка")
    i27=models.Ingredient(name="Яйцо")
    i28=models.Ingredient(name="Горошек") #добавочные
    i29=models.Ingredient(name="Огурцы")
    i30=models.Ingredient(name="Лосось")
    i31=models.Ingredient(name="Сгущёнка")
    i32=models.Ingredient(name="Зелёный чай")
    i33=models.Ingredient(name="Курица")
    i34=models.Ingredient(name="Телятина")
    i35=models.Ingredient(name="Баранина")
    i36=models.Ingredient(name="Яблоко")
    i37=models.Ingredient(name="Банан")
    i38=models.Ingredient(name="Груша")
    i39=models.Ingredient(name="Печенье")
    i40=models.Ingredient(name="Картофель")

    soc1=models.System_of_calculation(name="кг") #система исчисления
    soc2=models.System_of_calculation(name="г")
    soc3=models.System_of_calculation(name="л")
    soc4=models.System_of_calculation(name="мл")
    soc5=models.System_of_calculation(name="шт.")
    soc6=models.System_of_calculation(name="стол. л.")
    soc7=models.System_of_calculation(name="чайн. л.")

    r1=models.Recipe(name="Пицца", face_img="recipe/files/pizza.jpg", cooking_time=120, category=c6, user=u1, mealtime=[m2,m3], published=False) #рецепты
    r2=models.Recipe(name="Клубника в шоколаде", face_img="recipe/files/choko.jpg", cooking_time=30, category=c1, user=u1, mealtime=[m1],published=True) 
    r3=models.Recipe(name="Макароны с сыром", face_img="recipe/files/mak.jpg", cooking_time=20, category=c6, user=u2, mealtime=[m2,m3],published=True) 
    r4=models.Recipe(name="Гречка с молоком", face_img="recipe/files/grechka.jpg", cooking_time=60, category=c6, user=u1, mealtime=[m1,m2,m3],published=False) 
    r5=models.Recipe(name="Чай с малиной", face_img="recipe/files/chay.jpg", cooking_time=15, category=c5, user=u2, mealtime=[m1,m2,m3],published=True) 
    r6=models.Recipe(name="Манник", face_img="recipe/files/mannik.jpg", cooking_time=100, category=c1, user=u4, mealtime=[m1,m2,m3],published=True) 

    #пицца
    s1=models.Step(number=1, info="В тёплой воде, нагретой до 37-40°С, растворите сахар. А затем всыпьте дрожжи и оставьте на 15 минут до появления пышной шапочки. Если шапочки так и не появилось, то либо дрожжи испорчены, либо перегрели воду и тесто не поднимется. Нужно замешивать заново.", recipe=r1) #шаги
    s2=models.Step(number=2, info="В миску просейте муку. Всыпьте соль. Перемешайте все и сделайте в центре муки углубление. Влейте в него активированные дрожжи и оливковое масло.", recipe=r1) 
    s3=models.Step(number=3, info="Замесите упругое однородное тесто. Замешивать нужно около 7-10 минут, пока тесто не начнет отлипать от рук. При необходимости можно добавить ещё немного оливкового масла. Накройте миску полотенцем и оставьте тесто на 45 минут в тепле для подъёма.", recipe=r1)
    s4=models.Step(number=4, info="Пока поднимается тесто, приготовьте соус. В чаше блендера соедините помидоры, кетчуп, дольки чеснока, приправы и майонез. Взбейте все до однородности.", recipe=r1)
    s5=models.Step(number=5, info="В сковороде на среднем огне разогрейте растительное масло. Вылейте взбитую томатную смесь. Тушите, помешивая, около 5 минут до испарения жидкости и густоты.", recipe=r1)
    s6=models.Step(number=6, info="Готовый соус снимите с огня и охладите.", recipe=r1)
    s7=models.Step(number=7, info="Теперь приготовьте начинку. Колбасу нарежьте тонкими кружочками. Моцареллу натрите на крупной терке.", recipe=r1)
    s8=models.Step(number=8, info="Тесто обомните и раскатайте в тонкую круглую лепешку диаметром около 30 см.", recipe=r1)
    s9=models.Step(number=9, info="Перенесите лепёшку на застелённый пергаментом противень. Это нужно делать сразу, до того, как выложите начинку.", recipe=r1)
    s10=models.Step(number=10, info="Обильно смажьте тесто пряным томатным соусом. Сверху посыпьте тертым сыром. Поверх равномерно распределите кружочки пепперони.", recipe=r1)
    s11=models.Step(number=11, info="Выпекайте пиццу в разогретой до 250°С духовке 8-10 минут. Точное время зависит от вашей духовки. Если есть возможность включить режим 'верх+низ+конвекция', используйте его.", recipe=r1)
    #клубника в шоколаде
    s12=models.Step(number=1, info="Клубнику промойте под проточной холодной водой прямо в дуршлаге. Оставьте ягоды в нём же, чтобы стекла лишняя жидкость. Хвостики не отрывайте, за них будет удобно держать десерт при поедании.", recipe=r2)
    s13=models.Step(number=2, info="Затем разложите клубнику сохнуть на бумажное полотенце. Дополнительно оботрите каждую ягоду — лишняя влага помешает шоколаду покрыть клубнику равномерно. Разложите сухие ягоды на тарелку в один слой и уберите минут на 10-15 в морозилку — на охлажденных ягодах шоколадная глазурь застынет быстрее и не стечёт.", recipe=r2)
    s14=models.Step(number=3, info="Поставьте шоколад в микроволновку на максимальную мощность, время установите 20 секунд (или больше, в зависимости от модели и мощности).", recipe=r2)
    s15=models.Step(number=4, info="Перемешайте шоколад до однородности. Влейте в него растительное масло — оно сделает глазурь более жидкой и удобной в работе.", recipe=r2)
    s16=models.Step(number=5, info="Достаньте из морозилки клубнику. Насадите ягоду на деревянную шпажку. Обмакните ее в растопленный шоколад, кончик с хвостиком можно оставить голеньким. Выкладывайте глазированные ягоды на доску, накрытую пергаментом.", recipe=r2)
    s17=models.Step(number=6, info="Украсьте ягоды полосочками из шоколада контрастного цвета. Вы также можете посыпать их дроблёными орехами, кокосовой стружкой, сублимированными ягодами, кондитерской посыпкой. Уберите доску с клубникой в холодильник для полной стабилизации глазури (хватит 10 минут).", recipe=r2)
    #макароны с сыром
    s18=models.Step(number=1, info="Отварите макароны в кастрюле согласно инструкции на упаковке, обязательно хорошо посолите воду.", recipe=r3)
    s19=models.Step(number=2, info="Натрите на терке весь сыр в нагретую сковороду и добавьте к нему ложку приправ. Хорошо мешайте лопаткой до тех пор, пока весь сыр не расплавится.", recipe=r3)
    s20=models.Step(number=3, info="Отварные макароны выложите в приготовленный сыр. Перемешайте.", recipe=r3)
    #гречка с молоком
    s21=models.Step(number=1, info="Гречку залить кипятком, посолить. Довести до кипения. Убавить огонь до минимального, накрыть крышкой.", recipe=r4)
    s22=models.Step(number=2, info="Кашу варить до готовности, около 25-30 минут.", recipe=r4)
    s23=models.Step(number=3, info="Готовую кашу разложить в тарелки и залить молоком. Добавить в гречневую кашу с молоком кусочек масла.", recipe=r4)
    #чай с малиной
    s24=models.Step(number=1, info="Заварить чёрный чай, охладить. И перелить в кувшин.", recipe=r5)
    s25=models.Step(number=2, info="Малину хорошо промыть и высыпать в охлаждённый чай, добавить воду.", recipe=r5)
    s26=models.Step(number=3, info="Лайм нарежьте кружочками и добавьте в кувшин, по вкусу положите сахар.", recipe=r5)
    s27=models.Step(number=4, info="Украсьте освежающий напиток листиками мяты.", recipe=r5)
    #манник
    s28=models.Step(number=1, info="В миске соедините сметану комнатной температуры и манную крупу. Все хорошенько перемешайте до однородности и оставьте массу на 30 минут, чтобы крупа разбухла. Очень важно, чтобы манка как следует разбухла. Ведь от этого зависит, насколько мягким и нежным получится пирог.", recipe=r6)
    s29=models.Step(number=2, info="В другой миске яйца соедините с сахаром и щепоткой соли. Всё взбейте миксером до пышности примерно 2 минуты. Должна получиться пышная масса с множеством мелких воздушных пузырьков. От того, как вы взобьете яйца, зависит воздушность готовой выпечки.", recipe=r6)
    s30=models.Step(number=3, info="Добавьте в яичную смесь разбухшую в сметане манку и снова взбейте все миксером. В массе не должно остаться никаких комочков.", recipe=r6)
    s31=models.Step(number=4, info="Всыпьте просеянную муку и снова перемешайте тесто до однородности миксером.", recipe=r6)
    s32=models.Step(number=5, info="Вылейте готовое тесто в застеленную пергаментом и смазанную растительным маслом форму для выпекания (Ø 18-20 см). Поставьте манник в разогретую до 180°С духовку примерно на 40-50 минут.", recipe=r6)

    ap1=models.Additional_photo(recipe_photo=r1, img="recipe/files/pizza2.jpg") #дополнительные фото
    ap2=models.Additional_photo(recipe_photo=r1, img="recipe/files/pizza3.jpg") 
    ap3=models.Additional_photo(recipe_photo=r2, img="recipe/files/choko2.jpg") 
    ap4=models.Additional_photo(recipe_photo=r2, img="recipe/files/choko3.jpg")
    ap5=models.Additional_photo(recipe_photo=r2, img="recipe/files/choko4.jpg")
    ap6=models.Additional_photo(recipe_photo=r3, img="recipe/files/mak2.jpg") 
    ap7=models.Additional_photo(recipe_photo=r4, img="recipe/files/grechka2.jpg")
    ap8=models.Additional_photo(recipe_photo=r5, img="recipe/files/chay2.jpg")
    ap9=models.Additional_photo(recipe_photo=r6, img="recipe/files/mannik2.jpg")
    ap10=models.Additional_photo(recipe_photo=r6, img="recipe/files/mannik3.jpg")
    ap11=models.Additional_photo(recipe_photo=r6, img="recipe/files/mannik4.jpg")

    #пицца
    count1=models.Count(recipe=r1, ingredient=i1, count=250, system_of_calc=soc2)
    count2=models.Count(recipe=r1, ingredient=i2, count=120, system_of_calc=soc4)
    count3=models.Count(recipe=r1, ingredient=i3, count=10, system_of_calc=soc2)
    count4=models.Count(recipe=r1, ingredient=i4, count=1, system_of_calc=soc6)
    count5=models.Count(recipe=r1, ingredient=i5, count=1, system_of_calc=soc2)
    count6=models.Count(recipe=r1, ingredient=i6, count=1, system_of_calc=soc2)
    count7=models.Count(recipe=r1, ingredient=i7, count=2, system_of_calc=soc5)
    count8=models.Count(recipe=r1, ingredient=i14, count=1, system_of_calc=soc6)
    count9=models.Count(recipe=r1, ingredient=i9, count=1, system_of_calc=soc6)
    count10=models.Count(recipe=r1, ingredient=i8, count=1, system_of_calc=soc6)
    count11=models.Count(recipe=r1, ingredient=i10, count=2, system_of_calc=soc5)
    count12=models.Count(recipe=r1, ingredient=i11, count=1, system_of_calc=soc6)
    count13=models.Count(recipe=r1, ingredient=i12, count=120, system_of_calc=soc2)
    count14=models.Count(recipe=r1, ingredient=i13, count=100, system_of_calc=soc2)
    #клубника в шоколаде
    count15=models.Count(recipe=r2, ingredient=i15, count=800, system_of_calc=soc2)
    count16=models.Count(recipe=r2, ingredient=i16, count=90, system_of_calc=soc2)
    count17=models.Count(recipe=r2, ingredient=i4, count=2, system_of_calc=soc7)
    #макароны с сыром  
    count17=models.Count(recipe=r3, ingredient=i17, count=300, system_of_calc=soc2)
    count18=models.Count(recipe=r3, ingredient=i12, count=200, system_of_calc=soc2)
    count19=models.Count(recipe=r3, ingredient=i11, count=1, system_of_calc=soc7)
    count20=models.Count(recipe=r3, ingredient=i6, count=1, system_of_calc=soc7)
    #гречка с молоком
    count21=models.Count(recipe=r4, ingredient=i6, count=1, system_of_calc=soc7)
    count22=models.Count(recipe=r4, ingredient=i18, count=200, system_of_calc=soc2)
    count23=models.Count(recipe=r4, ingredient=i19, count=1, system_of_calc=soc3)
    count24=models.Count(recipe=r4, ingredient=i20, count=40, system_of_calc=soc2)
    #чай с малиной
    count25=models.Count(recipe=r5, ingredient=i21, count=100, system_of_calc=soc2)
    count26=models.Count(recipe=r5, ingredient=i22, count=5, system_of_calc=soc5)
    count27=models.Count(recipe=r5, ingredient=i23, count=1, system_of_calc=soc5)
    count28=models.Count(recipe=r5, ingredient=i24, count=2, system_of_calc=soc5)
    count29=models.Count(recipe=r5, ingredient=i5, count=1, system_of_calc=soc6)
    count30=models.Count(recipe=r5, ingredient=i2, count=700, system_of_calc=soc4)
    #манник
    count31=models.Count(recipe=r6, ingredient=i25, count=250, system_of_calc=soc2)
    count32=models.Count(recipe=r6, ingredient=i26, count=200, system_of_calc=soc2)
    count33=models.Count(recipe=r6, ingredient=i27, count=3, system_of_calc=soc5)
    count34=models.Count(recipe=r6, ingredient=i5, count=200, system_of_calc=soc2)
    count35=models.Count(recipe=r6, ingredient=i1, count=150, system_of_calc=soc2)
    count36=models.Count(recipe=r6, ingredient=i6, count=1, system_of_calc=soc7)

    score1=models.Score(user=u1, recipe=r2, like=True, dizlike=False) #баллы
    score2=models.Score(user=u2, recipe=r2, like=True, dizlike=False)
    score3=models.Score(user=u2, recipe=r3, like=False, dizlike=True)
    score4=models.Score(user=u5, recipe=r3, like=True, dizlike=False)
    score5=models.Score(user=u5, recipe=r5, like=False, dizlike=True)
    score6=models.Score(user=u5, recipe=r6, like=True, dizlike=False)
    score7=models.Score(user=u1, recipe=r6, like=True, dizlike=False)
    score8=models.Score(user=u4, recipe=r5, like=True, dizlike=False)

    l1=models.Lang(name="Русский", code="ru") #языки
    l2=models.Lang(name="English", code="en")
    l3=models.Lang(name="Français", code="fr")

    #переводы

    #английский перевод
    t1_cat_en=models.TranslationCategory(category=c1, lang=l2, text="Dessert") #категории на английском
    t2_cat_en=models.TranslationCategory(category=c2, lang=l2, text="Meat")
    t3_cat_en=models.TranslationCategory(category=c3, lang=l2, text="Soup")
    t4_cat_en=models.TranslationCategory(category=c4, lang=l2, text="Fish")
    t5_cat_en=models.TranslationCategory(category=c5, lang=l2, text="Drink")
    t6_cat_en=models.TranslationCategory(category=c6, lang=l2, text="Main dish")

    t1_m_en=models.TranslationMealtime(mealtime=m1, lang=l2, text="Breakfast") #время приёма пищи на английском
    t2_m_en=models.TranslationMealtime(mealtime=m2, lang=l2, text="Lunch")
    t3_m_en=models.TranslationMealtime(mealtime=m3, lang=l2, text="Dinner")

    t1_ingr_en=models.TranslationIngredient(ingredient=i1, lang=l2, text="Wheat flour") #ингредиенты на английском
    t2_ingr_en=models.TranslationIngredient(ingredient=i2, lang=l2, text="Water")  #пицца
    t3_ingr_en=models.TranslationIngredient(ingredient=i3, lang=l2, text="Dry yeast") 
    t4_ingr_en=models.TranslationIngredient(ingredient=i4, lang=l2, text="Vegetable oil")
    t5_ingr_en=models.TranslationIngredient(ingredient=i5, lang=l2, text="Sugar") 
    t6_ingr_en=models.TranslationIngredient(ingredient=i6, lang=l2, text="Salt") 
    t7_ingr_en=models.TranslationIngredient(ingredient=i7, lang=l2, text="Tomatoes") 
    t8_ingr_en=models.TranslationIngredient(ingredient=i8, lang=l2, text="Mayonnaise") 
    t9_ingr_en=models.TranslationIngredient(ingredient=i9, lang=l2, text="Ketchup") 
    t10_ingr_en=models.TranslationIngredient(ingredient=i10, lang=l2, text="Garlic") 
    t11_ingr_en=models.TranslationIngredient(ingredient=i11, lang=l2, text="Seasonings") 
    t12_ingr_en=models.TranslationIngredient(ingredient=i12, lang=l2, text="Mozzarella cheese") 
    t13_ingr_en=models.TranslationIngredient(ingredient=i13, lang=l2, text="Raw smoked sausage") 
    t14_ingr_en=models.TranslationIngredient(ingredient=i14, lang=l2, text="Olive oil") 
    t15_ingr_en=models.TranslationIngredient(ingredient=i15, lang=l2, text="Chocolate") #клубника в шоколаде
    t16_ingr_en=models.TranslationIngredient(ingredient=i16, lang=l2, text="Strawberry") 
    t17_ingr_en=models.TranslationIngredient(ingredient=i17, lang=l2, text="Pasta") #макароны с сыром
    t18_ingr_en=models.TranslationIngredient(ingredient=i18, lang=l2, text="Buckwheat groats") #гречка с молоком
    t19_ingr_en=models.TranslationIngredient(ingredient=i19, lang=l2, text="Milk") 
    t20_ingr_en=models.TranslationIngredient(ingredient=i20, lang=l2, text="Butter") 
    t21_ingr_en=models.TranslationIngredient(ingredient=i21, lang=l2, text="Raspberry") #чай с малиной
    t22_ingr_en=models.TranslationIngredient(ingredient=i22, lang=l2, text="Black tea") 
    t23_ingr_en=models.TranslationIngredient(ingredient=i23, lang=l2, text="Lime")
    t24_ingr_en=models.TranslationIngredient(ingredient=i24, lang=l2, text="Mint") 
    t25_ingr_en=models.TranslationIngredient(ingredient=i25, lang=l2, text="Sour cream") #манник
    t26_ingr_en=models.TranslationIngredient(ingredient=i26, lang=l2, text="Semolina") 
    t27_ingr_en=models.TranslationIngredient(ingredient=i27, lang=l2, text="Egg")
    t28_ingr_en=models.TranslationIngredient(ingredient=i28, lang=l2, text="Pea") #добавочные
    t29_ingr_en=models.TranslationIngredient(ingredient=i29, lang=l2, text="Cucumbers")
    t30_ingr_en=models.TranslationIngredient(ingredient=i30, lang=l2, text="Salmon") 
    t31_ingr_en=models.TranslationIngredient(ingredient=i31, lang=l2, text="Condensed milk")
    t32_ingr_en=models.TranslationIngredient(ingredient=i32, lang=l2, text="Green tea") 
    t33_ingr_en=models.TranslationIngredient(ingredient=i33, lang=l2, text="Chicken")
    t34_ingr_en=models.TranslationIngredient(ingredient=i34, lang=l2, text="Veal") 
    t35_ingr_en=models.TranslationIngredient(ingredient=i35, lang=l2, text="Sheepmeat")
    t36_ingr_en=models.TranslationIngredient(ingredient=i36, lang=l2, text="Apple") 
    t37_ingr_en=models.TranslationIngredient(ingredient=i37, lang=l2, text="Banana")
    t38_ingr_en=models.TranslationIngredient(ingredient=i38, lang=l2, text="Pear") 
    t39_ingr_en=models.TranslationIngredient(ingredient=i39, lang=l2, text="Cookie")
    t40_ingr_en=models.TranslationIngredient(ingredient=i40, lang=l2, text="Potato")

    t1_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc1, lang=l2, text="kg") #система исчисления на английском
    t2_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc2, lang=l2, text="g")
    t3_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc3, lang=l2, text="l")
    t4_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc4, lang=l2, text="ml")
    t5_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc5, lang=l2, text="pcs.")
    t6_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc6, lang=l2, text="tbsp.")
    t7_soc_en=models.TranslationSysOfCalc(sys_of_calc=soc7, lang=l2, text="tsp.")

    t1_r_en=models.TranslationRecipe(recipe=r1, lang=l2, text="Pizza") #рецепты на английском
    t2_r_en=models.TranslationRecipe(recipe=r2, lang=l2, text="Chocolate-covered strawberries")
    t3_r_en=models.TranslationRecipe(recipe=r3, lang=l2, text="Macaroni and cheese")
    t4_r_en=models.TranslationRecipe(recipe=r4, lang=l2, text="Buckwheat with milk") 
    t5_r_en=models.TranslationRecipe(recipe=r5, lang=l2, text="Tea with raspberries")
    t6_r_en=models.TranslationRecipe(recipe=r6, lang=l2, text="Semolina pie")

    #пицца
    t1_s_en=models.TranslationStep(step=s1, lang=l2, text="In warm water heated to 37-40 ° C, dissolve sugar. And then add the yeast and leave for 15 minutes until a fluffy cap appears. If the caps have not appeared, then either the yeast is spoiled, or the water has overheated and the dough will not rise. It needs to be kneaded again.")
    t2_s_en=models.TranslationStep(step=s2, lang=l2, text="Sift the flour into a bowl. Add salt. Mix everything together and make a well in the center of the flour. Pour in the activated yeast and olive oil.") 
    t3_s_en=models.TranslationStep(step=s3, lang=l2, text="Knead a smooth, elastic dough. Knead for about 7-10 minutes, until the dough begins to peel off from your hands. If necessary, you can add a little more olive oil. Cover the bowl with a towel and leave the dough in the heat for 45 minutes to rise.") 
    t4_s_en=models.TranslationStep(step=s4, lang=l2, text="While the dough is rising, prepare the sauce. Combine tomatoes, ketchup, garlic cloves, seasonings and mayonnaise in a blender bowl. Whisk everything until smooth.") 
    t5_s_en=models.TranslationStep(step=s5, lang=l2, text="Heat the vegetable oil in a frying pan over medium heat. Pour out the whipped tomato mixture. Simmer, stirring, for about 5 minutes until the liquid has evaporated and thickened.") 
    t6_s_en=models.TranslationStep(step=s6, lang=l2, text="Remove the finished sauce from the heat and refrigerate.") 
    t7_s_en=models.TranslationStep(step=s7, lang=l2, text="Now prepare the filling. Cut the sausage into thin slices. Grate the mozzarella on a coarse grater.") 
    t8_s_en=models.TranslationStep(step=s8, lang=l2, text="Knead the dough and roll it into a thin round cake with a diameter of about 30 cm.") 
    t9_s_en=models.TranslationStep(step=s9, lang=l2, text="Transfer the tortilla to a parchment-lined baking sheet. This should be done immediately, before you put the filling.") 
    t10_s_en=models.TranslationStep(step=s10, lang=l2, text="Brush the dough liberally with the spicy tomato sauce. Sprinkle grated cheese on top. Spread the pepperoni slices evenly over the top.") 
    t11_s_en=models.TranslationStep(step=s11, lang=l2, text="Bake the pizza in a preheated oven at 250°Bake in the oven for 8-10 minutes. The exact time depends on your oven. If it is possible to turn on the 'top+bottom+convection' mode, use it.") 
    #клубника в шоколаде
    t12_s_en=models.TranslationStep(step=s12, lang=l2, text="Rinse the strawberries under running cold water in a colander. Leave the berries in it to drain the excess liquid. Do not tear off the tails, they will be convenient to hold the dessert when eating.") 
    t13_s_en=models.TranslationStep(step=s13, lang=l2, text="Then spread the strawberries to dry on a paper towel. Additionally, wipe each berry — excess moisture will prevent the chocolate from covering the strawberries evenly. Arrange the dried berries on a plate in a single layer and put them in the freezer for 10-15 minutes — the chocolate glaze will harden faster on the cooled berries and will not drain.") 
    t14_s_en=models.TranslationStep(step=s14, lang=l2, text="Put the chocolate in the microwave at maximum power, set the time to 20 seconds (or more, depending on the model and power).") 
    t15_s_en=models.TranslationStep(step=s15, lang=l2, text="Stir the chocolate until smooth. Pour vegetable oil into it — it will make the glaze more liquid and easier to use.") 
    t16_s_en=models.TranslationStep(step=s16, lang=l2, text="Remove the strawberries from the freezer. Place the berries on a wooden skewer. Dip it in the melted chocolate, the tip and tail can be left bare. Spread the glazed berries on a board covered with parchment.") 
    t17_s_en=models.TranslationStep(step=s17, lang=l2, text="Decorate the berries with stripes of contrasting chocolate. You can also sprinkle them with crushed nuts, coconut chips, freeze-dried berries, and confectionery sprinkles. Put the strawberry board in the refrigerator to fully stabilize the glaze (10 minutes is enough).") 
    #макароны с сыром
    t18_s_en=models.TranslationStep(step=s18, lang=l2, text="Boil the pasta in a saucepan according to the instructions on the package, be sure to add salt to the water well.") 
    t19_s_en=models.TranslationStep(step=s19, lang=l2, text="Grate all the cheese into a heated frying pan and add a spoonful of seasonings to it. Stir well with a spatula until all the cheese has melted.") 
    t20_s_en=models.TranslationStep(step=s20, lang=l2, text="Put the boiled pasta in the cooked cheese. Mix it up.")
    #гречка с молоком 
    t21_s_en=models.TranslationStep(step=s21, lang=l2, text="Pour boiling water over buckwheat and add salt. Bring to a boil. Turn down the heat to a minimum, cover with a lid.") 
    t22_s_en=models.TranslationStep(step=s22, lang=l2, text="Cook porridge until tender, about 25-30 minutes.") 
    t23_s_en=models.TranslationStep(step=s23, lang=l2, text="Put the finished porridge in plates and pour milk over it. Add a piece of butter to the buckwheat porridge with milk.") 
    #чай с малиной
    t24_s_en=models.TranslationStep(step=s24, lang=l2, text="Brew black tea, cool. And pour it into a jug.") 
    t25_s_en=models.TranslationStep(step=s25, lang=l2, text="Wash the raspberries well and pour them into the iced tea, add water.")
    t26_s_en=models.TranslationStep(step=s26, lang=l2, text="Cut the lime into small circles and add it to the jug, add sugar to taste.") 
    t27_s_en=models.TranslationStep(step=s27, lang=l2, text="Decorate a refreshing drink with mint leaves.")
    #манник
    t28_s_en=models.TranslationStep(step=s28, lang=l2, text="In a bowl, combine sour cream at room temperature and semolina. Mix everything well until smooth and leave the mass for 30 minutes so that the cereal swells. It is very important that the semolina is properly swollen. After all, it depends on how soft and tender the pie will turn out.") 
    t29_s_en=models.TranslationStep(step=s29, lang=l2, text="In another bowl, combine the eggs with sugar and a pinch of salt. Beat everything with a mixer until fluffy for about 2 minutes. You should get a lush mass with lots of small air bubbles. The lightness of the finished pastry depends on how you beat the eggs.")
    t30_s_en=models.TranslationStep(step=s30, lang=l2, text="Add the semolina swollen in sour cream to the egg mixture and beat everything again with a mixer. There should be no lumps left in the mass.") 
    t31_s_en=models.TranslationStep(step=s31, lang=l2, text="Add the sifted flour and mix the dough again until smooth with a mixer.")
    t32_s_en=models.TranslationStep(step=s32, lang=l2, text="Pour the finished dough into a baking dish lined with parchment and greased with vegetable oil (Ø 18-20 cm). Place the mannikin in a preheated 180°C oven for about 40-50 minutes.")

    #французский перевод
    t1_cat_fr=models.TranslationCategory(category=c1, lang=l3, text="Dessert") #категории на французском
    t2_cat_fr=models.TranslationCategory(category=c2, lang=l3, text="Viande")
    t3_cat_fr=models.TranslationCategory(category=c3, lang=l3, text="Soupe")
    t4_cat_fr=models.TranslationCategory(category=c4, lang=l3, text="Poisson")
    t5_cat_fr=models.TranslationCategory(category=c5, lang=l3, text="Boisson")
    t6_cat_fr=models.TranslationCategory(category=c6, lang=l3, text="L'essentiel")

    t1_m_fr=models.TranslationMealtime(mealtime=m1, lang=l3, text="Petit Déjeuner") #время приёма пищи на французском
    t2_m_fr=models.TranslationMealtime(mealtime=m2, lang=l3, text="Déjeuner")
    t3_m_fr=models.TranslationMealtime(mealtime=m3, lang=l3, text="Dinner")

    t1_ingr_fr=models.TranslationIngredient(ingredient=i1, lang=l3, text="Farine de froment") #ингредиенты на французском
    t2_ingr_fr=models.TranslationIngredient(ingredient=i2, lang=l3, text="Eau")  #пицца
    t3_ingr_fr=models.TranslationIngredient(ingredient=i3, lang=l3, text="Levure sèche") 
    t4_ingr_fr=models.TranslationIngredient(ingredient=i4, lang=l3, text="Huile végétale")
    t5_ingr_fr=models.TranslationIngredient(ingredient=i5, lang=l3, text="Sucre") 
    t6_ingr_fr=models.TranslationIngredient(ingredient=i6, lang=l3, text="Sel") 
    t7_ingr_fr=models.TranslationIngredient(ingredient=i7, lang=l3, text="Tomates") 
    t8_ingr_fr=models.TranslationIngredient(ingredient=i8, lang=l3, text="Mayonnaise") 
    t9_ingr_fr=models.TranslationIngredient(ingredient=i9, lang=l3, text="Ketchup") 
    t10_ingr_fr=models.TranslationIngredient(ingredient=i10, lang=l3, text="Ail") 
    t11_ingr_fr=models.TranslationIngredient(ingredient=i11, lang=l3, text="Assaisonnements") 
    t12_ingr_fr=models.TranslationIngredient(ingredient=i12, lang=l3, text="Fromage Mozzarella") 
    t13_ingr_fr=models.TranslationIngredient(ingredient=i13, lang=l3, text="Saucisse fumée") 
    t14_ingr_fr=models.TranslationIngredient(ingredient=i14, lang=l3, text="Huile d'olive") 
    t15_ingr_fr=models.TranslationIngredient(ingredient=i15, lang=l3, text="Chocolat") #клубника в шоколаде
    t16_ingr_fr=models.TranslationIngredient(ingredient=i16, lang=l3, text="Fraise") 
    t17_ingr_fr=models.TranslationIngredient(ingredient=i17, lang=l3, text="Macaroni") #макароны с сыром
    t18_ingr_fr=models.TranslationIngredient(ingredient=i18, lang=l3, text="Sarrasin") #гречка с молоком
    t19_ingr_fr=models.TranslationIngredient(ingredient=i19, lang=l3, text="Lait")
    t20_ingr_fr=models.TranslationIngredient(ingredient=i20, lang=l3, text="Beurre") 
    t21_ingr_fr=models.TranslationIngredient(ingredient=i21, lang=l3, text="Framboise") #чай с малиной
    t22_ingr_fr=models.TranslationIngredient(ingredient=i22, lang=l3, text="Thé noir") 
    t23_ingr_fr=models.TranslationIngredient(ingredient=i23, lang=l3, text="Lime")
    t24_ingr_fr=models.TranslationIngredient(ingredient=i24, lang=l3, text="Menthe") 
    t25_ingr_fr=models.TranslationIngredient(ingredient=i25, lang=l3, text="Crème fraîche") #манник
    t26_ingr_fr=models.TranslationIngredient(ingredient=i26, lang=l3, text="Semoule") 
    t27_ingr_fr=models.TranslationIngredient(ingredient=i27, lang=l3, text="Œuf")
    t28_ingr_fr=models.TranslationIngredient(ingredient=i28, lang=l3, text="Pois") #добавочные
    t29_ingr_fr=models.TranslationIngredient(ingredient=i29, lang=l3, text="Concombres")
    t30_ingr_fr=models.TranslationIngredient(ingredient=i30, lang=l3, text="Saumon") 
    t31_ingr_fr=models.TranslationIngredient(ingredient=i31, lang=l3, text="Lait condensé")
    t32_ingr_fr=models.TranslationIngredient(ingredient=i32, lang=l3, text="Thé vert") 
    t33_ingr_fr=models.TranslationIngredient(ingredient=i33, lang=l3, text="Poulet")
    t34_ingr_fr=models.TranslationIngredient(ingredient=i34, lang=l3, text="Veau") 
    t35_ingr_fr=models.TranslationIngredient(ingredient=i35, lang=l3, text="Viande de mouton")
    t36_ingr_fr=models.TranslationIngredient(ingredient=i36, lang=l3, text="Pomme") 
    t37_ingr_fr=models.TranslationIngredient(ingredient=i37, lang=l3, text="Banane")
    t38_ingr_fr=models.TranslationIngredient(ingredient=i38, lang=l3, text="Poire") 
    t39_ingr_fr=models.TranslationIngredient(ingredient=i39, lang=l3, text="Biscuit")
    t40_ingr_fr=models.TranslationIngredient(ingredient=i40, lang=l3, text="Pommes de terre")

    t1_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc1, lang=l3, text="kg") #система исчисления на французском
    t2_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc2, lang=l3, text="g")
    t3_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc3, lang=l3, text="l")
    t4_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc4, lang=l3, text="ml")
    t5_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc5, lang=l3, text="pce")
    t6_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc6, lang=l3, text="c. à s.")
    t7_soc_fr=models.TranslationSysOfCalc(sys_of_calc=soc7, lang=l3, text="c. à c.")

    t1_r_fr=models.TranslationRecipe(recipe=r1, lang=l3, text="Pizza") #рецепты на французском 
    t2_r_fr=models.TranslationRecipe(recipe=r2, lang=l3, text="Fraises au chocolat")
    t3_r_fr=models.TranslationRecipe(recipe=r3, lang=l3, text="Macaroni au fromage")
    t4_r_fr=models.TranslationRecipe(recipe=r4, lang=l3, text="Sarrasin au lait") 
    t5_r_fr=models.TranslationRecipe(recipe=r5, lang=l3, text="Thé aux framboises")
    t6_r_fr=models.TranslationRecipe(recipe=r6, lang=l3, text="Glycérie")

    #пицца
    t1_s_fr=models.TranslationStep(step=s1, lang=l3, text="Dans l'eau tiède, chauffée à 37-40°C, dissoudre le sucre. Et puis versez la levure et laissez-la pendant 15 minutes jusqu'à ce qu'un bonnet luxuriant apparaisse. Si les bouchons ne sont pas apparus, la levure est gâtée ou l'eau surchauffée et la pâte ne Monte pas. Il faut pétrir à nouveau.")
    t2_s_fr=models.TranslationStep(step=s2, lang=l3, text="Dans un bol, tamiser la farine. Verser le sel. Mélangez le tout et faites une dépression au centre de la farine. Versez-y la levure activée et l'huile d'olive.") 
    t3_s_fr=models.TranslationStep(step=s3, lang=l3, text="Pétrir une pâte élastique et homogène. Pétrir environ 7-10 minutes, jusqu'à ce que la pâte commence à se détacher des mains. Si nécessaire, vous pouvez ajouter un peu plus d'huile d'olive. Couvrir le bol avec une serviette et laisser la pâte 45 minutes au chaud pour lever.") 
    t4_s_fr=models.TranslationStep(step=s4, lang=l3, text="Pendant que la pâte Monte, préparez la sauce. Dans le bol du mélangeur, mélanger les tomates, le ketchup, les gousses d'ail, les assaisonnements et la mayonnaise. Fouetter le tout jusqu'à consistance lisse.") 
    t5_s_fr=models.TranslationStep(step=s5, lang=l3, text="Dans une poêle à feu moyen, chauffer l'huile végétale. Verser le mélange de tomates fouettées. Laisser mijoter, en remuant, environ 5 minutes jusqu'à ce que le liquide s'évapore et soit épais.") 
    t6_s_fr=models.TranslationStep(step=s6, lang=l3, text="Retirer la sauce prête du feu et réfrigérer.") 
    t7_s_fr=models.TranslationStep(step=s7, lang=l3, text="Maintenant, préparez la farce. Couper la saucisse en fines tranches. Râper la mozzarella sur une grande râpe.") 
    t8_s_fr=models.TranslationStep(step=s8, lang=l3, text="La pâte est écrasée et roulée en une fine tortilla ronde d'environ 30 cm de diamètre.") 
    t9_s_fr=models.TranslationStep(step=s9, lang=l3, text="Transférer la tortilla sur une plaque à pâtisserie recouverte de parchemin. Cela doit être fait immédiatement, avant de disposer le remplissage.") 
    t10_s_fr=models.TranslationStep(step=s10, lang=l3, text="Graisser abondamment la pâte avec la sauce tomate épicée. Saupoudrer de fromage râpé sur le dessus. Sur le dessus, répartir uniformément les cercles de pepperoni.") 
    t11_s_fr=models.TranslationStep(step=s11, lang=l3, text="Cuire la pizza dans un four préchauffé à 250 ° C pendant 8-10 minutes. L'heure exacte dépend de votre four. S'il est possible d'activer le mode 'haut+bas+convection', utilisez-le.") 
    #клубника в шоколаде
    t12_s_fr=models.TranslationStep(step=s12, lang=l3, text="Rincer les fraises sous l'eau froide courante directement dans une passoire. Laissez les baies dans le même verre à l'excès de liquide. Les queues ne se détachent pas, elles seront pratiques pour tenir le dessert en mangeant.") 
    t13_s_fr=models.TranslationStep(step=s13, lang=l3, text="Ensuite, étalez les fraises sur une serviette en papier. En outre, essuyez chaque baie — l'excès d'humidité empêchera le chocolat de couvrir les fraises uniformément. Étalez les baies sèches sur une assiette en une seule couche et retirez les minutes 10-15 dans le congélateur — sur les baies refroidies, le glaçage au chocolat gèlera plus rapidement et ne s'écoulera pas.") 
    t14_s_fr=models.TranslationStep(step=s14, lang=l3, text="Mettez le chocolat au micro-ondes à la puissance maximale, le temps est réglé sur 20 secondes (ou plus, selon le modèle et la puissance).") 
    t15_s_fr=models.TranslationStep(step=s15, lang=l3, text="Incorporer le chocolat jusqu'à consistance lisse. Versez — y de l'huile végétale-elle rendra le glaçage plus liquide et plus facile à travailler.") 
    t16_s_fr=models.TranslationStep(step=s16, lang=l3, text="Sortez les fraises du congélateur. Plantez les baies sur une brochette en bois. Trempez-le dans du chocolat fondu, la pointe avec la queue peut être laissée nue. Étaler les baies vitrées sur une planche recouverte de parchemin.") 
    t17_s_fr=models.TranslationStep(step=s17, lang=l3, text="Décorez les baies avec des bandes de chocolat de couleur contrastante. Vous pouvez également les saupoudrer de noix concassées, de copeaux de noix de coco, de baies lyophilisées, de pépites de confiserie. Retirez la planche avec les fraises dans le réfrigérateur pour stabiliser complètement le glaçage (10 minutes suffisent).") 
    #макароны с сыром
    t18_s_fr=models.TranslationStep(step=s18, lang=l3, text="Faire bouillir les pâtes dans une casserole selon les instructions sur l'emballage, assurez-vous de bien Saler l'eau.") 
    t19_s_fr=models.TranslationStep(step=s19, lang=l3, text="Râpez tout le fromage dans une poêle chauffée et ajoutez-y une cuillerée d'assaisonnements. Remuez bien avec une spatule jusqu'à ce que tout le fromage soit fondu.") 
    t20_s_fr=models.TranslationStep(step=s20, lang=l3, text="Mettez les pâtes bouillies dans le fromage cuit. Mélangez.")
    #гречка с молоком 
    t21_s_fr=models.TranslationStep(step=s21, lang=l3, text="Sarrasin verser de l'eau bouillante, sel. Porter à ébullition. Réduire le feu au minimum, couvrir.") 
    t22_s_fr=models.TranslationStep(step=s22, lang=l3, text="Cuire la bouillie jusqu'à tendreté, environ 25-30 minutes.") 
    t23_s_fr=models.TranslationStep(step=s23, lang=l3, text="Mettez la bouillie prête dans des assiettes et versez le lait. Ajouter un morceau de beurre à la bouillie de sarrasin avec du lait.") 
    #чай с малиной
    t24_s_fr=models.TranslationStep(step=s24, lang=l3, text="Infuser le thé noir, refroidir. Et verser dans une cruche.") 
    t25_s_fr=models.TranslationStep(step=s25, lang=l3, text="Rincez bien les framboises et versez-les dans du thé refroidi, ajoutez de l'eau.")
    t26_s_fr=models.TranslationStep(step=s26, lang=l3, text="Couper le citron vert en tranches et ajouter au pichet, mettre le sucre au goût.") 
    t27_s_fr=models.TranslationStep(step=s27, lang=l3, text="Décorez la boisson rafraîchissante avec des feuilles de menthe.")
    #манник
    t28_s_fr=models.TranslationStep(step=s28, lang=l3, text="Dans un bol, mélanger la crème sure à température ambiante et la semoule. Bien mélanger jusqu'à consistance lisse et laisser la masse pendant 30 minutes pour que le croup gonfle. Il est très important que la semoule gonfle correctement. Après tout, cela dépend de la douceur et de la douceur du gâteau.") 
    t29_s_fr=models.TranslationStep(step=s29, lang=l3, text="Dans un autre bol, mélanger les œufs avec le sucre et une pincée de sel. Fouetter le tout avec un mélangeur jusqu'à ce qu'il soit luxuriant pendant environ 2 minutes. Devrait obtenir une masse luxuriante avec beaucoup de petites bulles d'air. De la façon dont vous soulevez les œufs, dépend de la légèreté de la cuisson finie.")
    t30_s_fr=models.TranslationStep(step=s30, lang=l3, text="Ajouter la semoule gonflée dans la crème sure au mélange d'œufs et fouetter à nouveau le tout avec un mélangeur. Dans la masse, il ne devrait pas y avoir de grumeaux.") 
    t31_s_fr=models.TranslationStep(step=s31, lang=l3, text="Verser la farine tamisée et mélanger à nouveau la pâte jusqu'à consistance lisse avec un mélangeur.")
    t32_s_fr=models.TranslationStep(step=s32, lang=l3, text="Verser la pâte finie dans un plat allant au four recouvert de parchemin et graissé avec de l'huile végétale (Ø 18-20 cm). Mettez le mannik dans un four préchauffé à 180°C pendant environ 40-50 minutes.")


    session.add_all([u1,u2,u3,u4,u5,
                    c1,c2,c3,c4,c5,c6,
                    m1,m2,m3,
                    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    soc1,soc2,soc3,soc4,soc5,soc6,soc7,
                    r1,r2,r3,r4,r5,r6,
                    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,
                    ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8,ap9,ap10,ap11, 
                    count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,
                    count11,count12,count13,count14,count15,count16,count17,count18,count19,count20,
                    count21,count22,count23,count24,count25,count26,count27,count28,count29,count30,
                    count31,count32,count33,count34,count35,count36,
                    score1,score2,score3,score4,score5,score6,score7,score8,
                    l1,l2,l3,
                    #английский перевод
                    t1_cat_en, t2_cat_en, t3_cat_en, t4_cat_en, t5_cat_en, t6_cat_en,
                    t1_m_en, t2_m_en, t3_m_en,
                    t1_ingr_en, t2_ingr_en, t3_ingr_en, t4_ingr_en, t5_ingr_en, t6_ingr_en, t7_ingr_en, t8_ingr_en, t9_ingr_en, t10_ingr_en,
                    t11_ingr_en, t12_ingr_en, t13_ingr_en, t14_ingr_en, t15_ingr_en, t16_ingr_en, t17_ingr_en, t18_ingr_en, t19_ingr_en, t20_ingr_en,
                    t21_ingr_en, t22_ingr_en, t23_ingr_en, t24_ingr_en, t25_ingr_en, t26_ingr_en, t27_ingr_en, t28_ingr_en, t29_ingr_en, t30_ingr_en,
                    t31_ingr_en, t32_ingr_en, t33_ingr_en, t34_ingr_en, t35_ingr_en, t36_ingr_en, t37_ingr_en, t38_ingr_en, t39_ingr_en, t40_ingr_en,
                    t1_soc_en, t2_soc_en, t3_soc_en, t4_soc_en, t5_soc_en, t6_soc_en, t7_soc_en,
                    t1_s_en, t2_s_en, t3_s_en, t4_s_en, t5_s_en, t6_s_en, t7_s_en, t8_s_en, t9_s_en, t10_s_en,
                    t11_s_en, t12_s_en, t13_s_en, t14_s_en, t15_s_en, t16_s_en, t17_s_en, t18_s_en, t19_s_en, t20_s_en,
                    t21_s_en, t22_s_en, t23_s_en, t24_s_en, t25_s_en, t26_s_en, t27_s_en, t28_s_en, t29_s_en, t30_s_en, t31_s_en, t32_s_en,
                    #французский перевод
                    t1_cat_fr, t2_cat_fr, t3_cat_fr, t4_cat_fr, t5_cat_fr, t6_cat_fr, 
                    t1_m_fr, t2_m_fr, t3_m_fr,
                    t1_ingr_fr, t2_ingr_fr, t3_ingr_fr, t4_ingr_fr, t5_ingr_fr, t6_ingr_fr, t7_ingr_fr, t8_ingr_fr, t9_ingr_fr, t10_ingr_fr,
                    t11_ingr_fr, t12_ingr_fr, t13_ingr_fr, t14_ingr_fr, t15_ingr_fr, t16_ingr_fr, t17_ingr_fr, t18_ingr_fr, t19_ingr_fr, t20_ingr_fr,
                    t21_ingr_fr, t22_ingr_fr, t23_ingr_fr, t24_ingr_fr, t25_ingr_fr, t26_ingr_fr, t27_ingr_fr, t28_ingr_fr, t29_ingr_fr, t30_ingr_fr,
                    t31_ingr_fr, t32_ingr_fr, t33_ingr_fr, t34_ingr_fr, t35_ingr_fr, t36_ingr_fr, t37_ingr_fr, t38_ingr_fr, t39_ingr_fr, t40_ingr_fr,
                    t1_soc_fr, t2_soc_fr, t3_soc_fr, t4_soc_fr, t5_soc_fr, t6_soc_fr, t7_soc_fr,
                    t1_s_fr, t2_s_fr, t3_s_fr, t4_s_fr, t5_s_fr, t6_s_fr, t7_s_fr, t8_s_fr, t9_s_fr, t10_s_fr,
                    t11_s_fr, t12_s_fr, t13_s_fr, t14_s_fr, t15_s_fr, t16_s_fr, t17_s_fr, t18_s_fr, t19_s_fr, t20_s_fr,
                    t21_s_fr, t22_s_fr, t23_s_fr, t24_s_fr, t25_s_fr, t26_s_fr, t27_s_fr, t28_s_fr, t29_s_fr, t30_s_fr, t31_s_fr, t32_s_fr
                    ])
    session.commit()

