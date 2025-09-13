# Sample Python Application Code

Although simple in nature, this application uses a structure by type folder structure. The choice of this implementation is done
as the application itself is small. For larger application I would suggest a structure by feature decomposition.
An interesting article describing the difference between the two can be found here [Structure by Type vs Feature](https://maestros.io/structure-by-type-vs-feature)


## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/hikarilabs/error-buddy-ai-agent.git
   ```

2. **Navigate to the sample application and open it into its own IDE folder**
    ```bash
    cd fastapi-demo-service
    ```

3. **Create a virtual environment for this application and run the upgrade script**
    ```bash
    python3 -m venv venv
    
    . venv/bin/activate
    
    python -m pip install --upgrade pip
    
    pip install --upgrade setuptools wheel
    ```

4. **Install dependencies: Required only if deployed on localhost**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   - API Main Endpoint: http://localhost:8000/api
   - Health Check: http://localhost:8000/api/health

## Architecture

- **Endpoints Layer**: FastAPI endpoints for handling HTTP requests
- **Schemas Layer**: Pydantic models for data validation
- **Services Layer**: Business logic implementation, in this case an error generator
