jQuery(function ($) {
    var $res = $('#resultText'),
        $src = $('#sourceText');

    $src.on('input change', function () {
        onChange($src.val());
    });

    if (window.localStorage) {
        var val = localStorage.getItem('savedSrc') || '';
        $src.val(val);
        onChange(val);
    }

    function onChange(val) {
        $res.val(translit(val));

        if (window.localStorage) {
            localStorage.setItem('savedSrc', val);
        }
    }

    function translit(input) {
        input = input || '';

        return input
            .replace(/іє/g, 'ie') // Exception
            .replace(/Іє/g, 'Ie') // Exception
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
            .replace(/Т/g, 'Y')
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
            .replace(/'/g, '');
    }
});