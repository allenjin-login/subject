function css(url){
    let link = document.createElement("link");
    link.rel = "stylesheet";
    link.type = "text/css";
    link.href = url;
    let head = document.createElementsByTagName("head")[0];
    head.appendChild(link);
}  