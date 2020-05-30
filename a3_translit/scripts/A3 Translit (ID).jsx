// v.0.1
// Транслітератор тексту від Агентів змін — http://translit.a3.kyiv.ua. Автор — Олександр Колодько.
// Інструмент для транслітерації топонімів. У основі географічна транслітерація УКППТ 1996, у якій прибрані апострофи, усунено дублювання у «iie» та «iia», «ьо» транслітерується як «io».
// Побажання та відгуки надсилайте на info@a3.kyiv.ua
// https://github.com/agentyzmin/a3-tools/tree/master/a3_translit

// Line below allows for script to be undone entirely. Comment it and uncomment the next line "Main()" to be able to undo the script step by step
app.doScript(Main, ScriptLanguage.JAVASCRIPT, undefined, UndoModes.ENTIRE_SCRIPT, "Run Script");
// Main();

function Main() {

  if (app.selection.length < 1) { exit(); }

  for (var i = 0; i < app.selection.length; i++) {

    switch (app.selection[i].constructor) {
      case TextFrame:
      case TextColumn:
      case Text:
      case Cell:
      case Paragraph:
      case Word:
        var translitText = translit(app.selection[i].contents);
        app.selection[i].contents = translitText;
        break;
      case GraphicLine:
      case Oval:
      case Polygon:
      case Rectangle:
      case TextFrame:
      case EPSText:
      case SplineItem:
        if (app.selection[i].textPaths.length > 0) {
          var translitText = translit(app.selection[i].textPaths[0].contents);
          app.selection[i].textPaths[0].contents = translitText;
        }
        break;
      default:
        break;
    }
  }
  
  function translit(input) {
    input = input || '';

    return input
      .replace(/іє/g, 'ie') // Exception
      .replace(/Іє/g, 'Ie') // Exception
      .replace(/ія/g, 'ia') // Exception
      .replace(/Ія/g, 'Ia') // Exception
      .replace(/зг/g, 'zgh') // Exception
      .replace(/Зг/g, 'Zgh') // Exception
      .replace(/ьо/g, 'io') // Exception
      .replace(/а/g, 'a')
      .replace(/б/g, 'b')
      .replace(/в/g, 'v')
      .replace(/г/g, 'h')
      .replace(/ґ/g, 'g')
      .replace(/д/g, 'd')
      .replace(/е/g, 'e')
      .replace(/(^|\s)є/g, '$1ye')
      .replace(/є/g, 'ie')
      .replace(/ж/g, 'zh')
      .replace(/з/g, 'z')
      .replace(/и/g, 'y')
      .replace(/і/g, 'i')
      .replace(/(^|\s)ї/g, '$1yi')
      .replace(/ї/g, 'i')
      .replace(/(^|\s)й/g, '$1y')
      .replace(/й/g, 'i')
      .replace(/к/g, 'k')
      .replace(/л/g, 'l')
      .replace(/м/g, 'm')
      .replace(/н/g, 'n')
      .replace(/о/g, 'o')
      .replace(/п/g, 'p')
      .replace(/р/g, 'r')
      .replace(/с/g, 's')
      .replace(/т/g, 't')
      .replace(/у/g, 'u')
      .replace(/ф/g, 'f')
      .replace(/х/g, 'kh')
      .replace(/ц/g, 'ts')
      .replace(/ч/g, 'ch')
      .replace(/ш/g, 'sh')
      .replace(/щ/g, 'sch')
      .replace(/ь/g, '')
      .replace(/(^|\s)ю/g, '$1yu')
      .replace(/ю/g, 'iu')
      .replace(/(^|\s)я/g, '$1ya')
      .replace(/я/g, 'ia')
      .replace(/А/g, 'A')
      .replace(/Б/g, 'B')
      .replace(/В/g, 'V')
      .replace(/Г/g, 'H')
      .replace(/Ґ/g, 'G')
      .replace(/Д/g, 'D')
      .replace(/Е/g, 'E')
      .replace(/(^|\s)Є/g, '$1Ye')
      .replace(/Є/g, 'Ie')
      .replace(/Ж/g, 'Zh')
      .replace(/З/g, 'Z')
      .replace(/И/g, 'Y')
      .replace(/І/g, 'I')
      .replace(/(^|\s)Ї/g, '$1Yi')
      .replace(/Ї/g, 'I')
      .replace(/(^|\s)Й/g, '$1Y')
      .replace(/Й/g, 'I')
      .replace(/К/g, 'K')
      .replace(/Л/g, 'L')
      .replace(/М/g, 'M')
      .replace(/Н/g, 'N')
      .replace(/О/g, 'O')
      .replace(/П/g, 'P')
      .replace(/Р/g, 'R')
      .replace(/С/g, 'S')
      .replace(/Т/g, 'T')
      .replace(/У/g, 'U')
      .replace(/Ф/g, 'F')
      .replace(/Х/g, 'Kh')
      .replace(/Ц/g, 'Ts')
      .replace(/Ч/g, 'Ch')
      .replace(/Ш/g, 'Sh')
      .replace(/Щ/g, 'Sch')
      .replace(/Ь/g, '')
      .replace(/(^|\s)Ю/g, '$1Yu')
      .replace(/Ю/g, 'Iu')
      .replace(/(^|\s)Я/g, '$1Ya')
      .replace(/Я/g, 'Ia')
      .replace(/'/g, '')
      .replace(/’/g, '');
  }

}

//redraw();
