function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }

async function setCookie() {
    // Отправляем запрос на сервер для создания cookie
    const response = await fetch("/cookie");
}

if (getCookie("user_id")) {
    console.log('Cookies exist');
    
}else{
    console.log('No cookies');
    setCookie();
}