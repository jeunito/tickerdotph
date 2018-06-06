function tickerdotph(ticker) {
    var url = "${URL}/funds/" + ticker; // replace ${URL} variable with url to tickerdotph rest api
    var res = UrlFetchApp.fetch(url).getContentText();
    var fund = JSON.parse(res);
    return fund.price
}
