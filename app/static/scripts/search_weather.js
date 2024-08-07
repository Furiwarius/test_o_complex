
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
            await print_current_datas(data)

        }
        else
            console.log(response);
}


async function print_current_datas(datas) {

    // Перед добавлением данных на страницу, удаляет страые данные
    delete_old_datas("search")

    // Добавляет элемент 
    text = ``
    div = document.createElement('div');
    div.id = "search";
    for (elem in datas.message.current){
        
        if (elem!="rain" && elem!="snowfall") {
            text += `<p>${elem}: ${datas.message.current[elem]}</p>`;
        }
        else if (elem=="rain" && datas.message.current[elem]!=0) {
            text += "<p>It is raining</p>";
        }
        else if (elem=="snowfall" && datas.message.current[elem]!=0) {
            text += "<p>It is snowing</p>";
        }
    }
    div.innerHTML = text
    document.body.append(div);
}



async function delete_old_datas(elem_id) {

    // Удаляет элемент если он есть на странице
    if (document.getElementById(elem_id)){
        document.getElementById(elem_id).remove()
    }
}