async function Getreim(){

    const id = document.getElementById("idInput").value
    const url = `http://localhost:5000//reimburstment/${id}`

    const httpResponse = await fetch(url)
    const body = await httpResponse.json()

    console.log(body)

}