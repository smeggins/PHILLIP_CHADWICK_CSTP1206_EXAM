console.log('loaded script');

function hello() {
    const helloDiv = document.querySelector('#hello-data')

    console.log('data set is: ', helloDiv.dataset.hello)
    const data = JSON.parse(helloDiv.dataset.hello)
    console.log('the data is: ', data)

    let output = ''
    if (data.phoneNumber) {
        output += 'Phone Number: ' + data.phoneNumber
    }
    if (data.email) {
        if (data.phoneNumber) {
            output += '\n'
        }
        output += 'Email: ' + data.email
    }
    window.alert(output)
}

function createUser () {

    const data = {
        name: 'Jimmy Jam',
        sex: 'Male',
        bio: 'The jimmest jam that ever jimmed',
        dName: document.getElementById('userName').innerHTML,
        age: '42',
        hobbiesList: ['jimming', 'jamming', 'jimming and jamming at the same time'],
        contactList: {'email': 'horseHockey@anEmail.com', 'phoneNumber': '(123)456-7890'}
    }

    fetch(
        "/create",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("successful post", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );
}

    function deleteUser () {

    const deleteUser = document.querySelector('#delete-data')
    console.log(deleteUser.dataset.delete)

    fetch(
        "/delete",
        {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(deleteUser.dataset.delete)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("successful post", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );
}