from flask import render_template, json, jsonify

# as the models file contains all the models, import what you need
from app.models import Alpaca

class AlpacaController(object):

    # TODO: Implement Index
    # WHAT: Grabs data from model and uses it to display the relevant
    # alpacas from the database
    # CONDITIONS: If user specifies age, then must filter the list
    # RETURN: Return formatted Alpaca's to use for the view
    def index(self, age):
        data = Alpaca().get_all(age)
        results = []
        for item in data:
            alpaca = {
            'name' : item.name,
            'displayName': item.displayName,
            'profilePic': Alpaca().get_filename(item.name),
            'age': item.age,
            'sex': item.sex
            }
            results.append(alpaca)
        if age != None:
            intage = int(age)
        else:
            intage = age

        return render_template("index.html", results=results, age=intage)
    
    # TODO: Implement Profile
    # WHAT: Grabs the relevant Alpaca from the model and uses it to
    # display the profile for that alpaca from the database
    # RETURN: Return formatted Alpaca to use for the view
    def profile(self, name):
        data = Alpaca().get(name)
        results = {
            'name' : data.name,
            'displayName': data.displayName,
            'profilePic': Alpaca().get_filename(data.name),
            'hobbies': data.hobbiesList,
            'bio': data.bio,
            'hobbies' : data.hobbiesList,
            'contact' : data.contactList
        }
        return render_template("profile.html", results=results, hobbies=results['hobbies'], contact=json.dumps(results['contact']))
    
    # TODO: Implement Search
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # CONDITIONS: If user specifies nothing you can return everything or nothing!
    # that part if determined by you however if something is specified, it must
    # be a filtered list of alpacas
    # RETURN: Return formatted alpacas as a list using the
    # search criteria
    def search(self, name):
        if name == None:
            results = {
            'message' : "you gave no parameters. could find no users"
            }
        else : 
            data = Alpaca().get_all()
            results = {
            'message' : []
            }
            for item in data:
                if name in item.name:
                    results['message'].append("searching with the letter " + name + " we found the following user: " + item.name + "\n")
                    print("using " + name + " we found the following user: " + item.name)

        return jsonify(results)
    
    # TODO: Implement Create
    # WHAT: Uses the data recieved to create an Alpaca model
    # REQUIREMENTS: Make a 'fake' save function in Alpaca that
    # Prints saving alpaca and then list the information recieved
    # and then give back a message stating what was saved
    # i.e Fred was created!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def create(self, name, sex, bio, dName, age, hobbiesList, contactList):
        alpaca = Alpaca(name, sex, bio, dName, age, hobbiesList, contactList)
        data = {'message': "successfully created the following user: " + name + "\n using the current profile name: " + dName}
        print('saving alpaca', name, sex, bio, dName, age, hobbiesList, contactList)

        return jsonify(data)

    # TODO: Implement Delete
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # and then deletes it
    # REQUIREMENTS: Make a 'fake' delete function in Alpaca that
    # Prints the alpaca that will be delted followed by deleting alpaca
    # and then list the information recieved and then give back a
    # message stating what was saved i.e Fred was deleted!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def delete(self, name):
        deletedAlpaca = Alpaca().get(name)
        data = {'message': "successfully delete the following user: " + deletedAlpaca.name}
        print('deleting alpaca', deletedAlpaca.name)

        return jsonify(data)

alpaca_controller = AlpacaController()