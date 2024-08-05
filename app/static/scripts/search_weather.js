

function send(){
 
    // Получаем введенный город
    const location = document.getElementById("location").value;

    // Отправляем запрос
    const response = fetch("/weather", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({ 
                location: location
            })
        });
        if (response.ok) {
            // Если получили ответ, то печатаем его
            const data = response.json();
            document.getElementById("weather").textContent = data.weather;
        }
        else
            console.log(response);
}