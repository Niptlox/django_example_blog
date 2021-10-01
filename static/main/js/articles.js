

var old_y = 0;
// last article in list
var last_art = 5;
var loading_art = false;

function populate() {
    if (!isNaN(last_art) && !loading_art){
        //while (loading_art);
        // нижняя граница страницы
        let windowRelativeBottom = document.documentElement.getBoundingClientRect().bottom;

        let article_height = document.getElementById( 'end' ).getBoundingClientRect().x;

        console.log(windowRelativeBottom, document.documentElement.clientHeight, article_height)
        if (old_y == windowRelativeBottom || windowRelativeBottom > document.documentElement.clientHeight + article_height) return;
    //        document.getElementById( 'articles' ).insertAdjacentHTML("beforeend", `<p>Date: ${new Date()}</p>`);
        old_y = windowRelativeBottom;


        var url_article = urlApiOfArticleList(last_art)

        console.log(url_article);
        first_last_art = last_art
        loading_art = true;
        $.getJSON(url_article , function ( data, textStatus, jqXHR ) { // указываем url и функцию обратного вызова
            for ( key in data ) { // создаем цикл for in
                a = data[key];
                addArticleOfList(urlOfArticle(a.id), a.article_title, a.article_introduction, a.introduction_img, a.pub_date, a.username)
//                var str = String.format('<p>{0}<br>  {1} </p>', data[key].article_title, data[key].article_introduction);
//                $( "#articles" ).append(str);
                last_art += 1

            };
            console.log('1======= ' + last_art)
            if (first_last_art == last_art){
                last_art = NaN
            };
            loading_art = false;
            console.log('2======= ' + last_art)
            populate();
        })
        
        
    }

}

window.addEventListener('scroll', populate);
// function() {console.log("b" + document.documentElement.getBoundingClientRect().bottom)}

populate(); // инициализация документа


