# Географічна транслітерація

Інструмент для транслітерації топонімів. У основі географічна транслітерація УКППТ 1996, у якій прибрані апострофи, усунено дублювання у «iie» та «iia», «ьо» транслітерується як «io».

[translit.a3.kyiv.ua](http://translit.a3.kyiv.ua) · [Demo on Github](https://agentyzmin.github.io/a3-tools/a3_translit/)



# **Додаткові скрипти**
Постійно копіювати текст з браузера незручно, а продукти Adobe вміють працювати зі скриптами Java Script. Тому чому б не перенести транслітератор безпосередньо у Ілюстратор та Індизайн.

Завантажити jsx-скрипти:

[Adobe Illustrator](https://raw.githubusercontent.com/agentyzmin/a3-tools/master/a3_translit/scripts/A3%20Translit%20(AI).jsx) · [Adobe InDesign](https://raw.githubusercontent.com/agentyzmin/a3-tools/master/a3_translit/scripts/A3%20Translit%20(ID).jsx)



## **Як працює у Adobe Illustrator**

Обираєте текст, запускаєте скрипт. Працює з точковим текстом, текстовими фреймами, текстом на кривих.

[![Скрипт для транслітерації в Adobe Illustrator](http://img.youtube.com/vi/0NphpSzBg2Q/0.jpg)](http://www.youtube.com/watch?v=0NphpSzBg2Q "Скрипт для транслітерації в Adobe Illustrator")



## **Як працює у Adobe InDesign**

Обираєте текст, запускаєте скрипт. Дякуємо Дмитру Чернишу за допомогу із вдосконаленням скрипту.

[![Скрипт для транслітерації в Adobe InDesign](http://img.youtube.com/vi/8m3ksfNvGlg/0.jpg)](http://www.youtube.com/watch?v=8m3ksfNvGlg "Скрипт для транслітерації в Adobe InDesign")



## **Як інсталювати скрипти**

### **Adobe Illustrator**

Збережіть скрипт .jsx у папку:
* для Mac OS: Applications\Adobe Illustrator 2020\Presets\en_GB\Scripts
* для Windows: C:\Program Files\Adobe\Adobe Illustrator 2020\Presets\en_US\Scripts

«2020» — версія встановленої програми.
«en_GB» — код встановленої мови, тому файл якщо у вас Ілюстратор не англійською.

### **Adobe InDesign**

Відкрийте панель скриптів Window > Utilities > Scripts, тоді клацніть правою кнопкою миші на папках Application чи User. Краще використати папку User для ваших скриптів (папка Application зробить доступними вскрити для всіх користувачів на цьому комп’ютері, але для цього потрібні права адміністратора). Щоб відкрити папку, у контектному меню оберіть Reveal in Finder (чи Reveal для Windows).

![Reveal in Finder](https://indesignsecrets.com/wp-content/uploads/2017/10/revealinfinder_new.jpeg)


## **Офіційна транслітерація**

За тим же принципом тільки з використанням офіційної транслітерації українського алфавіту латиницею затвердженої [постановою](https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF) Кабінету Міністрів України №55 від 27 січня 2010 р.

Завантажити jsx-скрипти офіційної транслітерації:

[Adobe Illustrator](https://raw.githubusercontent.com/agentyzmin/a3-tools/master/a3_translit/scripts/Translit%20KMU%202010%20(AI).jsx) · [Adobe InDesign](https://raw.githubusercontent.com/agentyzmin/a3-tools/master/a3_translit/scripts/Translit%20KMU%202010%20(ID).jsx)



## **P.S. Як створити свій скрипт**

Також на основі цих скритіп можна створити свій, який буде міняти символи саме ті, які вам потрібні. Чи то ваш варіант транслітерації, чи якась своя ідея.

За заміну символів у скрипті відповідає функція *translit*:

```jsx
function translit() {
	myGrep('іє', 'ie'); 
	…
}
```

Кожен рядок замінює один символ на інший:

```jsx
myGrep('іє', 'ie');
```

'іє' — знаходимо літери «іє», 'ie' — замінюємо на ie.
