
async function send(){
    
    // получаем введеные данные
    const sity = document.getElementById("location").value;

    // отправляем запрос
    const response = await fetch("/weather", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({ 
                sity: sity,
            })
        });
        if (response.ok) {
            const data = await response.json(); 
            await print_datas(data)

        }
        else {
            console.log(response);
            print_error()}
}


async function print_datas(datas) {

    // Перед добавлением данных на страницу, удаляет страые данные
    delete_old_datas("search")

    // Добавляет элемент 
    text = ``
    for (elem in datas.message.current){
        div = document.createElement('div');
        div.id = "search";
        text += `<p>${elem}: ${datas.message.current[elem]}</p>`;
    }
    div.innerHTML = text
    document.body.append(div);
}


async function print_error() {

    // Перед добавлением данных на страницу, удаляет страые данные
    delete_old_datas("search")

    div = document.createElement('div');
    div.id = "search";
    div.innerHTML = "<p>Сервис не смог найти это место</p>"
    document.body.append(div)
}



async function delete_old_datas(elem_id) {

    // Удаляет элемент если он есть на странице
    if (document.getElementById(elem_id)){
        document.getElementById(elem_id).remove()
    }
}