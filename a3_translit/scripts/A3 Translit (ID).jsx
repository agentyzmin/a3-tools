// v.0.1
// Транслітератор тексту від Агентів змін — http://translit.a3.kyiv.ua. Автор — Олександр Колодько.
// Інструмент для транслітерації топонімів. У основі географічна транслітерація УКППТ 1996, у якій прибрані апострофи, усунено дублювання у «iie» та «iia», «ьо» транслітерується як «io».
// Побажання та відгуки надсилайте на info@a3.kyiv.ua
// https://github.com/agentyzmin/a3-tools/tree/master/a3_translit

// Line below allows for script to be undone at once. Comment it and uncomment the next line "Main()" to be able to undo the script step by step
app.doScript(Main, ScriptLanguage.JAVASCRIPT, undefined, UndoModes.ENTIRE_SCRIPT, "Run Script");
// Main();

function Main() {

  var changeObject;
  var selList = app.selection;

  if (selList.length < 1) { exit(); }

  function myGrep(findString, changeString) {
    app.findGrepPreferences = NothingEnum.NOTHING;
    app.changeGrepPreferences = NothingEnum.NOTHING;
    try {
      app.findGrepPreferences.findWhat = findString;
      app.changeGrepPreferences.changeTo = changeString;
      changeObject.changeGrep();
    } catch (e) {}
  }

  function translit() {
    myGrep('іє', 'ie'); // Exception
    myGrep('Іє', 'Ie'); // Exception
    myGrep('ія', 'ia'); // Exception
    myGrep('Ія', 'Ia'); // Exception
    myGrep('зг', 'zgh');// Exception
    myGrep('Зг', 'Zgh'); // Exception
    myGrep('ьо', 'io'); // Exception
    myGrep('а', 'a');
    myGrep('б', 'b');
    myGrep('в', 'v');
    myGrep('г', 'h');
    myGrep('ґ', 'g');
    myGrep('д', 'd');
    myGrep('е', 'e');
    myGrep('(^|\\s)є', '$1ye');
    myGrep('є', 'ie');
    myGrep('ж', 'zh');
    myGrep('з', 'z');
    myGrep('и', 'y');
    myGrep('і', 'i');
    myGrep('(^|\\s)ї', '$1yi');
    myGrep('ї', 'i');
    myGrep('(^|\\s)й', '$1y');
    myGrep('й', 'i');
    myGrep('к', 'k');
    myGrep('л', 'l');
    myGrep('м', 'm');
    myGrep('н', 'n');
    myGrep('о', 'o');
    myGrep('п', 'p');
    myGrep('р', 'r');
    myGrep('с', 's');
    myGrep('т', 't');
    myGrep('у', 'u');
    myGrep('ф', 'f');
    myGrep('х', 'kh');
    myGrep('ц', 'ts');
    myGrep('ч', 'ch');
    myGrep('ш', 'sh');
    myGrep('щ', 'sch');
    myGrep('ь', '');
    myGrep('(^|\\s)ю', '$1yu');
    myGrep('ю', 'iu');
    myGrep('(^|\\s)я', '$1ya');
    myGrep('я', 'ia');
    myGrep('А', 'A');
    myGrep('Б', 'B');
    myGrep('В', 'V');
    myGrep('Г', 'H');
    myGrep('Ґ', 'G');
    myGrep('Д', 'D');
    myGrep('Е', 'E');
    myGrep('(^|\\s)Є', '$1Ye');
    myGrep('Є', 'Ie');
    myGrep('Ж', 'Zh');
    myGrep('З', 'Z');
    myGrep('И', 'Y');
    myGrep('І', 'I');
    myGrep('(^|\\s)Ї', '$1Yi');
    myGrep('Ї', 'I');
    myGrep('(^|\\s)Й', '$1Y');
    myGrep('Й', 'I');
    myGrep('К', 'K');
    myGrep('Л', 'L');
    myGrep('М', 'M');
    myGrep('Н', 'N');
    myGrep('О', 'O');
    myGrep('П', 'P');
    myGrep('Р', 'R');
    myGrep('С', 'S');
    myGrep('Т', 'T');
    myGrep('У', 'U');
    myGrep('Ф', 'F');
    myGrep('Х', 'Kh');
    myGrep('Ц', 'Ts');
    myGrep('Ч', 'Ch');
    myGrep('Ш', 'Sh');
    myGrep('Щ', 'Sch');
    myGrep('Ь', '');
    myGrep('(^|\\s)Ю', '$1Yu');
    myGrep('Ю', 'Iu');
    myGrep('(^|\\s)Я', '$1Ya');
    myGrep('Я', 'Ia');
    myGrep("'", "");
    myGrep("’", "");
  }

  function switchAndTranslit(chObj) {
    switch (chObj.constructor) {
      case TextColumn:
      case TextFrame:
      case Text:
      case Cell:
      case Paragraph:
      case Word:
        changeObject = chObj;
        break;
      case GraphicLine:
      case Oval:
      case Polygon:
      case Rectangle:
      case EPSText:
      case SplineItem:
        if (chObj.textPaths.length > 0) {
          changeObject = chObj.textPaths[0];
        }
        break;
      default:
        break;
    }

    translit();
  }

  for (var i = selList.length; i--;) {
    if (selList[i] instanceof Group) {
      for (var j = selList[i].allPageItems.length; j--;) {
        changeObject = selList[i].allPageItems[j];
        switchAndTranslit(changeObject);
      }
    } else {
      changeObject = selList[i];
      switchAndTranslit(changeObject);
    }
  }
}
