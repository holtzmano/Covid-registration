from django.http import HttpResponse

get_citizens_page = """



<html>
    <head>
        <title>Vaccination DB - Citizens' Data </title>
    </head>
    <body>
        <div id="root"></div>

        <!-- Load React -->
        <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>


        <script type="text/babel">

            const VaccinationsData = () => {
                const [citizensDataValue, setCitizensDataValue] = React.useState([]);
                const [cityValue, setCityValue] = React.useState("");

                const init = () => {
                    const requestOptions = {
                        method: 'GET',
                        headers: { 'Content-Type': 'application/json' }
                    };
                    fetch('get_data', requestOptions)
                        .then(response => response.json())
                        .then(data => setCitizensDataValue(data));
                };

                React.useEffect(() => {
                    init();      
                }, []);
                
                React.useEffect(() => {
                       
                }, [cityValue]);
                
                const createTable = () => {
                    
                };

                return (
                    <div>
                        <label>
                            Choose a city:
                            <select onChange={(e) => setCityValue(e.target.value)}>
                                <option value=""></option>
                                <option value="Tel-Aviv">Tel-Aviv</option>
                                <option value="Jerusalem">Jerusalem</option>                              
                            </select>
                        </label>
                       
                        <table>
                            <thead>
                                <tr>
                                    <th>First Name</th>
                                    <th>Last Name</th>
                                    <th>Date of Birth</th>
                                    <th>Address</th>
                                    <th>City</th>
                                    <th>Zipcode</th>
                                    <th>Landline</th>
                                    <th>Cellular Phone</th>
                                    <th>Infected</th>
                                    <th>Diabetes</th>
                                    <th>Cardio vascular</th>
                                    <th>Allergies</th>
                                    <th>Previous Conditions- Other</th>
                                </tr>
                            </thead>
                            <tbody>
                            {
                                citizensDataValue.map((citizen_data) => cityValue != "" && citizen_data.city != cityValue ? 
                                    <div></div> :
                                    <tr>
                                        <td>{citizen_data.first_name}</td>
                                        <td>{citizen_data.last_name}</td>
                                        <td>{citizen_data.date_of_birth}</td>
                                        <td>{citizen_data.address}</td>
                                        <td>{citizen_data.city}</td>
                                        <td>{citizen_data.zip_code}</td>
                                        <td>{citizen_data.land_line}</td>
                                        <td>{citizen_data.cellular_phone}</td>
                                        <td>{citizen_data.infected ? "yes" : "no"}</td>
                                        <td>{citizen_data.previous_conditions.diabetes ? "yes" : "no"}</td>
                                        <td>{citizen_data.previous_conditions.cardio_vascular ? "yes" : "no"}</td>
                                        <td>{citizen_data.previous_conditions.allergies ? "yes" : "no"}</td>
                                        <td>{citizen_data.previous_conditions.other}</td>
                                    </tr>)
                            }
                            </tbody>
                        </table>
                    </div>
                );
            }
            
            const root = ReactDOM.createRoot(document.getElementById('root'));
            root.render(<VaccinationsData />);
        </script>
    </body>
</html>
"""

def get_citizens_data(request):
    return HttpResponse(get_citizens_page)

