const URL_API_A = "/api/article/";
const URL_API_U = "/api/user/";

let urlOfArticle = (aid) => "/article/" + aid.toString();
let urlApiOfArticleList = (aid) => URL_API_A + "?i=" + aid.toString();
let urlApiOfUser = (uid) => URL_API_U + uid.toString();

String.format = function() {
    var s = arguments[0];
    for (var i = 0; i < arguments.length - 1; i++) {
    var reg = new RegExp("\\{" + i + "\\}", "gm");
    s = s.replace(reg, arguments[i + 1]);
    }
    return s;
}


function convertDateToStr(date) {
    dt = new Date(date);
    dt_now = new Date();
    diff = dt.getDate() - dt_now.getDate();
    if (diff == 0) {
        str_date = "сегодня";
    } else if (diff == 1) {
        str_date = "вчера";
    } else {
        str_date = dt.toLocaleString('local', {
                                            year: 'numeric',
                                            month: 'long',
                                            day: 'numeric'});
    }
    str_date += " в " + dt.toLocaleTimeString('local', {hour:"2-digit", minute:"2-digit"});
    return str_date
}


function addArticleOfList(url, title, intro, img, pub_date, username) {
    pub_date = convertDateToStr(pub_date);
    if (!username) username = "NoName";
    html_article = `
        <article class="card mb-3" id="article">
            <div class="card-header bg-transparent border-primary">
                ${username}
            </div>`
    if (img){
        html_article += `<img src="${img}" class="card-img-top" alt="Img ${title}">`
    }
    html_article += `
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${intro}</p>
                <div class="row">
                        <div class="col-auto mr-auto"><a href="${url}" class="btn btn-outline-primary">Читать статью</a></div>
                        <div class="col-auto"><p class="card-text"><small class="text-muted">${pub_date}</small></p></div>


                </div>
            </div>
        </article>`
    $("#articles").append(html_article);
    return html_article
}