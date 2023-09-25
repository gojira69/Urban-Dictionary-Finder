const searchButton = document.getElementById('searchButton');
const termInput = document.getElementById('termInput');
const resultDiv = document.getElementById('result');

searchButton.addEventListener('click', () => {
    const term = termInput.value;
    fetch(`/define?term=${term}`)
        .then((response) => response.json())
        .then((data) => {
            resultDiv.innerHTML = `<h2>${term}</h2>`;
            if (data.list && data.list.length > 0) {
                data.list.forEach((item) => {
                    resultDiv.innerHTML += `<p><strong>${item.word}</strong>: ${item.definition}</p>`;
                });
            } else {
                resultDiv.innerHTML += '<p>No definitions found.</p>';
            }
        })
        .catch((error) => {
            resultDiv.innerHTML = `<p>An error occurred: ${error.message}</p>`;
        });
});
