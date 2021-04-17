console.log('loaded script');

function searchUser () {

    // const data = {
    //     name: 'Ph'
    // }

    fetch(
        "/search/e",
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            },
            // body: JSON.stringify(data)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("found users!", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );
}