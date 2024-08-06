
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
            document.getElementById("message").textContent = data.message;
        }
        else
            console.log(response);
}