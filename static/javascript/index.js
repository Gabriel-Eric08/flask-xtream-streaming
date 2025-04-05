function setCredentials() {
    event.preventDefault();

    let playlist_name = document.getElementById('Playlist_name').value;
    let username = document.getElementById('Username').value;
    let password = document.getElementById('Password').value;
    let url_xtream = document.getElementById('Url_xtream').value;

    let data = {
        "Playlistname": playlist_name,
        "Username": username,
        "Password": password,
        "URL_Xtream": url_xtream
    };

    console.log("Enviando dados:", data);
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    };

    fetch('http://127.0.0.1:5000/auth/', options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro ${response.status}: ${response.statusText}`);
            }
            return response.json();
        })
        .then(update => {
            console.log("Resposta do servidor:", update);
            
            if (update.redirect) {
                window.location.href = update.redirect; // Redireciona para a página de destino
            } else {
                alert("Credenciais registradas com sucesso!");
            }
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
            alert("Erro ao registrar as credenciais. Verifique o console para mais detalhes.");
        });
}