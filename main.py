from website import create_app  # Import the create_app function from the website package
from flask import after_this_request

# Create an instance of the Flask application using the factory function
app = create_app()

# Add no-cache headers to all responses to ensure the latest content is always served
@app.after_request
def add_header(response):
    response.cache_control.no_store = True  # Prevent storing the response in cache
    response.cache_control.no_cache = True  # Prevent using any cached version of the response
    response.cache_control.must_revalidate = True  # Require cache validation with the server before using a cached response
    response.cache_control.max_age = 0  # Set max age to 0 to indicate the response is stale immediately
    response.expires = 0  # Set expiration to 0 to expire immediately
    return response

# Run the Flask application in debug mode when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)   # Enable debug mode for better error messages and automatic reloads
