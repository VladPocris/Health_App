window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id=" + "simpletext" + ">>></a> <a id=" + "textyoastsecond" + ">Calendar</a>";
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("calendarBTN").className = "nav-link active";
}