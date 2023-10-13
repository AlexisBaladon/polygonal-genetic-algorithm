from flask import Blueprint, request

from api.modules.transform import transform_controller

transform_blueprint = Blueprint("transform", __name__)

@transform_blueprint.route("", methods=['GET'])
def image_to_transform():
        return """
    <!DOCTYPE html>
        <html>
        <head>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.2.0/socket.io.js"></script>
            <script type="text/javascript">
                var socket = io.connect('http://' + document.domain + ':' + location.port);

                socket.on('connect', function() {
                    console.log('Connected');

                    // Handle WebSocket events
                    socket.on('update', function(data) {
                        // Process the update received from the server
                        console.log('Update received:', data);
                        // Update the client's UI as needed
                    });
                });

                // Your code to initiate the image processing and send WebSocket events
            </script>
            <title>Image Submission Form</title>
        </head>
        <style>
            form div {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                margin: 10px 0 10px 0;
            }
        </style>
        <body>
            <h1>Submit an Image</h1>
            <div style="justify-content: center; display: flex; width: 100%">
                <form method="POST" enctype="multipart/form-data" 
                    style="width: 250px; justify-content: center; 
                    display: flex; flex-direction: column; 
                    width: 800px;
                ">
                    <div>
                        <label for="image">Image:</label>
                        <input type="file" name="image" accept="image/*" required >
                    </div>
                    <div>
                        <label for="seed">Seed:</label>
                        <input type="number" name="seed" value="0" step="1">
                    </div>
                    <div>
                        <div>
                            <label for="INDPB">INDPB:</label>
                            <input type="number" name="INDPB" value="0.1" step="0.1">
                        </div>
                        <div>
                            <label for="CXPB">CXPB:</label>
                            <input type="number" name="CXPB" value="0.9" step="0.1">
                        </div>
                        <div>
                            <label for="MUTPB">MUTPB:</label>
                            <input type="number" name="MUTPB" value="0.1" step="0.1">
                        </div>
                    </div>
                    <div>
                        <div>
                            <label for="NGEN">NGEN:</label>
                            <input type="number" name="NGEN" value="50" step="1">
                        </div>
                    </div>
                    <div>
                        <div>
                            <label for="MU">MU:</label>
                            <input type="number" name="MU" value="50" step="1">
                        </div>
                        <div>
                            <label for="LAMBDA">LAMBDA:</label>
                            <input type="number" name="LAMBDA" value="50" step="1">
                        </div>
                    </div>
                    <div>
                        <div>
                            <label for="selection">selection:</label>
                            <select name="selection">
                                <option value="best">best</option>
                                <option value="tournament">tournament</option>
                            </select>
                        </div>
                        <div>
                            <label for="tournament_size">tournament_size:</label>
                            <input type="number" name="tournament_size" value="2" step="1">
                        </div>
                        <div>
                            <label for="gaussian_rate">gaussian_rate:</label>
                            <input type="number" name="gaussian_rate" value="0.05" step="0.1">
                        </div>
                    </div>
                    <div>
                        <div>
                            <label for="width">width:</label>
                            <input type="number" name="width" value="None">
                        </div>
                        <div>
                            <label for="height">height:</label>
                            <input type="number" name="height" value="None">
                        </div>
                    </div>
                    <div>
                        <div>
                            <label for="vertex_count">vertex_count:</label>
                            <input type="number" name="vertex_count" value="None">
                        </div>
                        <div>
                            <label for="edge_rate">edge_rate:</label>
                            <input type="number" name="edge_rate" value="0.5" step="0.1">
                        </div>
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </body>
        </html>
"""

@transform_blueprint.route("", methods=['POST'])
def transformed_image():
    return transform_controller.transform(request)