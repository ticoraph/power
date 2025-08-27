// Charge le fichier JSON généré par Python
fetch('data/data.json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('message').textContent = "Erreur lors du chargement.";
        console.error(error);
    });