window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id='simpletext'>>></a><a class='responsive-font1' id='textyoastsecond'>News</a>"
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("newsBTN").className = "nav-item active";
}