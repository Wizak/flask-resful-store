from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = (
    "/static/swagger.json"
)  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See swagger-ui docs.
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

# Now point your browser to localhost:5000/api/docs/
