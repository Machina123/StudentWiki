const languageButton = document.querySelector('button.btn.btn-languages');

languageButton.addEventListener('click',()=>{
    let siteHref = document.location.href;
    siteHref = siteHref.replace('/pl/','/en/');
    console.log(siteHref);
    window.open(siteHref);
});
