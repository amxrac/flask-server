# Local LLM API Gateway

  

A lightweight Flask-based API gateway that provides a simplified interface to Ollama LLM services, enabling seamless integration with large language models in applications.

  

## Features

  

- **Simplified API Interface**: Abstracts the complexity of direct Ollama API calls
- **Cross-Origin Support**: Configured with CORS for browser-based applications
- **Error Handling**: Robust error management with informative responses
  

## Technical Implementation

  

This service implements a clean API gateway pattern with O(1) routing complexity, forwarding client requests to the Ollama backend service. The implementation:

  

- Uses a stateless architecture for horizontal scalability
- Implements proper HTTP status code responses
- Provides JSON response formatting for client consumption
- Includes configurable model selection (currently using llama3.1)

  

## Usage

  

### Running the Service

  ```
# Install dependencies
pip install -r requirements.txt

# Start the server  
python app.py
```


The service will be available at `http://localhost:5000`.

  

### API Endpoints

  

#### Generate Text

`POST /generate`

  

**Request Body:**
```
{  
  "prompt": "Your prompt here"  
}
```
  

**Response:**
```
{  
  "response": "Generated text from the LLM..."  
}
```
  

## Architecture
  

This service follows a proxy pattern, acting as an intermediary between client applications and Ollama's LLM service. The separation provides:
  

1. A simplified interface for client applications
2. Potential for adding authentication, rate limiting, and monitoring
3. Ability to switch underlying LLM services without client changes

  
## Requirements

  

- Python 3.8+
- Flask
- Requests
- Flask-CORS
- Ollama running locally on port 11434

  
